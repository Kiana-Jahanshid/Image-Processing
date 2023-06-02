import cv2
import numpy as np
from cv2 import *
from key_generator import secret_key_generator

def encryption():
        input_image = cv2.imread("input/van.jpg", cv2.COLOR_BGR2RGB)
        x, y ,z= input_image.shape
        input_image = input_image.astype(float) / 255

        key = secret_key_generator()

        image_encrypted = input_image / key
        cv2.imwrite('CipherImage.bmp', image_encrypted * 255 )
       
        return image_encrypted , key 

