import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check whether image is found
if img is None:
    print("Image NOT FOUND")
else:
    print("Image FOUND")

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gray Scale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
