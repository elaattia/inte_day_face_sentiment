# IEEE CS Chapter Face Sentiment Game

This project contains two main Python files for facial emotion recognition using DeepFace and OpenCV:

- **face_sentiment_game_web.py**: A Streamlit web app for live sentiment detection via webcam.
- **test_deepface_webcam.py**: A simple test script to check DeepFace emotion recognition using your webcam.

---

## 1. Prerequisites

- Python 3.8 or above installed
- Webcam connected and working

### Install required packages

Run in your terminal:
```bash
pip install streamlit opencv-python deepface Pillow
```

---

## 2. File Descriptions

### face_sentiment_game_web.py

**Purpose:**  
A Streamlit web application for live emotion detection. It analyzes facial emotion in real-time and displays a custom message based on the detected sentiment.

**Usage:**
1. Open terminal and navigate to your project directory.
2. Run:
   ```bash
   streamlit run face_sentiment_game_web.py
   ```
3. In your browser, click **Open Camera** to start the webcam feed.
4. Look at the camera; your detected emotion and a custom message will display.
5. Click **Close Camera** to stop the webcam.

**Features:**
- Live webcam feed.
- Automatic emotion detection every 2 seconds.
- Custom messages based on emotion.
- Works best with good lighting and a visible face.

---

### test_deepface_webcam.py

**Purpose:**  
A minimal OpenCV script to check if DeepFace can detect emotions from your webcam.

**Usage:**
1. Open terminal and navigate to your project directory.
2. Run:
   ```bash
   python test_deepface_webcam.py
   ```
3. A webcam window opens.
4. Press **c** to capture a frame and analyze emotion.
   - The detected emotion is printed in the terminal.
5. Press **q** to quit.

**Features:**
- Useful for verifying DeepFace installation and webcam compatibility.
- Prints emotion labels to the console.

---

## 3. Troubleshooting

- If no emotion is detected, ensure your face is well-lit and centered.
- Update DeepFace if errors occur:
  ```bash
  pip install --upgrade deepface
  ```
- If the webcam does not work, check your device permissions and try another camera.

---

## 4. Customization

- You can edit the `EMOTION_MESSAGES` dictionary in `face_sentiment_game_web.py` to display custom messages for each emotion.

---

## 5. License

This project is intended for educational and IEEE CS Chapter promotional use.
