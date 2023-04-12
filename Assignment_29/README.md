# Basic Math Operations in image processing
## How to install reuire libraries :
Run Following Command :
> pip install -r requirements.txt 
## How to run :
Execute this command for each of the python files, in terminal ( python FileName.py ) 
<br>
<br>
# 🔸🔶 Results 🔶🔸

# 1. Face Morphing
Two input images are :


<p float="left">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/Queen1.jpg" width="200" />
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/sor.jpg" width="200" /> 
</p>

+ ###  Final Result :
> ![image](https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/face_morphing_result_s.jpg)

<br>
<br>

## 2. Black Hole
There are four input images from this black hole ,with different noise pattern . 
Here we have four slice of "one of mentioned images" , that contain noise :
<p float="left">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/selected/1.jpg" width="130" />
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/selected/2.jpg" width="130" /> 
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/selected/3.jpg" width="130" /> 
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/selected/4.jpg" width="130" /> 
</p>
so , we have to reduce noise by Averaging each same quarter , and concatenate columns of first row , then  columns of second row at the end .

> ![image](https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/black_hole_result_s.jpg)


<br>
<br>

# 3. Photo to Sketch

* input photo :
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/albert.jpg" width="300" /> 
</p>
<br>

* Sketched result : 
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/sketch_result.jpg" width="300" /> 
</p>
<br>
<br>

# 4. Find the secret text

+ Here we have 2 input images , and the left image contains  hidden text , which we want to detect it with the right one :
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/1.jpg" width="300" /> 
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/2.jpg" width="300" /> 
</p>
<br>

+ Hidden text :
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/secret_text_s.JPG" width="300" /> 
</p>
<br>
<br>


# 5. Background estimation
<br>
<br>

# 6. Virtual decoration
Here is the main image , which we want to change it's floor covering :
<p float="middle">
  <img src ="inputs\room.jpg" width="400" /> 
</p>
<br>
and this is our desire floor covering which want to apply it into the above main image :
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/floor.jpg" width="400" /> 
</p>
<br>
aslo , this is mask image :
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/room_mask.jpg" width="400" /> 
</p>
<br>

##  Solution ❓❔❓
### 1.  first we add inverted mask with floor cover :  
<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/invert_mask.jpg" width="250" /> 
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/floor.jpg" width="250" /> 
</p>
<br>

## result is :
<p float="middle">
     _____  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/final_floor.jpg" width="450" /> 
</p>
<br>

## 2. Now, add original room photo with initial mask :

<p float="middle">
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/room.jpg" width="250" /> 
  <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/inputs/room_mask.jpg" width="250" /> 
</p>
<br>

so , this is the result :
<p float="middle">
     ______  <img src ="final_furniture.jpg" width="450" /> 
</p>
<br>

## 3. Then , we invert zero pixels of "stage 1" into white pixels :
<p float="middle">
    <img src ="final_floor.jpg" width="250" /> 
    -->
    <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/final_floor_with_whitewall.jpg" width="250" /> 
</p>
<br>

## 4. At the end, we need to add results of "stage3" with "stage2" :
<p float="middle">
    <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/final_floor_with_whitewall.jpg" width="250" /> 
    <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/final_furniture.jpg" width="250" /> 
</p>
<br>

# Final result :
<p float="middle">
    <img src ="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_29/outputs/final_decoration.jpg" /> 
</p>
<br>
