import numpy as np
import cv2

origIm = cv2.imread('TestImages/Coins1.jpg')
imHSV = cv2.cvtColor(origIm, cv2.COLOR_BGR2HSV)

lower_green = np.array([50, 50, 50])
upper_green = np.array([90, 255, 255])

mask1 = cv2.inRange(imHSV, lower_green, upper_green)

res = cv2.bitwise_and(origIm, origIm, mask=mask1)

maskGray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(maskGray, cv2.HOUGH_GRADIENT, 1, 20, param1=90, param2=35, minRadius=0, maxRadius=350)

if circles is not None:
    for circleSet in circles:
        for circle in circleSet:
            cv2.circle(origIm, (circle[0], circle[1]), circle[2], (0, 255, 0))

cv2.imshow("Image", origIm)
cv2.waitKey(0)
cv2.destroyAllWindows()
