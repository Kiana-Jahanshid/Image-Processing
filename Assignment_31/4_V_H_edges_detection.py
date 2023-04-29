import cv2 
import numpy as np 


def calc(filter_h , filter_v):
    for i in range(1 , rows-1 ):
        for j in range(1 , cols-1):
            small = img[i-1:i+2 , j-1:j+2]
            avg = np.abs(np.sum(filter_v * small ))
            avg2 = np.sum(filter_h * small )
            mag = np.sqrt(pow(avg, 2.0) + pow(avg2, 2.0))  
            res[i , j] = mag
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


edge_detection   = calc(filter_vertical_edge_det   , filter_horizontal_edge_det)
cv2.imwrite("outputs/4_both_edges_detection.png" , edge_detection)
