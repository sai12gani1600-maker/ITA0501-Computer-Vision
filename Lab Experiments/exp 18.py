
import cv2

img = cv2.imread(r"image.jpg")

if img is not None:
    roi = img[50:200, 50:200]
    copied = roi.copy()
    img[220:370, 220:370] = copied

    cv2.imshow("Cropped Image", roi)
    cv2.imshow("Copy and Paste", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
