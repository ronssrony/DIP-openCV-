import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    result = cv2.filter2D(image, -1, kernel)
    return result

# Read the image in grayscale
img = cv2.imread("imagg.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply average filtering with a 5x5 kernel
filtered_img = average_filter(img, 5)

# Display the original and filtered images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Average Filtered Image')
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.show()
