#3.2
import cv2
import numpy as np
import matplotlib.pyplot as plt
def boundary_linking(edge_image):
    contours, _ = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def boundary_representation(contours):
    chain_codes = []
    for contour in contours:
        codes = []
        for i in range(len(contour)):
            if i == len(contour) - 1:
                next_point = contour[0][0]
            else:
                next_point = contour[i + 1][0]

            dx = next_point[0] - contour[i][0][0]
            dy = next_point[1] - contour[i][0][1]

            if dx == 1 and dy == 0:
                codes.append(0)
            elif dx == 1 and dy == 1:
                codes.append(1)
            elif dx == 0 and dy == 1:
                codes.append(2)
            elif dx == -1 and dy == 1:
                codes.append(3)
            elif dx == -1 and dy == 0:
                codes.append(4)
            elif dx == -1 and dy == -1:
                codes.append(5)
            elif dx == 0 and dy == -1:
                codes.append(6)
            elif dx == 1 and dy == -1:
                codes.append(7)

        chain_codes.append(codes)

    return chain_codes

def boundary_description(contours):
    fourier_descriptors = []
    for contour in contours:
        contour = contour[:, 0, :]  # Remove unnecessary dimensions
        complex_contour = contour[:, 0] + 1j * contour[:, 1]
        descriptors = np.fft.fft(complex_contour)

        fourier_descriptors.append(descriptors[:10])  # Adjust as needed

    return fourier_descriptors

input_image = cv2.imread('img-2.jpg')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
edges_image = cv2.Canny(gray_image, 100, 200)
contours = boundary_linking(edges_image)
chain_codes = boundary_representation(contours)
fourier_descriptors = boundary_description(contours)

plt.figure(figsize=(10, 8))
plt.subplot(1, 2, 1)
plt.imshow(edges_image, cmap='gray')
plt.title('Edge Detected Image')
plt.axis('off')

plt.subplot(1, 2, 2)
contour_image = input_image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.title('Linked Boundaries')
plt.axis('off')

plt.tight_layout()
plt.show()
print("Chain Codes for each contour:")
for i, codes in enumerate(chain_codes):
    print(f"Contour {i+1}: {codes}")

print("\nFourier Descriptors for each contour:")
for i, descriptors in enumerate(fourier_descriptors):
    print(f"Contour {i+1}: {descriptors}")
