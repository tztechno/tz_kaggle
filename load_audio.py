import librosa

def load_audio(filepath):
    audio, sr = librosa.load(filepath)
    return audio, sr
  
