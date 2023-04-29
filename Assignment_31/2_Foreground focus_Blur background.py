import cv2 
import numpy as np 

import matplotlib.pyplot as plt

img = cv2.imread("inputs/rose.jpg" , cv2.IMREAD_GRAYSCALE) # yek array az jens numpy hast 
rows , cols = img.shape

# averaging 
#pixel haye kenari tasviro dar miangin giri hesab nemikonim 
res = np.zeros((rows , cols) ,dtype=np.uint8 )
# stride 1 hast yani yek pixel yek pixel mirim jelo 

#filter = np.array([[1/9 , 1/9 , 1/9],
#                   [1/9 , 1/9 , 1/9],
#                   [1/9 , 1/9 , 1/9]])
# filter = np.ones((3,3)) / 9 
#yani yek array 3 dar 3 ke tamoome khone hash on
#
filter = np.ones((5,5)) / 25 


# np.average rooye array 1 bodi kar mikone 
for a in range( rows):
    for b in range(cols):

        if img[a,b].all() <200 :
            for i in range(2 , rows-2 ):
                for j in range(2 , cols-2):
                    small = img[i-2:i+3 , j-2:j+3]                  
                    avg = np.sum(filter * small )
                    res[i , j] = avg

#cv2.imwrite("res_filter5dar5.png" , res)
cv2.imshow("" , res )
cv2.waitKey()



"""""""""""""""
dar 5*5 vozooh kam shode , vali nise kamtar kam shode 
"""""""""""""""