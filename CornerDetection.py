import cv2
import numpy

img1 = cv2.imread("TestImages/Puzzle1.jpg")
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg = cv2.GaussianBlur(grayImg, (17, 17), -1)
goodFeats = cv2.goodFeaturesToTrack(grayImg, 350, 0.08, 15)

print goodFeats[0]

print goodFeats[0, 0]

print goodFeats[0, 0, 0], goodFeats[0, 0, 1]

for locations in goodFeats:
    for coords in locations:
        cv2.circle(img1, (coords[0], coords[1]), 5, (0, 255, 0))

cv2.imshow("Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()