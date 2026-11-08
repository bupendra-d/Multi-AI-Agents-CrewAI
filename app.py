import streamlit as st
from crew import generate_blog


# Page configuration
st.set_page_config(
    page_title="Multi-AI Agents | CrewAI"
)


# Application header
st.title("Multi-AI Agents - YouTube Blog Generator")

st.markdown(
    "An AI-powered multi-agent system that researches "
    "YouTube videos and generates informative blog articles "
    "using CrewAI and Groq."
)

st.divider()


# YouTube URL input
video_url = st.text_input(
    "Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

language = st.selectbox(
    "Select Video Language",
    options=["English", "Hindi"],
    index=0
)

language_code = {
    "English": "en",
    "Hindi": "hi"
}[language]


# Generate button
if st.button("Generate Blog", type="primary"):

    if not video_url.strip():
        st.warning("Please enter a YouTube video URL.")

    else:
        try:
            with st.spinner(
                "AI Agents are researching and writing your blog..."
            ):
                research, blog = generate_blog(
                    video_url.strip(),
                    language_code
                    )

            st.success("Blog generated successfully!")

            # Research output
            with st.expander("View Researcher's Findings"):
                st.markdown(research)

            # Final blog output
            st.subheader("Generated Blog")
            st.markdown(blog)

            # Download generated blog
            st.download_button(
                label="Download Blog",
                data=blog,
                file_name="generated_blog.md",
                mime="text/markdown"
            )

        except Exception as error:
            st.error(f"Something went wrong: {error}")
