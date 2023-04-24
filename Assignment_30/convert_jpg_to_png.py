from PIL import Image
import cv2
def jpg_to_png(img ):
    
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    array = list(range(0,20))
    newData = []
    for item in datas:
        if (item[0] in array) or (item[1] in array )or (item[2] in array):
                    # finding black colour by its RGB value
                    # storing a transparent value when we find a black colour
                    newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
    
    rgba.putdata(newData)
    rgba.save(f"LEFT.png", "PNG")
    return rgba


img = Image.open("resized_left_eye22.png")
jpg_to_png(img )