import numpy as np
from PIL import Image
import cv2


def secret_key_generator():
    input_image = cv2.imread("input/van.jpg", cv2.COLOR_BGR2RGB)
    x, y ,z= input_image.shape

    mu, sigma = 0 , 0.0001  
    key = np.random.normal(mu, sigma, (x, y , z)) 
    #key = np.random.randint(1, 255, (x, y, z))
    np.save('secret_key.npy' , key)

    #key = Image.fromarray(key.astype("uint8"))
    return key

secret_key_generator()