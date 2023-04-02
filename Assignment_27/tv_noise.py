import cv2 
import numpy as np 

init_image = cv2.imread("tv4.jpg")
img = cv2.cvtColor(init_image , cv2.COLOR_BGR2GRAY)

rows, cols=img.shape
writer = cv2.VideoWriter("noise.mp4" , cv2.VideoWriter_fourcc(*'mp4v') , 30 , (rows , cols))

print(img.shape)
while True:
    noise1 = np.random.random((96 , 120)) * 255 
    noise1 = np.array(noise1 , dtype=np.uint8)
    img[26:122 , 325:445] = noise1

    noise2 = np.random.random((82 , 113)) * 255 
    noise2 = np.array(noise2 , dtype=np.uint8)
    img[160:242 , 307:420] = noise2

    noise2 = np.random.random((90 , 115)) * 255 
    noise2 = np.array(noise2 , dtype=np.uint8)
    img[280:370 , 310:425] = noise2
    writer.write(img)

    cv2.imshow("TV NOISE" , img)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

writer.release()

