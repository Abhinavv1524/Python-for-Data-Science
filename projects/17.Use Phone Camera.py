import cv2
import numpy as np

url = "http://192.168.29.123:4747/video"  # Replace with actual IP stream URL
cp = cv2.VideoCapture(url)

while True:
    ret, frame = cp.read()
    if ret:
        cv2.imshow("Frame", frame)
    else:
        print("Failed to retrieve frame. Check your IP address and camera connection.")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cp.release()
cv2.destroyAllWindows()
