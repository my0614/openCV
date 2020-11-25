import numpy as np
import cv2
print(cv2.__version__)

src = cv2.imread("AVR_pinmap.png", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)
dst1 = cv2.flip(src,1)
dst2 = cv2.flip(dst1,0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
