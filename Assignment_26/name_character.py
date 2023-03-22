import cv2
import numpy as np 

bg = np.ones((500 , 500))
x = 0 
for i in range(6) :
    bg[107+x:154+x , 135:185] = 0
    x+= 43
y=0
bg[210:270 , 170:220] = 0
for i in range(2):
    bg[160-y:210-y , 220+y:270+y] = 0
    y+=50
j =0
for i in range(2):
    bg[270+j:320+j , 220+j:270+j] = 0
    j+=50

cv2.imshow("name character" , bg)
cv2.waitKey()