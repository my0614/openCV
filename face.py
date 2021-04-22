
import cv2
import numpy as np
import face_recognition

print(cv2.__version__)

face_a = face_recognition.load_image_file('다운로드.jpeg')
face_a = cv2.cvtColor(face_a, cv2.COLOR_BGR2RGB)

face_b = face_recognition.load_image_file('unnamed.jpeg')
face_b = cv2.cvtColor(face_b, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(face_a)[0]
enc = face_recognition.face_encodings(face_a)[0]
cv2.rectangle(face_a, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

cv2.imshow('face_a', face_a)
cv2.imshow('face_b', face_b)
cv2.waitKey(0)
