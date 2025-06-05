
[offline install]


import subprocess
import sys
import os

def download_packages():
    packages = [
        # PyTorch and related
        "torch==2.6.0+cu124",
        "torchvision==0.16.0+cu124", 
        "torchaudio==2.6.0+cu124",
        "pytorch-lightning==2.5.1.post0",
        "torchmetrics==1.7.1",
        "lightning-utilities==0.14.3",
        
        # CUDA libraries
        "nvidia-cuda-nvrtc-cu12==12.4.127",
        "nvidia-cuda-runtime-cu12==12.4.127",
        "nvidia-cuda-cupti-cu12==12.4.127",
        "nvidia-cublas-cu12==12.4.5.8",
        "nvidia-cufft-cu12==11.2.1.3",
        "nvidia-curand-cu12==10.3.5.147",
        "nvidia-cusolver-cu12==11.6.1.9",
        "nvidia-cudnn-cu12==9.1.0.70",
        "nvidia-cusparse-cu12==12.3.1.170",
        "nvidia-nvjitlink-cu12==12.4.127",
        "nvidia-nccl-cu12==2.21.5",
        
        # Dependencies
        "numpy==1.26.4",
        "packaging==24.0",
        "typing-extensions==4.13.2",
        "filelock==3.18.0",
        "sympy==1.13.1",
        "networkx==3.4.2",
        "jinja2==3.1.6",
        "fsspec==2025.3.2",
        "triton==3.2.0",
        
        # Other important packages
        "pillow==11.1.0",
        "tqdm==4.67.1",
        "PyYAML==6.0.2",
        "aiohttp==3.12.7",
        "frozenlist==1.6.0",
        "multidict==6.4.3",
        "yarl==1.20.0",
        "aiosignal==1.3.2",
        "aiohappyeyeballs==2.6.1",
        "propcache==0.3.1",
    ]
    
    # ダウンロード先ディレクトリの作成
    download_dir = "offline_packages"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # プラットフォーム設定
    platform = "win_amd64"  # Windows用
    # Linux用の場合は "linux_x86_64" に変更
    
    # PyTorch CUDAバージョン用の追加インデックス
    extra_index_url = "https://download.pytorch.org/whl/cu124"
    
    for package in packages:
        try:
            print(f"Downloading {package}...")
            
            # PyTorchパッケージの場合は追加インデックスを使用
            if any(pytorch_pkg in package for pytorch_pkg in ["torch", "torchvision", "torchaudio"]):
                subprocess.run([
                    sys.executable, "-m", "pip", "download",
                    "--extra-index-url", extra_index_url,
                    "--only-binary=:all:",
                    "--platform", platform,
                    "--python-version", "311",
                    "--implementation", "cp",
                    "--abi", "cp311",
                    "--dest", download_dir,
                    package
                ], check=True)
            else:
                subprocess.run([
                    sys.executable, "-m", "pip", "download",
                    "--only-binary=:all:",
                    "--platform", platform,
                    "--python-version", "311", 
                    "--implementation", "cp",
                    "--abi", "cp311",
                    "--dest", download_dir,
                    package
                ], check=True)
                
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {package}: {e}")
            continue
    
    print(f"All packages downloaded to {download_dir}/ directory!")
    print("\nTo install offline:")
    print(f"pip install --no-index --find-links {download_dir}/ <package_name>")
    print(f"Or install all: pip install --no-index --find-links {download_dir}/ -r requirements.txt")

def create_requirements_file():
    """requirements.txtファイルを作成"""
    packages = [
        "torch==2.6.0+cu124",
        "torchvision==0.16.0+cu124",
        "torchaudio==2.6.0+cu124",
        "pytorch-lightning==2.5.1.post0",
        "torchmetrics==1.7.1",
        "lightning-utilities==0.14.3",
        "nvidia-cuda-nvrtc-cu12==12.4.127",
        "nvidia-cuda-runtime-cu12==12.4.127",
        "nvidia-cuda-cupti-cu12==12.4.127",
        "nvidia-cublas-cu12==12.4.5.8",
        "nvidia-cufft-cu12==11.2.1.3",
        "nvidia-curand-cu12==10.3.5.147",
        "nvidia-cusolver-cu12==11.6.1.9",
        "nvidia-cudnn-cu12==9.1.0.70",
        "nvidia-cusparse-cu12==12.3.1.170",
        "nvidia-nvjitlink-cu12==12.4.127",
        "nvidia-nccl-cu12==2.21.5",
        "numpy==1.26.4",
        "packaging==24.0",
        "typing-extensions==4.13.2",
        "filelock==3.18.0",
        "sympy==1.13.1",
        "networkx==3.4.2",
        "jinja2==3.1.6",
        "fsspec==2025.3.2",
        "triton==3.2.0",
        "pillow==11.1.0",
        "tqdm==4.67.1",
        "PyYAML==6.0.2",
        "aiohttp==3.12.7",
        "frozenlist==1.6.0",
        "multidict==6.4.3",
        "yarl==1.20.0",
        "aiosignal==1.3.2",
        "aiohappyeyeballs==2.6.1",
        "propcache==0.3.1",
    ]
    
    with open("requirements.txt", "w") as f:
        for package in packages:
            f.write(package + "\n")
    
    print("requirements.txt created!")

if __name__ == "__main__":
    create_requirements_file()
    download_packages()

----


[install from notebook]

    !grep -v "nvidia-" /kaggle/input/download-lightning2/requirements.txt > requirements_no_cuda.txt
    !pip install --no-index --find-links /kaggle/input/download-lightning2/offline_packages/ -r requirements_no_cuda.txt --no-deps
    
    
    import pytorch_lightning as L
    from pytorch_lightning import LightningDataModule
    from pytorch_lightning import LightningModule
    from pytorch_lightning import Trainer
    from pytorch_lightning import seed_everything
    from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
    from pytorch_lightning.loggers import TensorBoardLogger, WandbLogger

