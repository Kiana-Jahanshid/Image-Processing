import cv2 

img = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img2 = 255 - img2
result = img + img2

cv2.imshow("secret text" , result)
cv2.imwrite("secret_text.jpg" , result)
cv2.waitKey()