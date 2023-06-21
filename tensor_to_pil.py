from PIL import Image
import torch

def tensor_to_pil(tensor):
    # テンソルをNumPy配列に変換し、ピクセル値の範囲を0から1に正規化する
    tensor = tensor.cpu().numpy()
    tensor = tensor.transpose(1, 2, 0)
    tensor = tensor.clip(0, 1)
    
    # NumPy配列をPIL画像に変換する
    pil_image = Image.fromarray((tensor * 255).astype(np.uint8))
    
    return pil_image
