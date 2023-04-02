import cv2 

image = cv2.imread("bat.jpg")
initial_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
threshold = 140
_ , output =cv2.threshold(initial_image , threshold , 255 , cv2.THRESH_BINARY_INV)
output[303:315 , 488:505] = 255
cv2.putText(output , "BATMAN" , (355 , 505) , cv2.FONT_HERSHEY_COMPLEX , 2.2 , 255 , 2)

cv2.imshow("BATMAN OUTPUT" , output)
cv2.waitKey()