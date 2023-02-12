import glob
import librosa
import matplotlib.pyplot as plt

path = "audio data/*.mp3"
all_files = glob.glob(path)

for file in all_files:
    y, sr = librosa.load(file)
    # Compute onset strength
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    # Plot the onset strength envelope
    plt.figure(figsize=(10, 4))
    plt.plot(onset_env, label='Onset strength')
    plt.title('Onset strength of ' + file)
    plt.xlabel('Time (samples)')
    plt.ylabel('Onset strength')
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.show()
