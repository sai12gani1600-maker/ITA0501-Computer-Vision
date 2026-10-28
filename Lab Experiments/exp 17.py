
import cv2

img = cv2.imread(r"image.jpg")

if img is not None:
    watermark = img.copy()
    cv2.putText(watermark, "WATERMARK", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    result = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
