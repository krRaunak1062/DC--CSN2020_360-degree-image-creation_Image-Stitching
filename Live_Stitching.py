import cv2
import numpy as np

# Open two cameras (change indices if needed)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

# Reduce resolution for speed
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create stitcher
stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("Camera feed error")
        break

    # Stitch frames
    status, stitched = stitcher.stitch([frame1, frame2])

    if status == cv2.Stitcher_OK:
        cv2.imshow("Live Stitched Feed", stitched)
    else:
        cv2.imshow("Camera 1", frame1)
        cv2.imshow("Camera 2", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
