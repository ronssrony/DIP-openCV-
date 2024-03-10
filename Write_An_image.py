import cv2 
img = cv2.imread("ronss.jpg" , cv2.IMREAD_GRAYSCALE)

filename = "ronss_copy.jpg" 
v = cv2.imwrite(filename , img) 
if v==True:
    print('Image saved successfully')
else:
    print('image saved failed')    
