import cv2 
import numpy as np 
import matplotlib.pyplot as plt

def lion_edge_detection(img):
    rows , cols = img.shape
    res = np.zeros((rows , cols) ,dtype=np.uint8 )

    filter = np.array([[-1 , -1 , -1],
                       [-1 ,  8 , -1],
                       [-1 , -1 , -1]])

    for i in range(1 , rows-1 ):
        for j in range(1 , cols-1):
            small = img[i-1:i+2 , j-1:j+2]
            avg = np.sum(filter * small )
            res[i , j] = avg

    cv2.imwrite("outputs/lion.png" , res)


def spider_edge_detection(img):
    rows , cols = img.shape
    res = np.zeros((rows , cols) ,dtype=np.uint8 )

    horizontal_filter = np.array([[-1, 0, 1],
                           [-1, 0, 1],
                           [-1, 0, 1]])  
    
    vertical_filter = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]]) 
    
    for i in range(1 , rows-1 ):
        for j in range(1 , cols-1):
            small = img[i-1:i+2 , j-1:j+2]
            avg = np.sum(horizontal_filter * small )
            avg2 = np.sum(vertical_filter * small )
            mag = np.sqrt(pow(avg, 2.0) + pow(avg2, 2.0))  
            res[i , j] = mag

    cv2.imwrite("outputs/spider.png" , res )



img = cv2.imread("inputs/lion.png" , cv2.IMREAD_GRAYSCALE) 
lion_edges = lion_edge_detection(img)

img = cv2.imread("inputs/spider.png" , cv2.IMREAD_GRAYSCALE) 
spider_edges = spider_edge_detection(img)