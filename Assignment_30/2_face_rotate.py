import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def roi_manipulations(ROI):
    global cropped_roi
    roi_landmarks = []
    for i in ROI :
        roi_landmarks.append(pred[i])
    roi_landmarks = np.array(roi_landmarks , dtype = int )

    x , y , w , h =  cv2.boundingRect(roi_landmarks)

    cropped_roi = img[y-7:y+h+7 , x-10:x+w+10] 
    rotate_cropped_roi = cv2.rotate(cropped_roi ,rotateCode = cv2.ROTATE_180 )
    mirror_roi = cv2.flip(rotate_cropped_roi , flipCode= 1)
    img[y-7:y+h+7 , x-10:x+w+10] = mirror_roi

    return img 


img = cv2.imread("inputs/girl.jpg")
fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")
face_cascade = cv2.CascadeClassifier('OpenVtuber\haarcascade_frontalface_default.xml')

color = (0, 0, 255)
boxes, scores = fd.inference(img)


lips      = [52 , 64 , 63 , 71 , 67 , 68 , 61 , 58 , 59 , 53 , 56 , 55 ]
left_eye  = [39 , 37 , 33 , 36 , 35 , 41 , 40 , 42 ]
right_eye = [95 , 94 , 96 , 93 , 91 , 87 , 90 , 89 ]



for pred in fa.get_landmarks(img , boxes):

    lip       = roi_manipulations(lips)
    left_eye  = roi_manipulations(left_eye)
    right_eye = roi_manipulations(right_eye)


img = cv2.rotate(img ,rotateCode = cv2.ROTATE_180 ) 

cv2.imshow("result", img)
cv2.waitKey()
    