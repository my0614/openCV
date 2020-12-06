import cv2

print(cv2.__version__)
src = cv2.imread("AVR_pinmap.png", cv2.IMREAD_COLOR)

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
