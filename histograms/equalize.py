import numpy as np
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq])) # np.htsack() is used to stack (combine) images horizontally
cv2.waitKey(0)

# python equalize.py --image ../dinosarus.png