import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

(T, thresh) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
print(T)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

(T, threshinv) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
print(T)
cv2.imshow("Threshold Binary Inverse", threshinv)
cv2.waitKey(0)

cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=threshinv))
cv2.waitKey(0)

# python simple_thresholding.py --image ../dinosarus.png