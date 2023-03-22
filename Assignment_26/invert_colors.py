import cv2
import numpy as np 

image = cv2.imread("2.jpg" )
inverted_img = image
x = image.shape[0] 
y = image.shape[1]
print(image.shape)

for row in range(x) :
    for column in range(y):
            inverted_img[row][column] = 255 - inverted_img[row][column]

cv2.imshow("inverted 2" ,inverted_img)
cv2.imwrite("boy.jpg" , inverted_img)
cv2.waitKey()
