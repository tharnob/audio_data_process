import glob
import librosa
import matplotlib.pyplot as plt

path = "audio data/*.mp3"
all_files = glob.glob(path)

for file in all_files:
    y, sr = librosa.load(file)
    # Perform processing on the audio file
    # Extract chroma features using librosa
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    # Display the chroma features
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', cmap='coolwarm')
    plt.colorbar()
    plt.title('Chroma features')
    plt.tight_layout()
    plt.show()
