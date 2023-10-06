
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

mosaic_image=mosaic(image_input2[(y_min):(y_min+box_height),(x_min):(x_min+box_width)])
image_input2[(y_min):(y_min+box_height),(x_min):(x_min+box_width)]=mosaic_image
