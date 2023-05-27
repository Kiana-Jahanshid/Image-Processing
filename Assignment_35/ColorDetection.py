import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
_ , frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80) , 'purple':(72, 50, 72 )} 
upper = {'red':(186,255,255) , 'green':(86,255,255)  , 'blue':(117,255,255) , 'yellow':(54,255,255) , 'orange':(20,255,255), 'purple':(224,176,255)}
colors= {'red':(0,0,255)     , 'green':(0,255,0)     , 'blue':(255,0,0)     , 'yellow':(0, 255, 217), 'orange':(0,140,255) , 'purple':(128, 0, 128)}



black =[]
white=[]
for i in range(20):
    black.append(i)

for i in range(200 , 256):
    white.append(i)

while True:
    _ , frame = cap.read()
    mask = cv2.rectangle(frame , (230 , 110) , (450, 310)  , 255 ,3)
    
    b = mask[:, :, :1]
    g = mask[:, :, 1:2]
    r = mask[:, :, 2:]

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)


    for i in range(rows):
        for j in range(cols):   


            if (g_mean > r_mean and g_mean > b_mean):
                cv2.putText(frame , "GREEN " , (50 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            elif (r_mean > b_mean and r_mean > g_mean):
                cv2.putText(frame , "RED "   , (250 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            elif (b_mean > g_mean and b_mean > r_mean):
                cv2.putText(frame , "BLUE "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif  mask[i,j].all() in black :
                cv2.putText(frame , "black " , (50 , 70) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
                
            elif mask[i,j].all() in white:
                cv2.putText(frame , "white " , (50 , 130), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3) 

            elif (mask[i,j][0] >= lower["yellow"][0]  and mask[i,j][1] >= lower["yellow"][1] and mask[i,j][2] >= lower["yellow"][2] ) \
            or (mask[i,j][0] <= upper["yellow"][0]  and mask[i,j][1] <= upper["yellow"][1] and mask[i,j][2] <= upper["yellow"][2] ):
                cv2.putText(frame , "yellow " , (50 , 190) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)             
                
            elif (mask[i,j][0] >= lower["purple"][0]  and mask[i,j][1] >= lower["purple"][1] and mask[i,j][2] >= lower["purple"][2] ) \
            or (mask[i,j][0] <= upper["purple"][0]  and mask[i,j][1] <= upper["purple"][1] and mask[i,j][2] < upper["purple"][2] ):
                cv2.putText(frame , "purple " , (50 , 170) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (mask[i,j][0] >= lower["orange"][0]  and mask[i,j][1] >= lower["orange"][1] and mask[i,j][2] >= lower["orange"][2] ) \
            or (mask[i,j][0] <= upper["orange"][0]  and mask[i,j][1] <= upper["orange"][1] and mask[i,j][2] <= upper["orange"][2] ):
                cv2.putText(frame , "orange " , (50 , 190) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3) 
 


    cv2.imshow("result" , frame)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

