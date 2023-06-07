import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:

    _ , frame = cap.read()
    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    rect = cv2.rectangle(frame , (230 , 110) , (450, 310)  , 255 ,3)
 
    height, width, _ = frame.shape
    x = int(width / 2)
    y = int(height / 2)

    center = hsv_frame[y, x]
    hue_value = center[0]

    if 0< hue_value < 5 or 170 <= hue_value <= 180:
        color = "RED"
    elif 15 <= hue_value <= 20:
        color = "ORANGE"
    elif 25<= hue_value <= 33:
        color = "YELLOW"
    elif 40 <= hue_value <= 78:
        color = "GREEN"
    elif 85<= hue_value <= 131:
        color = "BLUE"
    elif 133 <= hue_value <= 170:
        color = "PURPLE"
    else:
        color = "Unknown"



    cv2.putText(frame, color, (x - 200, 100), 0, 2, 0, 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("b"):
        break

