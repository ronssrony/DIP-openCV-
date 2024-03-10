import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("ronss.jpg" , cv2.IMREAD_GRAYSCALE) 

half = cv2.resize(img , (0,0) , fx=.1 , fy=.1) 
bigger = cv2.resize(img , (3000,3000)) 
stretch_near = cv2.resize(img , (730,540) , interpolation=cv2.INTER_LINEAR) 

Titles = ["Orginal" , "Half", "Bigger" , "Interpolation Nearest"]
images = [img ,half , bigger , stretch_near] 
count = 4 

for i in range(count):
    plt.subplot(2, 2 , i+1)
    plt.title(Titles[i]) 
    plt.imshow(images[i])

plt.show()    
