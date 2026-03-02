import cv2
import mediapipe as mp
import pyautogui
from mediapipe.tasks.python.vision import drawing_utils

webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _ , image = webcam.read()
    cv2.imshow("Hand volume control using python", image)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()