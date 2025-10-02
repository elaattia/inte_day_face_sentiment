import streamlit as st
import cv2
from deepface import DeepFace
import time

EMOTION_MESSAGES = {
    "happy": "You're happy because you love the CS team! Would you like to join us?",
    "neutral": "You look neutral. Maybe you want to learn more about the IEEE CS Chapter!",
    "sad": "You seem sad. Join our team to have more fun and make new friends!",
    "surprise": "Surprised? Discover amazing technical projects with IEEE CS!",
    "angry": "Feeling angry? Our team spirit will cheer you up!",
    "fear": "Don't worry, technical adventures and support await you here!",
    "disgust": "Let's turn that mood around with cool projects and teamwork!",
}

st.title("IEEE CS Chapter Integration Day Game")
st.write("We analyze your emotion live! Look at the camera to see your sentiment and a custom message.")

if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

col1, col2 = st.columns(2)
if col1.button("Open Camera", key="open"):
    st.session_state.camera_on = True
if col2.button("Close Camera", key="close"):
    st.session_state.camera_on = False

stframe = st.empty()
message_box = st.empty()

if st.session_state.camera_on:
    cam = cv2.VideoCapture(0)
    last_time = time.time()
    while st.session_state.camera_on:
        ret, frame = cam.read()
        if not ret:
            st.warning("Could not access the camera.")
            st.session_state.camera_on = False
            break
        small_frame = cv2.resize(frame, (640, 480))
        stframe.image(cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB), channels="RGB")
        if time.time() - last_time > 2:
            try:
                result = DeepFace.analyze(small_frame, actions=['emotion'], enforce_detection=False)
                # Si le résultat est une liste, prends le premier élément
                if isinstance(result, list) and len(result) > 0:
                    result = result[0]
                if 'dominant_emotion' in result:
                    emotion = result['dominant_emotion']
                    msg = EMOTION_MESSAGES.get(emotion, "Welcome to the IEEE CS Chapter!")
                    message_box.success(f"Detected Emotion: {emotion.capitalize()}\n\n{msg}")
                else:
                    message_box.warning("No emotion detected. Try again with better lighting and face towards camera.")
            except Exception as e:
                message_box.warning(f"Face not detected. Please look at the camera and ensure good lighting!\n{e}")
            last_time = time.time()
        time.sleep(0.1)
    cam.release()
    st.success("Camera closed.")