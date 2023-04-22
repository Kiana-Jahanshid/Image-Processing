import numpy as np
import cv2
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel
from PIL import Image
import math

def EuclideanDistance(source_representation, test_representation):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)
    return euclidean_distance



fd = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")

img = cv2.imread("inputs/mrbean.jpg") 
color = (0, 0, 255)
color2 = (125, 255, 125)
boxes, scores = fd.inference(img)

landmarks = [38 , 88 , 55 , 61  , 84 ]
#           [lefteye , righteye , ]


for pred in fa.get_landmarks(img , boxes):
    for index , p in enumerate(np.round(pred).astype(np.int)):
        ...
        #cv2.circle(img , tuple(p), 2, color, -1)
        #cv2.putText(img , str(index) , tuple(p) , cv2.FONT_HERSHEY_DUPLEX , 0.2 , (255 , 0 , 0))

for det in boxes.astype(np.int32):
    ...
    #cv2.rectangle(img, (det[0], det[1]),(det[2], det[3]), (2, 255, 0), 2)

roi_landmarks = []
for i in landmarks :
    roi_landmarks.append(pred[i])
roi_landmarks = np.array(roi_landmarks , dtype = int )
print(roi_landmarks) 



for i in range(len(landmarks)):
    print(f"point number {landmarks[i]}'s coordination is : "  , roi_landmarks[i])

lefteye = roi_landmarks[0]
righteye = roi_landmarks[1]
lefteye_x , lefteye_y  = lefteye
righteye_x , righteye_y  = righteye

if lefteye_y > righteye_y:
    point_3rd = (righteye_x, lefteye_y)
    direction = -1 
else:
    point_3rd = (lefteye_x, righteye_y)
    direction = 1 



a = EuclideanDistance(np.array(lefteye), np.array(point_3rd))
b = EuclideanDistance(np.array(righteye), np.array(point_3rd))
c = EuclideanDistance(np.array(righteye), np.array(lefteye))


if b != 0 and c != 0:
    cos_a = (b*b + c*c - a*a)/(2*b*c)
    angle = np.arccos(cos_a) 
    angle = (angle * 180) / math.pi #radian to degree

    if direction == -1:
        angle = 90 - angle

    img = Image.fromarray(img)
    img = np.array(img.rotate(direction * angle))


cv2.imshow("result", img )
cv2.waitKey()

