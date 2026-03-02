import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)
hands_detector = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

thumb_x, thumb_y = 0, 0
index_x, index_y = 0, 0

while True:
    success, image = webcam.read()
    if not success: 
        break

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = hands_detector.process(rgb_image)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            for finger_id, landmark in enumerate(landmarks):
                height, width, _ = image.shape
                coord_x, coord_y = int(landmark.x * width), int(landmark.y * height)

                if finger_id == 8:
                    cv2.circle(image, (coord_x, coord_y), 10, (255, 0, 255), cv2.FILLED)
                    thumb_x, thumb_y = coord_x, coord_y

                if finger_id == 4:
                    cv2.circle(image, (coord_x, coord_y), 10, (0, 255, 255), cv2.FILLED)
                    index_x, index_y = coord_x, coord_y

            finger_distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5

            if finger_distance > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

    cv2.imshow("Hand volume control", image)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

webcam.release()
cv2.destroyAllWindows()
