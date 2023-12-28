import cv2
import os

def images_to_video(image_folder, output_video_path, fps=30):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":
    image_folder_path = "path/to/your/images"
    output_video_path = "output_video.mp4"
    images_to_video(image_folder_path, output_video_path)
