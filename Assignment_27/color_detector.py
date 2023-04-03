import cv2

cap = cv2.VideoCapture(0)
_ , frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]
writer = cv2.VideoWriter("cam.mp4" , cv2.VideoWriter_fourcc(*'mp4v') , 30 , (cols , rows))
while True:
    _ , frame = cap.read()
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    mask = cv2.rectangle(frame , (220 , 120) , (430, 330)  , 255 ,3)
    for i in range(125 , 325):
        for j in range(225,425):
            if frame[i ,j] <= 60 :
                cv2.putText(frame , "BLACK " , (250 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            if frame[i ,j] > 70 and frame[i ,j] <= 130 :
                cv2.putText(frame , "GRAY " , (50 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            if frame[i ,j] > 180 and frame[i ,j] <= 255 :
                cv2.putText(frame , "WHITE " , (450 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

    writer.write(frame)
    cv2.imshow("result" , frame)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

writer.release()