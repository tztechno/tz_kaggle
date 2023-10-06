
cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)

src1: 最初の入力画像（通常、背景画像として使用されます）。
alpha: src1の重み付け係数。この係数が大きいほどsrc1の画像が強調されます。
src2: 2番目の入力画像（通常、前景画像として使用されます）。
beta: src2の重み付け係数。この係数が大きいほどsrc2の画像が強調されます。
gamma: 合成された画像に追加されるオプションのガンマ値（明るさを調整するための値）。通常、0.0です。
