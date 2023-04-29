import cv2 
import numpy as np 
import matplotlib.pyplot as plt


def calc(filter):
    for i in range(1 , rows-1 ):
        for j in range(1 , cols-1):
            small = img[i-1:i+2 , j-1:j+2]
            avg = np.abs(np.sum(filter * small ))
            res[i , j] = avg
    return res


img = cv2.imread("inputs/building.jpg" , cv2.IMREAD_GRAYSCALE) 
rows , cols = img.shape
res = np.zeros((rows , cols) ,dtype=np.uint8 )


filter_horizontal_edge_det = np.array([[-1 , -1 , -1],
                                       [ 0 ,  0 ,  0],
                                       [ 1 ,  1 ,  1]])

filter_vertical_edge_det = np.array([[2 , 0 , -2],
                                     [2 , 0 , -2],
                                     [2 , 0 , -2]])


vertical   = calc(filter_vertical_edge_det  )
cv2.imwrite("outputs/4_vertical_res.png" , vertical)

horizontal = calc(filter_horizontal_edge_det)
cv2.imwrite("outputs/4_horizontal_res.png" , horizontal)
