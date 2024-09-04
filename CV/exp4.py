import cv2
import numpy as np
import matplotlib.pyplot as plt
source_image_path = 'img-2.jpg'  
reference_image_path = 'img-3.jpg'  
source = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)
reference = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)
source_hist, bins = np.histogram(source.flatten(), 256, [0, 256])

reference_hist, bins = np.histogram(reference.flatten(), 256, [0, 256])

source_cdf = source_hist.cumsum()
source_cdf = source_cdf / source_cdf[-1]  # Normalize

reference_cdf = reference_hist.cumsum()
reference_cdf = reference_cdf / reference_cdf[-1]  # Normalize

mapping = np.zeros(256, dtype=np.uint8)
reference_cdf_index = 0

for src_pixel_value in range(256):
    while reference_cdf_index < 256 and source_cdf[src_pixel_value] > reference_cdf[reference_cdf_index]:
        reference_cdf_index += 1
    mapping[src_pixel_value] = reference_cdf_index if reference_cdf_index < 256 else 255

matched_image = mapping[source]
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.imshow(source, cmap='gray')
plt.title('Source Image'), plt.axis('off')
plt.subplot(2, 2, 2), plt.imshow(reference, cmap='gray')
plt.title('Reference Image'), plt.axis('off')
plt.subplot(2, 2, 3), plt.imshow(matched_image, cmap='gray')
plt.title('Histogram Matched Image'), plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('matched_image.jpg', matched_image)
