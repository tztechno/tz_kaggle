import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Path to the TIFF image file
image_path = '/path/to/your/image.tif'

# Load the TIFF image
image = mpimg.imread(image_path)

# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()
