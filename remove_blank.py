def get_non_white_rectangles(image_path, threshold_value):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = []
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        rectangles.append((x,y,w,h))
        rec_img=image[y:y+h,x:x+w,:]
    return rec_img
