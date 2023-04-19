import numpy as np
import cv2
import tensorflow as tf
from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def roi_resize(face_roi):

    roi_landmarks = []
    for i in face_roi :
        roi_landmarks.append(pred[i])
    roi_landmarks = np.array(roi_landmarks , dtype = int )
    print(roi_landmarks) 

    x , y , w , h =  cv2.boundingRect(roi_landmarks)
    mask =  np.zeros(img.shape , dtype=np.uint8)
    cv2.drawContours(mask , [roi_landmarks] , -1 , (255,255,255) , -1) 
    mask = mask // 255 

    result  = img * mask 
    croped_lip_result = result[y:y+h , x:x+w]
    big_roi = cv2.resize(croped_lip_result , (0,0) , fx=2 , fy=2)

    return big_roi



def put_resized_rois_on_face(img , lips , left_eye , right_eye):
    faces=face_cascade.detectMultiScale(img, 1.2, 5, 0, (120, 120), (350, 350))
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            min_y_big_eye_left = int(y + 2.7 * h / 8)
            max_y_big_eye_left = int(y + 6.3 * h / 12)
            big_eye_left_height = max_y_big_eye_left - min_y_big_eye_left

            min_y_big_eye_right = int(y + 2.5 * h / 8)
            max_y_big_eye_right = int(y + 6 * h / 12)
            big_eye_right_height = max_y_big_eye_right - min_y_big_eye_right 

            min_y_lip = int(y + 2 * h / 5 + 100)
            max_y_lip = int(y + 6 * h / 5 - 49)
            lip_height = max_y_lip - min_y_lip

            big_eye_left_region  = img[min_y_big_eye_left  : max_y_big_eye_left  , x+9 : x+(w//2)-16]
            big_eye_right_region = img[min_y_big_eye_right : max_y_big_eye_right , x+(w//2)+13  : x+w+20 ]            
            lips_region = img[min_y_lip : max_y_lip  ,  x+45 : x+w+15 ]

            big_eye_left  = cv2.resize( left_eye  , (w-150, big_eye_left_height)  , interpolation=cv2.INTER_CUBIC)
            big_eye_right = cv2.resize( right_eye , (w-165, big_eye_right_height) , interpolation=cv2.INTER_CUBIC)
            big_lips = cv2.resize(lips, (w-60, lip_height),interpolation=cv2.INTER_CUBIC)
            
            transparentOverlay(big_eye_left_region , big_eye_left)
            transparentOverlay(big_eye_right_region , big_eye_right)
            transparentOverlay(lips_region , big_lips)

    return img


def transparentOverlay(src, overlay, pos=(0, 0), scale=1):#
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  
    rows, cols, _ = src.shape  
    y, x = pos[0], pos[1]  
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j] 
    return src




fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")
face_cascade = cv2.CascadeClassifier('OpenVtuber\haarcascade_frontalface_default.xml')


img = cv2.imread("inputs/el2.jpg")
boxes, scores = fd.inference(img)


lips      = [52 , 64 , 63 , 71 , 67 , 68 , 61 , 58 , 59 , 53 , 56 , 55 ]
left_eye  = [39 , 37 , 33 , 36 , 35 , 41 , 40 , 42 ]
right_eye = [95 , 94 , 96 , 93 , 91 , 87 , 90 , 89 ]



for pred in fa.get_landmarks(img , boxes):

    resized_lips      = roi_resize(lips)
    resized_left_eye  = roi_resize(left_eye)
    resized_right_eye = roi_resize(right_eye)

    cv2.imwrite("resized_lips.jpg" , resized_lips)
    cv2.imwrite("resized_left_eye.jpg"  , resized_left_eye )
    cv2.imwrite("resized_right_eye.jpg" , resized_right_eye)


    lips = cv2.imread("resized_lips.png" , cv2.IMREAD_UNCHANGED)
    left_eye = cv2.imread("resized_left_eye.png" , cv2.IMREAD_UNCHANGED)
    right_eye = cv2.imread("resized_right_eye.png" , cv2.IMREAD_UNCHANGED)
    


final_result = put_resized_rois_on_face(img , lips , left_eye , right_eye )


cv2.imshow("result", final_result )
cv2.waitKey()
    
