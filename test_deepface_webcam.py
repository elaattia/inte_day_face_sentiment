import cv2
from deepface import DeepFace

cam = cv2.VideoCapture(0)
print("Press 'c' to capture a frame for emotion detection, or 'q' to quit.")

while True:
    ret, frame = cam.read()
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            # Si le résultat est une liste, prends le premier élément
            if isinstance(result, list) and len(result) > 0:
                result = result[0]
            if 'dominant_emotion' in result:
                print("Detected emotion:", result['dominant_emotion'])
            else:
                print("No emotion detected. Try again with better lighting and face towards camera.")
        except Exception as e:
            print("Face not detected! Error:", e)
    elif key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()