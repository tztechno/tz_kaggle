import torch
import numpy as np

def convert_to_input_tensor(frames):
    # frames: (16, 64, 64, 3)の形状を持つNumPy配列
    frames = np.transpose(frames, (0, 3, 1, 2))  # (16, 3, 64, 64)に軸を変換
    frames_tensor = torch.from_numpy(frames).float()  # NumPy配列をPyTorchのTensorに変換
    input_tensor = frames_tensor.unsqueeze(0)  # バッチサイズ1の4次元テンソルに変換
    return input_tensor




import torch
import numpy as np
from PIL import Image

def convert_to_input_tensor(paths, H=64, W=64, D=32):
    frames = []
    for path in paths:
        # 画像ファイルを読み込み、サイズを変更してからリストに追加
        img = Image.open(path).resize((W, H))
        frame = np.array(img, dtype=np.float32) / 255.0  # ピクセル値を[0, 1]に正規化
        frames.append(frame)

    # リストをNumPy配列に変換し、テンソルに変換してから軸を変換
    frames = np.array(frames)
    frames = np.transpose(frames, (0, 3, 1, 2))

    # バッチサイズ1の5次元テンソルに変換
    input_tensor = torch.from_numpy(frames).float().unsqueeze(0)

    # 3次元畳み込み層を適用するためのdepthの指定
    input_tensor = input_tensor.permute(0, 2, 1, 3, 4)
    input_tensor = input_tensor.reshape(1, D, 3, H, W)

    return input_tensor

