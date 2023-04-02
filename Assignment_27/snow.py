import cv2 
import numpy as np 

array = []
img = cv2.imread("sn.jpg")
img = cv2.resize(img, [680, 450])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = img.shape
for i in range(2000):
    speed = np.random.randint(1, 10)
    domain = np.random.randint(-4, 4)
    size = np.random.randint(1, 3)
    array.append([np.random.randint(0, cols), np.random.randint(0, rows), size, domain , speed])

while True :
    img = cv2.imread("sn.jpg")
    img = cv2.resize(img, [680, 450])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(2000):
        img[array[i][0] : array[i][0]+array[i][2]  ,  array[i][1] : array[i][1]+array[i][2]  ] = 255
        array[i][0] +=  array[i][4]
        array[i][1] +=  array[i][3]
        if array[i][0] > cols:
            array[i][0] = 0
    cv2.imshow("result" , img)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break
