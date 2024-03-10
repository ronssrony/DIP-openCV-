import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ronss.jpg", cv2.IMREAD_GRAYSCALE)
rows,cols = img.shape 
tx, ty = 1000,10
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]]) #no scaling , no rotation , shift x direction

translated_img = cv2.warpAffine(img, translation_matrix, (cols,rows))

Titles = ["Original", "Translated"]
images = [img, translated_img]
count = 2

for i in range(count):
    plt.subplot(1, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i], cmap='gray') 

plt.show()
