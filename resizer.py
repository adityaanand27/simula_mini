import cv2

# Load the image
img = cv2.imread('simu/red.png')

# Define the desired size
width = 50
height = 50
dim = (width, height)

# Resize the image
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Save the resized image
cv2.imwrite('simu/newred.png', resized_img)

# Display the original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()