import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(image, title, cmap='gray'):
    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()
image = cv2.imread('matched_image.jpg')
denoised_image = cv2.medianBlur(image, 5)
display_image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "Original Image")
display_image(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB), "Denoised Image (Median Filter)")
cv2.imwrite('denoised_image.jpg', denoised_image)
denoised_image_gray = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.float32) / 25
degradation_function = np.fft.fft2(kernel, s=denoised_image_gray.shape)
noise_spectrum = 0.01
denoised_fft = np.fft.fft2(denoised_image_gray)
inverse_filter = np.conj(degradation_function) / (np.abs(degradation_function) ** 2 + noise_spectrum)
restored_fft = denoised_fft * inverse_filter
restored_image = np.fft.ifft2(restored_fft)
restored_image = np.abs(restored_image)
restored_image = cv2.normalize(restored_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
display_image(restored_image, "Restored Image (Inverse Filtering)")
cv2.imwrite('restored_image.jpg', restored_image)
