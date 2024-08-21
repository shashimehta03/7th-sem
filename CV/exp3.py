import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('abc.jpg', cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

def negative_transformation(img):
    return 255 - img

def log_transformation(img):
    c = 255 / np.log(1 + np.max(img))
    return c * np.log(1 + img)

def gamma_transformation(img, gamma):
    c = 255 / (np.max(img) ** gamma)
    return c * (img ** gamma)

def histogram_equalization(img):
    return cv2.equalizeHist(img)

neg_img = negative_transformation(image)
log_img = log_transformation(image).astype(np.uint8)
gamma_img = gamma_transformation(image, 0.5).astype(np.uint8)
hist_eq_img = histogram_equalization(image)

plt.subplot(2, 2, 2)
plt.imshow(neg_img, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(log_img, cmap='gray')
plt.title('Log Transformation')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(gamma_img, cmap='gray')
plt.title('Gamma Transformation')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('negative_transformation.jpg', neg_img)
cv2.imwrite('log_transformation.jpg', log_img)
cv2.imwrite('gamma_transformation.jpg', gamma_img)
cv2.imwrite('histogram_equalization.jpg', hist_eq_img)
