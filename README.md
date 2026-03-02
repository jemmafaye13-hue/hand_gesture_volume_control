# Hand Gesture Volume Control 

This is a Python-based AI application that uses opencv and mediapipe to control your computer's system volume using hand gestures.

# Features
- Real-time Hand Tracking: Powered by MediaPipe.
- Dynamic Feedback: Visual lines and circles change color based on hand distance.
- Volume Control:
   - Pinch Gesture: Lowers volume (Distance < 50).
   - Open Gesture: Increases volume (Distance > 50).

# Requirements
Install the necessary libraries via terminal:
```bash
pip install opencv-python mediapipe pyautogui
