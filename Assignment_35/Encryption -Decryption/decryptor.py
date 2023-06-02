from PIL import Image  
import cv2
from encryptor import encryption

def decryption(encrypted_image , key):
        output_image = encrypted_image * key
        output_image *= 255.0
        return output_image

