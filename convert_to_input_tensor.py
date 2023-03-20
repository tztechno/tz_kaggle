import torch
import numpy as np

def convert_to_input_tensor(frames):
    # frames: (16, 64, 64, 3)の形状を持つNumPy配列
    frames = np.transpose(frames, (0, 3, 1, 2))  # (16, 3, 64, 64)に軸を変換
    frames_tensor = torch.from_numpy(frames).float()  # NumPy配列をPyTorchのTensorに変換
    input_tensor = frames_tensor.unsqueeze(0)  # バッチサイズ1の4次元テンソルに変換
    return input_tensor
    
