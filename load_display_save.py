import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-w", "--write", required=False, help="Path to the write image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

cv2.imshow("Image", image)
cv2.waitKey(0)

if args["write"]:
    cv2.imwrite(args["write"], image)
    print("Image written to disk")

# python load_display_save.py -i dinosarus.png -w copy.png