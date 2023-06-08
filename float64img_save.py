image_float64 = np.full((480, 640), 0.5, dtype=np.float64)

image_normalized = (image_float64 - np.min(image_float64)) / (np.max(image_float64) - np.min(image_float64))

image_uint8 = (image_normalized * 255).astype(np.uint8)

cv2.imwrite("image.jpg", image_uint8)
