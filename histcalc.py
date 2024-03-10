import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("ronss.jpg" , cv2.IMREAD_GRAYSCALE)

histr = cv2.calcHist([img] , [0] , None , [256] , [0,256])

# Print the frequency of pixel value 1
print(histr[1])
# Print the frequency of pixel value 0
print(histr[0])
# Print the entire histogram array
print(histr)
plt.plot(histr)
plt.show()
