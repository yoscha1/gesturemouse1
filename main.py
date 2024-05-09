import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            index_landmark = landmarks[8]  # Index finger landmark
            thumb_landmark = landmarks[4]  # Thumb landmark

            index_x = int(index_landmark.x * frame_width)
            index_y = int(index_landmark.y * frame_height)

            thumb_x = int(thumb_landmark.x * frame_width)
            thumb_y = int(thumb_landmark.y * frame_height)

            # Draw circles on index finger and thumb
            cv2.circle(img=frame, center=(index_x, index_y), radius=10, color=(0, 255, 255))
            cv2.circle(img=frame, center=(thumb_x, thumb_y), radius=10, color=(0, 255, 255))

            # Calculate index and thumb coordinates for the screen
            index_screen_x = screen_width / frame_width * index_x
            index_screen_y = screen_height / frame_height * index_y

            thumb_screen_x = screen_width / frame_width * thumb_x
            thumb_screen_y = screen_height / frame_height * thumb_y

            # Move the mouse pointer
            pyautogui.moveTo(index_screen_x, index_screen_y)
            print('outside', abs(index_y - thumb_screen_y))
            if abs(index_y - thumb_y) < 20:
                pyautogui.click()
                pyautogui.sleep(1)
            # Optionally, you can perform actions based on thumb position as well

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
