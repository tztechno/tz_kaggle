
def normalize_image_sizes(image_dir, output_dir=None, target_size=1200, mode='fit'):
    """
    Resizes all images in a directory while maintaining aspect ratio.
    
    Args:
        image_dir: Directory containing input images.
        output_dir: Directory to save the processed images. Defaults to image_dir.
        target_size: The desired maximum size for the longer side (or minimum size for the shorter side).
        mode: Resizing mode - 'fit' (fit within target), 'fill' (fill target), or 'pad' (fit with padding).
    """
    if output_dir is None:
        output_dir = image_dir

    os.makedirs(output_dir, exist_ok=True)

    print(f"Normalizing image sizes (mode: {mode}) while maintaining aspect ratio...")

    size_stats = {}
    converted_count = 0

    for img_file in sorted(os.listdir(image_dir)):
        if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue

        input_path = os.path.join(image_dir, img_file)
        output_path = os.path.join(output_dir, img_file)

        try:
            img = Image.open(input_path)
            original_size = img.size  # (width, height)
            original_aspect = original_size[0] / original_size[1]

            # Record original size for statistics
            size_key = f"{original_size[0]}x{original_size[1]}"
            if size_key not in size_stats:
                size_stats[size_key] = 0
            size_stats[size_key] += 1

            # Resize while maintaining aspect ratio
            if mode == 'fit':
                # Fit within target (長辺をtarget_sizeに合わせてリサイズ)
                if original_size[0] > original_size[1]:  # 横長
                    new_width = target_size
                    new_height = int(target_size / original_aspect)
                else:  # 縦長 or 正方形
                    new_height = target_size
                    new_width = int(target_size * original_aspect)
                    
            elif mode == 'fill':
                # Fill target (短辺をtarget_sizeに合わせてリサイズ)
                if original_size[0] > original_size[1]:  # 横長
                    new_height = target_size
                    new_width = int(target_size * original_aspect)
                else:  # 縦長 or 正方形
                    new_width = target_size
                    new_height = int(target_size / original_aspect)
                    
            elif mode == 'pad':
                # Fit with padding (短辺をtarget_sizeに合わせて、余白を追加)
                if original_size[0] > original_size[1]:  # 横長
                    new_width = target_size
                    new_height = int(target_size / original_aspect)
                else:  # 縦長 or 正方形
                    new_height = target_size
                    new_width = int(target_size * original_aspect)
                
                # 余白を追加して正方形にする
                img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                img_square = Image.new('RGB', (target_size, target_size), (255, 255, 255))
                offset = ((target_size - new_width) // 2, (target_size - new_height) // 2)
                img_square.paste(img_resized, offset)
                img = img_square
                print(f"  ✓ {img_file}: {original_size} → {new_width}x{new_height} (padded to {target_size}x{target_size})")
                img.save(output_path, quality=95)
                converted_count += 1
                continue
            
            else:
                raise ValueError(f"Unknown mode: {mode}. Use 'fit', 'fill', or 'pad'.")

            # リサイズ実行
            img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_resized.save(output_path, quality=95)
            converted_count += 1

            print(f"  ✓ {img_file}: {original_size} → {new_width}x{new_height} (aspect ratio: {original_aspect:.2f})")

        except Exception as e:
            print(f"  ✗ Error processing {img_file}: {e}")

    print(f"\nConversion complete: {converted_count} images")
    print(f"Original size distribution: {size_stats}")
    return converted_count

########################################

mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])

normalized_image = normalize(image, mean, std)
print(normalized_image)

########################################

import torch
import torchvision.transforms as T
import numpy as np

img=cv2.imread(paths0[i])
images0+=[img]
img_tensor = torch.from_numpy(img).permute(1, 2, 0).float()
nor_image = normalize(img_tensor).permute(2, 0, 1)
images2+=[nor_image]

########################################

import torch
import torchvision.transforms as T
import numpy as np

normalize = T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

# Assuming you have a NumPy array image
image_np = np.random.rand(3, 224, 224)  # Example random image

# Convert the NumPy array image to a Torch tensor
image_tensor = torch.from_numpy(image_np)

# Add a batch dimension if the tensor doesn't have one
if len(image_tensor.shape) == 3:
    image_tensor = image_tensor.unsqueeze(0)

# Normalize the image tensor
normalized_image = normalize(image_tensor)

# Print the shape and range of the normalized image tensor
print(normalized_image.shape)
print(normalized_image.min(), normalized_image.max())

########################################
