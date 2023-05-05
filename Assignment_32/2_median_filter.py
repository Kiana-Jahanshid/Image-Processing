import cv2 
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("inputs/board.tif" , cv2.IMREAD_GRAYSCALE )

x = img
for i in range(5) :
    x = cv2.medianBlur(x , 3 )

horizontal = np.hstack((img , x))
final_concat = np.concatenate((img , x), axis=1)
cv2.imwrite("outputs/board_MEDIAN_filter.jpg" ,final_concat )
cv2.imshow('MEDIAN filter', final_concat)
cv2.waitKey()

