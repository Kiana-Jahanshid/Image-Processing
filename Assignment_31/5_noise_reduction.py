import cv2 
import numpy as np 
import matplotlib.pyplot as plt


def mean_filter(x , y):
    for i in range(x , rows-x ):
        for j in range(x , cols-x):
            small = img[i-x:i+y , j-x:j+y]
            avg = np.mean(small)
            res[i , j] = avg
    return res


img = cv2.imread("inputs/circle.jpg" , cv2.IMREAD_GRAYSCALE) 
rows , cols = img.shape
res = np.zeros((rows , cols) , dtype=np.uint8 )

#filter3x3 = mean_filter(1 , 2)
#filter5x5 = mean_filter(2 , 3)
filter15x15 = mean_filter(7 , 8)

#cv2.imwrite("outputs/noise_reduction_filter3x3_square.png" , filter3x3)
#cv2.imwrite("outputs/noise_reduction_filter5x5_square.png" , filter5x5)
cv2.imwrite("outputs/noise_reduction_filter15x15_square.png" , filter15x15)