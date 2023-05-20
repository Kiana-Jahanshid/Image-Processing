import cv2 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 50)

pic = cv2.imread('input/4.png',-1)
pic = cv2.resize(pic , (700 , 750))

while True :   
      
    cv2.imshow(" Background " , pic)   
    x , frame = cap.read()
    pic[ 220 :300 , 260:460] = frame [ 220 :300 , 260:460]

    if cv2.waitKey(25) & 0xFF == ord("b"):
        break