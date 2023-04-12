import cv2 
import numpy as np 

q = cv2.imread("Queen1.jpg")
s= cv2.imread("sor.jpg")
q = cv2.resize(q , [230 , 300])
s= cv2.resize(s , [230 , 300])
q = cv2.cvtColor(q , cv2.COLOR_BGR2GRAY)
s = cv2.cvtColor(s , cv2.COLOR_BGR2GRAY)

lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, 2) * 255.0, 0, 255)
q = cv2.LUT(q, lookUpTable)

lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, 0.6) * 255.0, 0, 255)
s = cv2.LUT(s, lookUpTable)


q  = q.astype(np.float32)
s = s.astype(np.float32)
a,b,c= [0,0,0]  
img_list = []

for i in range(3):
    print(a , b , c)
    r = ( q*((1+a)/(2+c)) + s*((1+b)/(2+c)) )
    if i==0 :
        c+=1
        a+=1
    if i==1 :
        a-=1
        b+=1
    r=r.astype(np.uint8)
    img_list.append(r)
    cv2.imwrite(f"morph_{i+1}.jpg" , r) 

for i in range(1,4):
    img_list.append(cv2.imread(f"morph_{i}.jpg"))

s=s.astype(np.uint8)
q=q.astype(np.uint8)
result = cv2.hconcat([q,img_list[1],img_list[0],img_list[2],s])

cv2.imshow("Queen + Sori" , result)
cv2.imwrite("face_morphing_result.jpg" , result )
cv2.waitKey()
