import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

img = cv2.imread("inputs/zeb.jpg" , cv2.IMREAD_GRAYSCALE)

edge_detection_kernel = np.array([[-1 , -1 , -1],
                                  [-1 ,  8 , -1],
                                  [-1 , -1 , -1]])

identity_kernel = np.array([[0  ,  0 ,  0],
                            [0  ,  1 ,  0],
                            [0  ,  0 ,  0]])

Sharpening_kernel = np.array([[0  , -1 ,  0],
                              [-1 ,  5 , -1],
                              [0  , -1 ,  0]])

emboss_kernel = np.array([[-2 , -1 ,  0],
                          [-1 ,  1 ,  1],
                          [ 0 ,  1 ,  2]])

my_kernel1 = np.array([[ 1 ,  2 ,  1],
                       [ 0 ,  0 ,  0],
                       [-1 , -2 , -1]])


result = cv2.filter2D(img  ,-1, my_kernel1 )
cv2.imwrite("outputs/horizontal_edges.jpg" , result)
cv2.imshow("", result)
cv2.waitKey()
