#polygon data to mask image
masks = np.zeros((6, image_size, image_size, 1), dtype=bool)
for i,annotation in enumerate(annotej["annotations"]):
    if i<6:
        print(annotej["id"])
        segmentation = annotation["coordinates"]
        cur_mask = imantics.Polygons(segmentation).mask(*input_image_size).array
        cur_mask = np.expand_dims(resize(cur_mask, (image_size, image_size), mode='constant', preserve_range=True), 2)
        masks[i] = masks[i] | cur_mask
