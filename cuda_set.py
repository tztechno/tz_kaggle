# Set seed for reproducibility
torch.manual_seed(42)
np.random.seed(42)
random.seed(42)

# Check and set up CUDA
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# If CUDA is available, print GPU details
if device.type == "cuda":
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
