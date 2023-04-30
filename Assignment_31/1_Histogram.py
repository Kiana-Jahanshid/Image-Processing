import cv2 
import matplotlib.pyplot as plt 
import numpy as np 


image  = cv2.imread("inputs/Fruit.jpg" , cv2.IMREAD_GRAYSCALE)
rows , cols = image.shape
print(image.shape)

def histogram_calculation(image) :
    histogram = np.zeros(256)
    for i in range(rows):
        for j in range(cols):
            value = image[i , j]
            histogram[value] += 1 
    return histogram

#1️⃣
histogram = histogram_calculation(image)
plt.plot(histogram)

#2️⃣
y = np.arange(256)
#plt.bar( y ,  histogram )

#3️⃣
#plt.hist( image.ravel() , 256)

plt.show()
