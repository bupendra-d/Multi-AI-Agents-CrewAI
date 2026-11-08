import os
import re
import requests

import streamlit as st
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from crewai.tools import tool

load_dotenv()


def get_video_id(video_url: str) -> str:
    """Extract YouTube video ID from a URL."""

    parsed_url = urlparse(video_url)
    hostname = parsed_url.hostname or ""

    if hostname in ("youtube.com", "www.youtube.com", "m.youtube.com"):
        video_id = (
            parse_qs(parsed_url.query).get("v", [None])[0]
            or re.search(r"/(?:shorts|embed|live)/([\w-]+)", parsed_url.path)
        )

        if hasattr(video_id, "group"):
            video_id = video_id.group(1)

    elif hostname in ("youtu.be", "www.youtu.be"):
        video_id = parsed_url.path.strip("/").split("/")[0]

    else:
        video_id = None

    if not video_id or not re.fullmatch(r"[\w-]{11}", video_id):
        raise ValueError("Please provide a valid YouTube video URL.")

    return video_id


def get_supadata_api_key():
    """Load Supadata API key from environment or Streamlit Secrets."""

    api_key = os.getenv("SUPADATA_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets.get("SUPADATA_API_KEY")
        except Exception:
            api_key = None

    if not api_key:
        raise ValueError("SUPADATA_API_KEY is missing.")

    return api_key


@tool("YouTube Transcript Tool")
def yt_tool(video_url: str, language: str = "en") -> str:
    """Extract English or Hindi YouTube transcripts using Supadata."""

    video_id = get_video_id(video_url)
    api_key = get_supadata_api_key()

    video_url = f"https://www.youtube.com/watch?v={video_id}"

    try:
        response = requests.get(
            "https://api.supadata.ai/v1/transcript",
            params={
                "url": video_url,
                "text": "true",
                "lang": language
            },
            headers={
                "x-api-key": api_key
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()
        transcript = data.get("content", "")

        if not transcript:
            raise ValueError("No transcript available for this video.")

        return transcript

    except requests.exceptions.RequestException as error:
        raise RuntimeError(
            f"Supadata transcript extraction failed: {error}"
        ) from error
