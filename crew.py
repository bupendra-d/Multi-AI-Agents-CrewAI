import os
from dotenv import load_dotenv

import crewai.llms.cache as crew_cache
crew_cache.mark_cache_breakpoint = lambda msg: msg
from crewai import Agent, Task, Crew, Process, LLM
from tools import yt_tool

import streamlit as st

load_dotenv()


def generate_blog(video_url: str, language: str = "en"):
    api_key = ( 
        os.getenv("GROQ_API_KEY")
        or st.secrets.get("GROQ_API_KEY", None)
    )

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

    # Initialize LLM
    llm = LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=api_key,
        temperature=0.5
    )

    # Agent 1: Blog Researcher
    researcher = Agent(
        role="YouTube Content Researcher",
        goal="Extract and analyze relevant information from the given YouTube video.",
        backstory=(
            "An experienced researcher specializing in Artificial Intelligence, "
            "Machine Learning, Data Science, Deep Learning and Generative AI."
        ),
        llm=llm,
        tools=[yt_tool],
        verbose=False
    )

    # Agent 2: Blog Writer
    writer = Agent(
        role="Technical Blog Writer",
        goal=("Extract and analyze the YouTube video transcript in the"
        "requested language: {language}."
        ),
        backstory=(
            "A professional technical writer who simplifies complex "
            "technologies into clear, engaging and informative articles."
        ),
        llm=llm,
        verbose=False
    )

    # Research Task
    research_task = Task(
        description=(
            "Extract the transcript from this YouTube video: {video_url}. "
            "The requested transcript language is {language}. "
            "Analyze the complete transcript and identify its main topics, "
            "important concepts, explanations and key takeaways."
            ),
        expected_output=(
            "A detailed and well-organized research report covering "
            "the important information from the video."
        ),
        agent=researcher
    )

    # Writing Task
    writing_task = Task(
        description=(
            "Using the research findings from the previous task, "
            "write a comprehensive blog article about the video. "
            "Include an appropriate title, introduction, meaningful "
            "headings, explanations and conclusion. "
            "Maintain accuracy and avoid adding unsupported information."
        ),
        expected_output=(
            "A well-structured Markdown blog post based on the "
            "YouTube video's content."
        ),
        agent=writer,
        context=[research_task]
    )

    # Create Crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff(
        inputs={
            "video_url" : video_url,
            "language" : language
            }
        )
    
    return research_task.output.raw, result.raw

