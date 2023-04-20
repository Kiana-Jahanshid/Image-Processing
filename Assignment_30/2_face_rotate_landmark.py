import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


counter  = 0 
def roi_manipulations(ROI):
    
    global cropped_roi ,cropped_mirror_roi , lip_region , r_eye_region , l_eye_region , counter
    roi_landmarks = []
    for i in ROI :
        roi_landmarks.append(pred[i])
    roi_landmarks = np.array(roi_landmarks , dtype = int )

    x , y , w , h =  cv2.boundingRect(roi_landmarks)
    mask =  np.zeros(img.shape , dtype=np.uint8)
    cv2.drawContours(mask , [roi_landmarks] , -1 , (255,255,255) , -1) 
    mask = mask // 255

    result  = img * mask 
    cropped_roi = result[y-5:y+h+5 , x-7:x+w+7] 
    rotate_cropped_roi = cv2.rotate(cropped_roi ,rotateCode = cv2.ROTATE_180 )
    cropped_mirror_roi = cv2.flip(rotate_cropped_roi , flipCode= 1)
    cropped_mirror_roi = cv2.resize(cropped_mirror_roi , (0,0) , fx=1 , fy=1 )

    if counter == 0 :
        lip_region = img[y-12:y+h+25 , x-15:x+w+15]
        counter += 1 
    elif counter == 1 :
        r_eye_region = img[y-13:y+h+13 , x-15:x+w+15]
        counter += 1
    elif counter == 2 :
        l_eye_region = img[y-13:y+h+13 , x-15:x+w+15]
      
    return cropped_mirror_roi 



def put_resized_rois_on_face(img , lips_tr ,  left_eye_tr , right_eye_tr ):

    x = lips_tr.shape[0]
    y = lips_tr.shape[1]
    x = int(x/2)
    y = int(x/1.7)
    lips_tr = cv2.resize(lips_tr , [x ,y])

    x = left_eye_tr.shape[0]
    y = left_eye_tr.shape[1]
    x = int(x/2)
    y = int(x/2)
    left_eye_tr = cv2.resize(left_eye_tr , [x ,y])

    x = right_eye_tr.shape[0]
    y = right_eye_tr.shape[1]
    x = int(x/2)
    y = int(x/2)
    right_eye_tr = cv2.resize(right_eye_tr , [x ,y])
 
    transparentOverlay(lip_region  , lips_tr)
    transparentOverlay(r_eye_region , left_eye_tr)
    transparentOverlay(l_eye_region  , right_eye_tr)

    return img


def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
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


img = cv2.imread("inputs/girl2.jpeg")
img = cv2.resize(img  , [800 , 800])
fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")
face_cascade = cv2.CascadeClassifier('OpenVtuber\haarcascade_frontalface_default.xml')

boxes, scores = fd.inference(img)


lips      = [52 , 64 , 63 , 71 , 67 , 68 , 61 , 58 , 59 , 53 , 56 , 55 ]
left_eye  = [39 , 37 , 33 , 36 , 35 , 41 , 40 , 42 ]
right_eye = [95 , 94 , 96 , 93 , 91 , 87 , 90 , 89 ]


for pred in fa.get_landmarks(img , boxes):

    lips = roi_manipulations(lips)
    lips_tr = cv2.imread("lips2.png" , cv2.IMREAD_UNCHANGED)

    left_eye   = roi_manipulations(left_eye)
    left_eye_tr = cv2.imread("left_eye2.png" , cv2.IMREAD_UNCHANGED)
    
    right_eye  = roi_manipulations(right_eye)
    right_eye_tr = cv2.imread("right_eye2.png" , cv2.IMREAD_UNCHANGED)



final_result = put_resized_rois_on_face(img , lips_tr ,  left_eye_tr , right_eye_tr)
final_result = cv2.rotate(img ,rotateCode = cv2.ROTATE_180 ) 
print(final_result.shape)
final_result = cv2.resize(final_result , [600 ,600] ) 


cv2.imshow("result", final_result)
cv2.waitKey()
    