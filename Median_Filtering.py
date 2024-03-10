import cv2
import numpy as np
import matplotlib.pyplot as plt

def median_filter(image, kernel_size):
    # Apply the filter using medianBlur
    result = cv2.medianBlur(image, kernel_size)
    return result

# Read the image in grayscale
img = cv2.imread("imagg.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply median filtering with a 5x5 kernel
filtered_img = median_filter(img, 5)

# Display the original and median filtered images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Median Filtered Image')
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.show()
