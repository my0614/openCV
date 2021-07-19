  import cv2

VIDEO_FILE_PATH = './0719_test.mp4'
cap = cv2.VideoCapture(VIDEO_FILE_PATH)


#isOpen을 사용하여 파일 열기 확인
if cap.isOpened() == False:
    print ('Can\'t open the video (%d)' % (VIDEO_FILE_PATH))
    exit()

titles = ['orig']
#윈도우 생성 및 사이즈 변경'
print(titles[0])
for t in titles:
    cv2.namedWindow(t)
    
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#재생할 파일의 프레임 레이트 얻기
fps = cap.get(cv2.CAP_PROP_FPS)


fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#저장할 파일 이름
filename = '0719_result.avi'

out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))

#얼굴 인식용
face_cascade = cv2.CascadeClassifier()
face_cascade.load('./opencv-master/data/haarcascades/haarcascade_frontalface_default.xml') #opencv의 haarcascade xml로 load


while(True):
    #파일로 부터 이미지 얻기
    ret, frame = cap.read()
    #더 이상 이미지가 없으면 종료
    #재생 다 됨
    if frame is None:
        break;

    #얼굴인식 영상 처리
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur =  cv2.GaussianBlur(grayframe,(5,5), 0)
    faces = face_cascade.detectMultiScale(blur, 1.8, 2, 0, (50, 50))

    #원본 이미지에 얼굴 인식된 부분 표시
    for (x,y,w,h) in faces:
        cx = int(x+(w/2))
        cy = int(y+(h/2))
        cr = int(w/2)
        cv2.circle(frame,(cx,cy),cr,(255,0,0),3)

    # 얼굴 인식된 이미지 화면 표시
    cv2.imshow(titles[0],frame)

    # 인식된 이미지 파일로 저장
    out.write(frame)

    #1ms 동안 키입력 대기
    if cv2.waitKey(1) == 27:
        break;


#재생 파일 종료
cap.release()
#저장 파일 종료
out.release()
#윈도우 종료
cv2.destroyAllWindows()
