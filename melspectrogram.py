import librosa

y, sr = librosa.load(path)
mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

img=log_mel_spectrogram
img=cv2.resize(np.array(img),dsize=(128,128))
X = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

plt.imshow(X)
plt.axis('off') 
plt.savefig('./mel/'+label+'_'+file+'.png', bbox_inches='tight', pad_inches=0)
plt.close
