import cv2 
import numpy as np

floor = cv2.imread("floor.jpg") 
floor  = cv2.resize(floor , [650 ,500])
room = cv2.imread("room.jpg") 
room  = cv2.resize(room , [650 ,500])
room_mask1 = cv2.imread("room_mask.jpg") 
room_mask1  = cv2.resize(room_mask1 , [650 ,500])

room_mask = 255 - room_mask1
masking = cv2.add(room_mask , floor )
masking  = cv2.resize(masking , [650 ,500])

furniture = cv2.add(room_mask1 , room)
furniture  = cv2.resize(furniture , [650 ,500])
x=255
for i in range(256):
    masking[np.where((masking==[x,x,x]).all(axis=2))] = [0,0,0]
    x-= 1

result = furniture + masking
cv2.imshow("" , result)
cv2.imwrite("final_floor.jpg" , masking)
cv2.imwrite("final_furniture.jpg" , furniture)
cv2.imwrite("final_decoration.jpg" , result)
cv2.waitKey()
