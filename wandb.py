
import wandb

def auto_login_wandb():
    wandb.login(key="YOUR_API_KEY")  

auto_login_wandb()

---------------------

from kaggle_secrets import UserSecretsClient
import wandb
user_secrets = UserSecretsClient()
secret_value = user_secrets.get_secret("wandb_api_key")
wandb.login(key=secret_value)

# save metrics into wandb folder
import os
os.environ["WANDB_DIR"] = "./wandb"
wandb.init(project="open-r1", mode="online")

-------------------------

# Wandb login:
from kaggle_secrets import UserSecretsClient
import wandb
user_secrets = UserSecretsClient()
secret_value = user_secrets.get_secret("wandb_api_key")
wandb.login(key=secret_value)

