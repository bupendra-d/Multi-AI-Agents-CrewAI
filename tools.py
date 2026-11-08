import re
from urllib.parse import urlparse, parse_qs

from crewai.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(video_url: str) -> str:
    """Extract the YouTube video ID from a URL."""

    parsed_url = urlparse(video_url)
    hostname = parsed_url.hostname or ""

    if hostname in ("youtube.com", "www.youtube.com", "m.youtube.com"):
        video_id = (
            parse_qs(parsed_url.query).get("v", [None])[0]
            or re.search(r"/(?:shorts|embed)/([\w-]+)", parsed_url.path)
        )

        if hasattr(video_id, "group"):
            video_id = video_id.group(1)

    elif hostname == "youtu.be":
        video_id = parsed_url.path.strip("/")

    else:
        video_id = None

    if not video_id or not re.fullmatch(r"[\w-]{11}", video_id):
        raise ValueError("Please provide a valid YouTube video URL.")

    return video_id



@tool("YouTube Transcript Tool")
def yt_tool(video_url: str, language: str = "en") -> str:
    """Extract an English or Hindi YouTube transcript."""

    video_id = get_video_id(video_url)

    try:
        transcript = YouTubeTranscriptApi().fetch(
            video_id,
            languages=[language]
        )

        return " ".join(
            snippet.text for snippet in transcript
        )

    except Exception as error:
        raise RuntimeError(
            f"Unable to extract {language} transcript: {error}"
        ) from error
