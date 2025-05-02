


import wandb
secret_value = “xxxxxx”
wandb.login(key=secret_value)
# save metrics into wandb folder
import os
os.environ["WANDB_DIR"] = "./wandb"
wandb.init(project="yyyyyy", mode="online")
