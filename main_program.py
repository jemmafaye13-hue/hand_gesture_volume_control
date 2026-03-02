import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)
hands_detector = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

while True:
    success, image = webcam.read()
    if not success: break

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = hands_detector.process(rgb_image)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])

                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=10, color=(0, 255, 255))
                    x8, y8 = x, y

                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=10, color=(0, 255, 255))
                    x4, y4 = x, y

            dist = ((x8 - x4) ** 2 + (y8 - y4) ** 2) ** 0.5

            if dist > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

    cv2.imshow("Hand volume control", image)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

webcam.release()
cv2.destroyAllWindows()