import cv2 
import matplotlib.pyplot as plt 
import numpy as np 


image  = cv2.imread("inputs/Fruit.jpg" , cv2.IMREAD_GRAYSCALE)
rows , cols = image.shape
print(image.shape)


histogram = np.zeros(256)
for i in range(rows):
    for j in range(cols):

        value = image[i , j]
        histogram[value] += 1 
#plt.plot(histogram)





values = []
count = []
for i in range(len(histogram)):
    values.append(i)
    count.append(histogram[i])
y = np.arange(len(values))
#plt.bar( y ,  count )



h = np.zeros(256)
for i in range(rows):
    for j in range(cols):

        v = image[i , j]
        h[v] += 1 



plt.hist( value  , y   , range=(0,256))
plt.show()

# image=cv2.resize(image, (600 , 800))
# cv2.imshow("",histogram)
# cv2.waitKey()

