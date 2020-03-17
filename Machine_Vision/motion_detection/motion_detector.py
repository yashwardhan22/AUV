import numpy as np
import cv2
import imutils
import time

cap = cv2.VideoCapture(0)
firstFrame = None

while(True):
    ret, frame = cap.read()
    text = "No Movement"
    
    gray   = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur   = cv2.GaussianBlur(gray , (27, 27), 0)
    if firstFrame is None:
        firstFrame = gray
        continue
        
#--------------------------------------------------
    now = time.localtime(time.time())
    if now[5]%8 == 0:
        firstFrame = gray
        continue 
#--------------------------------------------------


    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 40, 250, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=3)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for c in cnts:
        if cv2.contourArea(c) < 2500:
            continue     
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Movement Detected"


    if text == "Movement Detected":
        txt_color = (0, 0, 255)
    else:
        txt_color = (255, 0, 0)
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, txt_color, 2)
    
    if(ret):
        cv2.imshow('Cam',frame)
        #cv2.imshow('Gray',gray)
        #cv2.imshow('Blur',blur)
        #cv2.imshow("Frame Delta", frameDelta)
        #cv2.imshow('Thresh',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
          
cap.release()
cv2.destroyAllWindows()
