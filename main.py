import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:RFEPQL@192.168.1.18')

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    print(frame.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        
        break

cap.release()
cv2.destroyAllWindows()