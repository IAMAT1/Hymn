import streamlit as st
from downloader import download_song

st.set_page_config(page_title="In-Memory Music Streamer", layout="centered")

st.title("🎵 HuggingFace Music Streamer (Now on Render!)")

query = st.text_input("Enter song name to stream from YouTube:")

if query:
    with st.spinner("Fetching and converting..."):
        try:
            title, mp3_data = download_song(query)
            st.success(f"Now Playing: {title}")
            st.audio(mp3_data, format="audio/mp3")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
