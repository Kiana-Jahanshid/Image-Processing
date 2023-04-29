import cv2 
import numpy as np 

img = cv2.imread("inputs/rose.jpg" , cv2.IMREAD_GRAYSCALE) 
rows , cols = img.shape
res = np.zeros((rows , cols) ,dtype=np.uint8 )

filter = np.ones((31,31)) / 961 

for i in range(15 , rows-15 ):
    for j in range(15 , cols-15):
        small = img[i-15:i+16 , j-15:j+16]    
        if img[i,j] <180 :              
            avg = np.sum(filter * small )
            res[i , j] = avg
        else :
            res[i,j] =img[i,j]

res = cv2.resize(res , [470,500])
cv2.imwrite("outputs/rose.png" , res)
cv2.imshow("" , res )
cv2.waitKey()

