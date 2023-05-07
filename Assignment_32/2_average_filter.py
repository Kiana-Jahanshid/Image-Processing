import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("inputs/1.jpg" , cv2.IMREAD_GRAYSCALE)
filter = np.ones((3,3)  , np.float32) * 5 # * 1 , 0.04 , 5
result = cv2.filter2D(img , -1 , filter  )


Direc = "outputs/magic"
files = os.listdir(Direc)
array=[]
list = []
for f in files :
    if os.path.isfile(Direc+'/'+f):
        array.append(f)
    x=cv2.imread(f"outputs/magic/{f}")
    list.append(x)


horizontal  = np.hstack((list[0] , list[1] , list[2] , list[3] , list[4] , list[5] , list[6]))
result = np.concatenate((list[0] , list[1] , list[2] , list[3] , list[4] , list[5] , list[6]), axis = 1)
cv2.imwrite("outputs/magic.jpg" , result )

cv2.imwrite("outputs/magic/original.jpg" , img)
cv2.imshow("" , result )
cv2.waitKey()
