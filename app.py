import streamlit as st
import time
import os

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .sidebar .sidebar-content {
        background-color: #f1f1f1;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: small;
        font-style: italic;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Logo and Title
logo_path = "logo.png"
conf_matrix_path = "conf_matrix.png"
training_results_path = "training_results.png"

if page == "Home":
    # Display the logo with a smaller width
    st.image(logo_path, width=600, caption="VisionHack: Arunoth || Manoswita")
    
    # Title
    st.markdown("<h1 style='text-align: center; color: #97AB47;'>⚽ Soccer Player Detection</h1>", unsafe_allow_html=True)

    # Video Upload
    uploaded_file = st.file_uploader("Upload your soccer video", type=["mp4", "avi", "mov"])

    # Placeholder for uploaded video
    if uploaded_file:
        st.video(uploaded_file)
        st.success("Video uploaded successfully!")

        # Button to start "processing"
        if st.button("Detect Players"):
            st.markdown("<h4 style='color: #17a2b8;'>Detecting players in the video... Please wait!</h4>", unsafe_allow_html=True)
            with st.spinner("Processing..."):
                time.sleep(5)  # Simulate 5 seconds delay

            # Check and display the output video
            output_video_path = "detected_players.mp4"  # Replace with your video path

            try:
                # Read the video file as bytes
                with open(output_video_path, "rb") as video_file:
                    video_bytes = video_file.read()

                # Display the video directly
                st.video(video_bytes)

                # Add a download button
                st.download_button(
                    label="Download Processed Video",
                    data=video_bytes,
                    file_name="output.mp4",
                    mime="video/mp4"
                )

                st.success("Detection complete!")

            except FileNotFoundError:
                st.error("Output video file not found!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Buttons to display images
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #F84D9E;'>Visualize Results</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Display Confusion Matrix"):
            st.image(conf_matrix_path, caption="Confusion Matrix", use_container_width=True)
    
    with col2:
        if st.button("Display Training Results"):
            st.image(training_results_path, caption="Training Results", use_container_width=True)

elif page == "About":
    # About Section Content
    st.title("About the Project")
    st.markdown("""
    <p style="font-size: 16px; line-height: 1.6;">
    This project was created by <b>Manoswita Bose (2347238)</b> and <b>Arunoth Symen (2347215)</b> from <b>5MCA-B</b> as part of the VisionHack challenge.
    </p>

    <h4 style="color: #007bff;">Motivation:</h4>
    <p style="font-size: 16px; line-height: 1.6;">
    The project was inspired by a shared interest in applying a cutting-edge deep learning model like YOLOv8 (You Only Look Once) to solve real-world problems. By detecting soccer players in videos, we aimed to showcase the potential of AI in sports analytics and beyond.
    </p>

    <h4 style="color: #007bff;">Environment Setup:</h4>
    <ul>
        <li>Check GPU status and ensure the required libraries are installed, including ultralytics (for YOLO) and roboflow (for dataset management).</li>
    </ul>

    <h4 style="color: #007bff;">Pretrained Model Usage:</h4>
    <ul>
        <li>A pretrained YOLOv8 model (<code>yolov8n.pt</code>) is used to perform object detection on a sample image.</li>
        <li>Detected objects are visualized, and details like bounding boxes, confidence scores, and class IDs are extracted.</li>
    </ul>

    <h4 style="color: #007bff;">Custom Dataset Integration:</h4>
    <ul>
        <li>Connect to Roboflow, a platform for dataset management, using an API key.</li>
        <li>Download a football/soccer dataset to demonstrate training on a specific use case.</li>
    </ul>

    <h4 style="color: #007bff;">Training the Model:</h4>
    <p style="font-size: 16px; line-height: 1.6;">
    Train the YOLO model on the dataset for 30 epochs. Evaluate training using key metrics, including a confusion matrix and performance results.
    </p>

    <h4 style="color: #007bff;">Future Scope:</h4>
    <p style="font-size: 16px; line-height: 1.6;">
    If given an opportunity, we can extend this workflow for analyzing player stats in all games.
    </p>
    """, unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
    Made with ❤️ for VisionHack by Manoswita Bose & Arunoth Symen.
    </div>
    """,
    unsafe_allow_html=True,
)
