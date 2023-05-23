import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw 


def add_font(background):
    background = cv2.resize(background, (1030 , 380))
    rgb = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
    image  = Image.fromarray(rgb)  
    draw = ImageDraw.Draw(image)  
    font = ImageFont.truetype("SegoePro-Bold.ttf", 130)  
    draw.text((300, 90), "Microsoft", font=font)  
    
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  
    cv2.imwrite("final_logo.jpg" , image)
    return image



background = np.ones(shape=(800,2300,3), dtype=np.uint8) * 80
background[200:380 , 200:380] = (35 , 80  , 245)
background[200:380 , 400:580] = (0  , 190 , 130)
background[400:580 , 200:380] = (240, 165 ,   0)
background[400:580 , 400:580] = (1  , 180 , 255)

res = add_font(background)
cv2.imshow('', res)  
cv2.waitKey() 

