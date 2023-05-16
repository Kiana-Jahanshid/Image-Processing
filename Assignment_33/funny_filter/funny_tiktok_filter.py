import cv2 
import numpy as np 
import keyboard 


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 50)
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") 

pic = cv2.imread('input/3.png',-1)
pic = cv2.resize(pic , (700 , 870))


while True :   

    cv2.imshow("" , pic)   
    x , frame = cap.read()
    faces = face_detector.detectMultiScale(frame)    
    for face in faces :
        x , y , w , h  = face
        pic[y+10:y+int((h/2))+10 , x+30:x+int(w)-50] = frame[y+10:y+int((h/2))+10 , x+30:x+int(w)-50] 

    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

