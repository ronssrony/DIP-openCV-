import cv2
import numpy as np

img = cv2.imread("imagg.jpeg", cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equ = cv2.equalizeHist(img)

# Stack original and equalized images side by side
res = np.hstack((img, equ))

# Display the images
cv2.imshow("image", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
