def load_image(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

train_images = pd.Series(random.sample(paths,5)).progress_apply(load_image)
