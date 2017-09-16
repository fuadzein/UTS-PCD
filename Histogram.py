import cv2

image = cv2.imread('E:\contoh.jpg')
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.imwrite("Histogram.jpg", image)
