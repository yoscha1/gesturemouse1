import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frame from video capture.")
        continue

    img = detector.findHands(img)

    if img is None:
        print("No image data received from HandDetector.")
        continue

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
