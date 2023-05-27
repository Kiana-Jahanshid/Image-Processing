from PIL import Image
import numpy as np

img = Image.open('input/final_logo.png')
img = img.convert("RGBA")
image = np.array(img)

gray = np.sum(image[:,:,:3], axis=2)
white_mask = np.where(gray == 80*3, 1, 0)

alpha = np.where(white_mask, 0, image[:,:,-1])

image[:,:,-1] = alpha 
img = Image.fromarray(np.uint8(image))

img.save("png_logo2.png", "PNG")