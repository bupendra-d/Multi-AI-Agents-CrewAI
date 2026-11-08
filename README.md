# Multi-AI Agents using CrewAI 

An AI-powered multi-agent application that researches YouTube videos and generates structured blog articles in **English and Hindi** using CrewAI, Groq, and Supadata.

## Live Demo

[Try Multi-AI Agents](https://multi-ai-agents-crewai-ew6ee3sqqxyyr3ryh5wpd6.streamlit.app/)

## Features

- Two specialized AI agents: Blog Researcher and Blog Writer.
- YouTube transcript extraction using Supadata API.
- English and Hindi video support.
- Sequential multi-agent task execution.
- LLM integration using Groq (GPT-OSS-20B).
- Streamlit web interface.
- Download generated blogs in Markdown format.

## Tech Stack

- Python
- CrewAI
- Groq API (GPT-OSS-20B)
- Supadata API
- Streamlit
- Requests

## How It Works

1. Enter a YouTube video URL.
2. Select the transcript language (English or Hindi).
3. The Researcher agent extracts and analyzes the transcript.
4. The Writer agent generates a structured blog.
5. View and download the generated blog.

## Installation

```bash
git clone https://github.com/bupendra-d/Multi-AI-Agents-CrewAI.git

cd Multi-AI-Agents-CrewAI

pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
SUPADATA_API_KEY=your_supadata_api_key
```

## Run Locally

```bash
streamlit run app.py
```

## Note

Transcript availability depends on the video and Supadata API access. API usage may be subject to service limits.

