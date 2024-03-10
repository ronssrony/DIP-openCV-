import cv2 
import numpy as np 
img = cv2.imread("ronss.jpg",cv2.IMREAD_GRAYSCALE)

rows ,cols = img.shape 

for i in range(rows):
    for j in range(cols):
        img[i][j] = 255-img[i][j] 

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 800, 600)

cv2.imshow("image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()        
