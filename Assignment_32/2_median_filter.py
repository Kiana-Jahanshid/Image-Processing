import cv2 
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("inputs/xray.jpg" , cv2.IMREAD_GRAYSCALE )

x = img
for i in range(4) :
    x = cv2.medianBlur(x , 3 )
x = cv2.medianBlur(x , 9 )

horizontal = np.hstack((img , x))
final_concat = np.concatenate((img , x), axis=1)

cv2.imwrite("outputs/xray_MEDIAN_filter.jpg" ,final_concat )
cv2.imshow('MEDIAN filter', final_concat)
cv2.waitKey()

