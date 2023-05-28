import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
_ , frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

lower = {'red':(166, 84, 141), 'green':(66, 122, 129), 'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80) , 'purple':(72, 50, 72 ) , 'white':(180, 180, 180), 'black':(0, 0, 0)} 
upper = {'red':(186,255,255) , 'green':(86,255,255)  , 'blue':(117,255,255) , 'yellow':(54,255,255) , 'orange':(20,255,255), 'purple':(224,176,255) , 'white':(255, 255, 255), 'black':(30, 30, 30)}
colors= {'red':(0,0,255)     , 'green':(0,255,0)     , 'blue':(255,0,0)     , 'yellow':(0, 255, 217), 'orange':(0,140,255) , 'purple':(128, 0, 128) , 'white':(255, 255, 255), 'black':(0, 0, 0)}

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
    
    w_mean = np.mean(r+g+b)
    y_mean = np.mean(g+r)
    p_mean = np.mean(r+b)
    o_mean = np.mean(r+y_mean)


    for i in range(rows):
        for j in range(cols): 

            if  (g_mean > r_mean and g_mean > b_mean and g_mean > y_mean and g_mean > p_mean  ):
                cv2.putText(frame , "GREEN " , (50 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (r_mean > b_mean and r_mean > g_mean and r_mean > y_mean and r_mean > p_mean ):
                cv2.putText(frame , "RED "   , (250 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (b_mean > g_mean and b_mean > r_mean  and b_mean > y_mean and b_mean > p_mean ):
                cv2.putText(frame , "BLUE "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (p_mean > g_mean and p_mean > r_mean and p_mean > b_mean and p_mean > y_mean ):
                cv2.putText(frame , "purple "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (y_mean > g_mean and y_mean > r_mean and y_mean > b_mean and y_mean > p_mean ):
                cv2.putText(frame , "yellow "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            elif (o_mean > g_mean and o_mean > r_mean and o_mean > b_mean and o_mean > p_mean  ):
                cv2.putText(frame , "orange "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            # elif (w_mean > g_mean and w_mean > r_mean and w_mean > b_mean ):
            #      cv2.putText(frame , "white "  , (450 , 90), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3) 
                
            # elif (mask[i,j][0] >= lower["white"][0]  and mask[i,j][1] >= lower["white"][1] and mask[i,j][2] >= lower["white"][2] ) \
            #   or (mask[i,j][0] <= upper["white"][0]  and mask[i,j][1] <= upper["white"][1] and mask[i,j][2] <= upper["white"][2] ):
            #     cv2.putText(frame , "white " , (50 , 170) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

            # elif (mask[i,j][0] >= lower["black"][0]  and mask[i,j][1] >= lower["black"][1] and mask[i,j][2] >= lower["black"][2] ) \
            #   or (mask[i,j][0] <= upper["black"][0]  and mask[i,j][1] <= upper["black"][1] and mask[i,j][2] <= upper["black"][2] ):
            #     cv2.putText(frame , "black " , (50 , 170) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)


            elif  mask[i,j].all() in black :
                cv2.putText(frame , "black " , (50 , 70) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
                
            elif mask[i,j].all() in white:
                cv2.putText(frame , "white " , (50 , 130), cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
                

    cv2.imshow("result" , frame)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

