import cv2

img = cv2.imread("TestImages/shops.jpg")

cv2.imshow("Origianl 1", img)

orb = cv2.ORB_create()

keypts, des = orb.dectectAndCompute(img, None)
print "number of keypoints found:", len(keypts)