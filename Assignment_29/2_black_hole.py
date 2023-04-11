import os 
import cv2 
import numpy as np 

counter = 1
for i in range(4):
    paths = os.listdir(f"black_hole/{i+1}/")
    images = []

    for path in paths :      
        img = cv2.imread(f"black_hole/{counter}/" + path) 
        img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        img  = img.astype(np.float32)
        print(img.shape)
        images.append(img)

    res = np.zeros(img.shape)
    for img in images :
        res += img 

    res  = res / len(images)
    res = res.astype(np.uint8)
    res = cv2.resize(res , [300 , 300])

    counter +=1
    cv2.imwrite(f"{i+1}.jpg" , res)    

p = []
for i in range(4):
    p.append(cv2.imread(f"{i+1}.jpg"))

x = cv2.hconcat([p[0], p[1]])
y = cv2.hconcat([p[2], p[3]])
final_image = cv2.vconcat([x, y])


cv2.imshow("black hole result" , final_image )
cv2.imwrite("black_hole_result.jpg" , final_image)
cv2.waitKey()
