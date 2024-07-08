import cv2
from deepface import DeepFace
import flet as ft
import threading

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to perform emotion detection
def detect_emotion(emotion_text):
    # Start capturing video
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale frame to RGB format
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = rgb_frame[y:y + h, x:x + w]

            # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']

            # Update the emotion text in the Flet app
            emotion_text.value = f"Detected Emotion: {emotion}"
            emotion_text.update()

        # Display the resulting frame
        cv2.imshow('Real-time Emotion Detection', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Main Flet app function
def main(page: ft.Page):
    page.title = "Emotion Detection App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create a text field to display the emotion
    emotion_text = ft.Text(value="", size=24, weight=ft.FontWeight.BOLD)

    # Create a button to start emotion detection
    def start_detection(e):
        threading.Thread(target=detect_emotion, args=(emotion_text,)).start()

    start_button = ft.ElevatedButton(text="Start Emotion Detection", on_click=start_detection)

    # Add controls to the page
    page.add(
        ft.Column(
            controls=[
                start_button,
                emotion_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Run the Flet app
ft.app(target=main)
