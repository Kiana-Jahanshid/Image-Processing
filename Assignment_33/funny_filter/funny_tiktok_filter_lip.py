import cv2 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 50)

pic = cv2.imread('input/5.png',-1)
pic = cv2.resize(pic , (700 , 750))

while True :   
      
    cv2.imshow(" Background " , pic)   
    x , frame = cap.read()
    pic[ 360 :460 , 300:400] = frame [ 200 :300 , 200:300]

    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

