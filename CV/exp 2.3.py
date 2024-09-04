#2.3
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('img-2.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imwrite('erosion.jpg', erosion)
dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite('dilation.jpg', dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening.jpg', opening)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('closing.jpg', closing)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite('gradient.jpg', gradient)
titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
images = [image, erosion, dilation, opening, closing, gradient]

plt.figure(figsize=(10, 7))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

