import cv2
import numpy as np
import matplotlib.pyplot as plt

def point_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
    points_of_interest = np.where(laplacian > 0, 255, 0).astype(np.uint8)
    return points_of_interest
def line_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)
    line_image = image.copy()

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return line_image

def edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 150)
    return edges

input_image = cv2.imread('img-2.jpg')
points_image = point_detection(input_image)
lines_image = line_detection(input_image)
edges_image = edge_detection(input_image)

# Display the results
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(points_image, cmap='gray')
plt.title('Points of Interest (LoG)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(lines_image, cv2.COLOR_BGR2RGB))
plt.title('Detected Lines (Hough Transform)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edges_image, cmap='gray')
plt.title('Detected Edges (Canny)')
plt.axis('off')

plt.tight_layout()
plt.show()
#3.1
