pip install nibabel

import nibabel as nib

# niiファイルのパスを指定
nii_file_path = 'path/to/your/nii/file.nii'

# niiファイルを読み込む
nii_img = nib.load(nii_file_path)

# ボリュームデータを取得
data = nii_img.get_fdata()

# データの次元を表示
print(data.shape)
