import cv2
import numpy as np


def nothing(x):
    pass

cv2.namedWindow("Color Picker")
cv2.createTrackbar("Hue", "Color Picker", 0, 170, nothing)
cv2.createTrackbar("Saturation", "Color Picker", 255, 255, nothing)
cv2.createTrackbar("Value", "Color Picker", 255, 255, nothing)

img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos("Hue", "Color Picker")
    s = cv2.getTrackbarPos("Saturation", "Color Picker")
    v = cv2.getTrackbarPos("Value", "Color Picker")

    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("Color Picker", img_bgr)

    keypress = cv2.waitKey(1)
    if keypress & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()