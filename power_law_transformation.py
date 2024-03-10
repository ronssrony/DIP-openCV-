import cv2
import numpy as np

img = cv2.imread("ronss.jpg", cv2.IMREAD_GRAYSCALE)

# Define the gamma value (adjust as needed)
gamma = 0.4

# Apply power-law transformation
img_power = np.power(img / 255.0, gamma) * 255.0

# Convert to uint8 data type
img_power = np.uint8(img_power)

# Display the image
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 800, 600)

cv2.imshow("image", img_power)
cv2.waitKey(0)
cv2.destroyAllWindows()
