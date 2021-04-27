import cv2
import numpy as np

img = cv2.imread('girl.png', 1)

while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 70, 70])
    upper_green = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(img, img, mask=mask)
    fg = cv2.bitwise_and(img, img, mask=mask_inv)

    cv2.imshow("fg", fg)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
