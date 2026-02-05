import cv2
import numpy as np

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture one pair for stitching
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()

if not ret1 or not ret2:
    print("Initial camera read failed")
    exit()

frame1 = cv2.resize(frame1, (640, 480))
frame2 = cv2.resize(frame2, (640, 480))

stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, stitched = stitcher.stitch([frame1, frame2])

if status != cv2.Stitcher_OK:
    print("Initial stitching failed — check overlap")
    exit()

print("Initial stitching SUCCESS")

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    frame1 = cv2.resize(frame1, (640, 480))
    frame2 = cv2.resize(frame2, (640, 480))

    cv2.imshow("Stitched (static)", stitched)
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
