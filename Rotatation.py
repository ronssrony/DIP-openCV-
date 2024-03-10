import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ronss.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
angle = 45

rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))

Titles = ["Original", "Rotated"]
images = [img, rotated_img]
count = 2

for i in range(count):
    plt.subplot(1, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i], cmap='gray')

plt.show()
