##################################################

from pydub import AudioSegment
display(AudioSegment.from_file('/kaggle/input/bengaliai-speech/train_mp3s/000005f3362c.mp3'))

##################################################

import librosa

path0 = 'path/to/your/audio/file.mp3'
y, sr = librosa.load(path0)

##################################################

