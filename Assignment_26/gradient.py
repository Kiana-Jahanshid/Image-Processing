import cv2 
import numpy as np

array = np.arange(0, 65025, 1, np.uint8)
image = np.reshape(array, (255, 255))
print(array)
x = 0
for i in range (255):
    image[i , 0:255] = 255-x
    x+=1

cv2.imshow("Gradient" ,image)
cv2.imwrite('gradient.jpg', image)
cv2.waitKey()
