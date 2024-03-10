import cv2
import numpy as np

img = cv2.imread("ronss.jpg", cv2.IMREAD_GRAYSCALE)

# Apply logarithmic transformation
img_log = np.log1p(img)

# Normalize the result to the range [0, 255]
img_log = (img_log / np.max(img_log)) * 255

# Convert to uint8 data type
img_log = np.uint8(img_log)

# Display the image
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 800, 600)

cv2.imshow("image", img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()
   
