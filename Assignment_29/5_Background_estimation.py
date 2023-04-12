import cv2
import numpy as np 
from skimage import data, filters

video = cv2.VideoCapture("cars.mp4")

frameIds = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 
frames = []
for fid in frameIds:
    video.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = video.read()
    frames.append(frame)
 
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8) 
cv2.imshow("road" , medianFrame)
cv2.imwrite("empty_road.jpg" , medianFrame)
cv2.waitKey() 
 