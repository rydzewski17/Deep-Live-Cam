import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.title("Deep Live Cam – Browser Webcam Test")

def video_frame_callback(frame):
    return frame  # Just show webcam feed with no changes

webrtc_streamer(
    key="deep-live-cam",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False}
)
