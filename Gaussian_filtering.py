import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image, kernel_size, sigma):
    # Create a 2D Gaussian kernel
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    
    # Apply the filter using convolution
    result = cv2.filter2D(image, -1, kernel * kernel.T)  # kernel * kernel.T for a 2D Gaussian
    
    return result

# Read the image in grayscale
img = cv2.imread("imagg.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian filtering with a 5x5 kernel and sigma = 1
filtered_img = gaussian_filter(img, 5, 1)

# Display the original and Gaussian filtered images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gaussian Filtered Image')
plt.imshow(filtered_img, cmap='gray')
plt.axis('off')

plt.show()
