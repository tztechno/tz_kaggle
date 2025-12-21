from google.colab import userdata
import os
os.environ['secret_hf_token'] = userdata.get('secret_hf_token')
