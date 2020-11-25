import numpy as np
import cv2
print(cv2.__version__)

src = cv2.imread("AVR_pinmap.png", cv2.IMREAD_COLOR)
height, width , channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 180,1)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
