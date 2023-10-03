########################################

import warnings
warnings.filterwarnings("ignore", category=UserWarning)  # Dataset has 0 variance
warnings.filterwarnings("ignore", category=FutureWarning)  # shade is now deprecated

########################################

import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter('ignore')

########################################

def warn(*args, **kwargs):
    pass
warnings.warn = warn
warnings.filterwarnings('ignore')

########################################
