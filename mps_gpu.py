import sys
import torch

print(f"Python: {sys.version}")
print(f"PyTorch: {torch.__version__}")

print(f"MPS available: {torch.backends.mps.is_available()}")
print(f"MPS built: {torch.backends.mps.is_built()}")

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using device:", device)
