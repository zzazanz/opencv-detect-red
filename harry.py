import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
 
if cap.isOpened():
    ret, _ = cap.read()
 
    while ret:
        ret, frame = cap.read()
        flip = cv2.flip(frame, 1)

        hsv = cv2.cvtColor(flip, cv2.COLOR_BGR2HSV)

        lower_red = np.array([60, 70, 70])
        upper_red = np.array([140, 70, 70])
        img_mask = cv2.inRange(hsv, lower_red, upper_red)

        kernel = np.ones((11,11), np.uint8)
        img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernel)
        img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel)

        img_result = cv2.bitwise_not(flip, flip, mask=img_mask)

        numOflabels, img_label, stats, centroids = cv2.connectedComponentsWithStats(img_mask)

        for idx, centroid, in enumerate(centroids):
            if stats[idx][0] == 0 and stats[idx][1] == 0:
                continue

            if np.any(np.isnan(centroid)):
                continue

        x, y, width, height, area = stats[idx]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area > 50:
            cv2.circle(flip, (centerX, centerY), 10, (0,0,255), 10)
            cv2.rectangle(flip, (x, y), (x+width, y+height), (0,0,255))

        cv2.imshow("camera", flip)
        
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()