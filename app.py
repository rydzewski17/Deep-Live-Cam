import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Deep Live Cam – Browser Webcam")

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    # You can call Deep-Live-Cam face swap logic here instead of this line
    img = cv2.putText(img, "Live", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="deep-live-cam",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False}
)
