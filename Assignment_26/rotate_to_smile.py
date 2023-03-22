import cv2

sad = cv2.imread("3.jpg")
img =cv2.resize(sad , [800 , 500])
img2 =cv2.resize(sad , [800 , 500])
cv2.imshow("original resized image" ,img)
cv2.waitKey()

for i in range(800):
    for j in range(500):
        img[499-j][799-i] = img[j][i] 
        img[j][i] = img[499-j][799-i]


cv2.imshow("happy_leftman",img) 
cv2.imwrite("happy_leftman.jpg", img)
cv2.waitKey()