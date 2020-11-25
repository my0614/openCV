import numpy as np
import cv2
print(cv2.__version__)

capture = cv2.VideoCapture(0) # 카메라장치번호
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 높이

while 1:
    ret, frame = capture.read() # 카메라 상태 받아옴
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0: break # 임의키 누를때 종료
capture.release() # 메모리해제
cv2.destoryAllWindows() # 윈도우 창 닫기