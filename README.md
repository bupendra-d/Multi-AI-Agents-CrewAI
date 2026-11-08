# Multi-AI Agents using CrewAI

An AI-powered multi-agent application that researches YouTube videos and generates structured blog articles in **English and Hindi** using CrewAI and Groq.

## Live Demo

[Try Multi-AI Agents](https://multimodal-rag-ps3hdzzmkqjwpqumkwgcwq.streamlit.app/)

## Features
- Two specialized AI agents: Blog Researcher and Blog Writer.
- Automated YouTube transcript extraction.
- English and Hindi video support.
- Sequential multi-agent task execution.
- LLM integration using Groq (GPT-OSS-20B).
- Streamlit web interface.
- Download generated blogs in Markdown format.

## Tech Stack
- Python
- CrewAI
- Groq API (GPT-OSS-20B)
- Streamlit
- YouTube Transcript API

## How It Works
1. Enter a YouTube video URL.
2. Select the video transcript language (English or Hindi).
3. The Researcher agent extracts and analyzes the transcript.
4. The Writer agent generates a structured blog.
5. View and download the generated blog.

## Installation

```bash
git clone https://github.com/bupendra-d/Multi-AI-Agents-CrewAI.git

cd Multi-AI-Agents-CrewAI

pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run Locally

```bash
streamlit run app.py
```

## Note
YouTube videos must have accessible transcripts in the selected language. Transcript availability and API access may vary.
