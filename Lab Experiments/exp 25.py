
import cv2

img = cv2.imread(r"image.jpg")

if img is not None:
    cv2.imshow("Watch Image", img)
    print("Image loaded successfully.")
    print("For watch recognition, use a watch image.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
