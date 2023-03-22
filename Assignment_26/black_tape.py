import cv2 

image = cv2.imread("prz.jpg")
res_img = cv2.resize(image ,[700 , 400])
grimg =cv2.cvtColor(res_img , cv2.COLOR_BGR2GRAY)
x = 0
for i in range(190):
    grimg[115-x:190-x , 0+x:1+x] = 0
    if x >= 115 :
        grimg[0:190-x , 0+x:1+x] = 0
    x+= 1
    
cv2.imshow("black tape ",grimg)
cv2.imwrite("black_tape.jpg" , grimg)
cv2.waitKey()