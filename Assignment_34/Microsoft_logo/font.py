import cv2
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image, ImageFont, ImageDraw 


def add_font(background):

    rgb = cv2.cvtColor(cv2.resize(cv2.imread(background) , (900 , 380)),cv2.COLOR_BGR2RGB)  
    pil  = Image.fromarray(rgb)  
    draw = ImageDraw.Draw(pil)  
    font = ImageFont.truetype("SegoePro-Bold.ttf", 110)  
    draw.text((300, 90), "Microsoft", font=font)  

    image = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)  
    cv2.imwrite("final_logo.jpg" , image)
    return image

res = add_font("logo.png")
cv2.imshow('', res)  
cv2.waitKey() 