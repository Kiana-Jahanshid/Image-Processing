import cv2 as cv
import numpy as np

image = cv.imread("Assignment_34\inputs\watermelon.jpg")

hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
H,S,V = cv.split(hsv)

# Shift only greens (Hue near 120) around hue circle by 120 degrees to blues - remembering OpenCV halves all these values - see comment
H[(H>0)&(H<30)] += 60
H[(H>0)&(H<40)] += 60
H[(H>40)&(H<60)] -= 40
H[(H>57)&(H<90)] -= 50
H[(H>90)&(H<100)] -= 90
H[(H>99)&(H<140)] -= 110


# H[(H>=0)&(H<20)] += 65
# H[(H>=340)&(H<=360)] += 70
H[(H>=320)&(H<340)] += 80
H[(H>=300)&(H<320)] += 90


result = cv.merge((H,S,V))
result = cv.cvtColor(result,cv.COLOR_HSV2BGR)
cv.imwrite("result.png",result)