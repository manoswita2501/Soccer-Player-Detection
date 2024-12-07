import streamlit as st
from moviepy.editor import VideoFileClip

# Function to compress video
def compress_video(input_path, output_path, target_resolution=(720, 480)):
    clip = VideoFileClip(input_path)
    clip_resized = clip.resize(height=target_resolution[1])  # Resize to target resolution
    clip_resized.write_videofile(output_path, codec="libx264", audio_codec="aac", preset="medium")
    return output_path

# Specify video paths
input_video_path = "path_to_your_large_video.mp4"
compressed_video_path = "compressed_video.mp4"

# Compress the video
st.write("Compressing video... This may take a moment.")
try:
    compressed_path = compress_video(input_video_path, compressed_video_path)
    st.success("Video compressed successfully!")
    
    # Display the compressed video
    with open(compressed_path, "rb") as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes, format="video/mp4")
except Exception as e:
    st.error(f"An error occurred: {e}")
