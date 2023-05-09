# 2D Convolution  and Histogram Equalization 📊📉

<br>

## How to install reuire libraries :
Run the Following Command :
> pip install -r requirements.txt 
<br>

## How to run :
Execute this command for each of the python files, in terminal: 
> python FileName.py  

<br>

## 1. 2D CONVOLUTION

Here, we want to Apply five 2D filters on our images :
the input image is : 
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/inputs/zeb.jpg" width="400" />

<br>
<br>
  
### 1_1. Our first filter is </b>*EDGE DETECTION*</b> :

> kernel = np.array([[-1 , -1 , -1],
                     [-1 ,  8 , -1],
                     [-1 , -1 , -1]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/edge.jpg" width="400" />


<br>
<br>
  
### 1_2. Our second filter is *SHARPENING FILTER* :

> kernel = np.array([[0  , -1 ,  0],
                     [-1 ,  5 , -1],
                     [0  , -1 ,  0]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/Sharpening.jpg" width="400" />

<br>
<br>
  
### 1_3. Our third filter is *EMBOSS FILTER* :

> kernel = np.array([[-2 , -1 ,  0],
                     [-1 ,  1 ,  1],
                     [0  ,  1 ,  2]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/emboss.jpg" width="400" />

<br>
<br>

### 1_3. Our third filter is *EMBOSS FILTER* :

> kernel = np.array([[-2 , -1 ,  0],
                     [-1 ,  1 ,  1],
                     [0  ,  1 ,  2]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/emboss.jpg" width="400" />

<br>
<br>
  
### 1_4. Our fourth filter is *IDENTITY FILTER* :

> kernel = np.array([[0  ,  0 ,  0],
                     [0  ,  1 ,  0],
                     [0  ,  0 ,  0]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/identity.jpg" width="400" />

<br>
<br>

### 1_5. Our fifth filter is *horizontal edges FILTER* :

> my_kernel1 = np.array([[ 1 ,  2 ,  1],
                         [ 0 ,  0 ,  0],
                         [-1 , -2 , -1]])

and the result after convolution is :
<p float="center">
  <img src="https://github.com/kiana-jahanshid/Image-Processing/blob/main/Assignment_32/outputs/vertical_edges.jpg" width="400" />

<br>
<br>

## MEDIAN FILTER 























