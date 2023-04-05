import cv2 
import numpy as np 

image = cv2.imread("cats.jpeg")
face_detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml") 
img = cv2.resize(image , [700 , 450])
faces = face_detector.detectMultiScale(img)
count = 0
for face in faces :
    x , y , w , h  = face 
    cv2.rectangle(img , [x, y] , [x+w , y+h]  , [0,0,150] , 2)
    count+=1
cv2.putText(img , f"NUMBER OF FACES : {count}" , (30 , 30) , cv2.FONT_HERSHEY_DUPLEX , 0.5 , (0,0,150) , 1)

print(f"NUMBER OF DETECTED CAT'S FACE : {count}" )
cv2.imshow("CAT'S FACE DETECTION" , img)
cv2.waitKey()