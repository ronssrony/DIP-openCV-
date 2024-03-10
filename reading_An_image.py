import cv2

# Read the image in grayscale
img = cv2.imread("ronss.jpg", cv2.IMREAD_GRAYSCALE)

# Create a named window with the specified flags
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# Set the desired window size (adjust the size as needed)
cv2.resizeWindow("image", 800, 600)

# Show the image in the created window
cv2.imshow("image", img)

# Wait for a key event and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
