import librosa
import matplotlib.pyplot as plt
import os

path = 'audio data'

# Get list of all audio files in the specified directory
audio_files = [f for f in os.listdir(path) if f.endswith('.mp3')]

for audio_file in audio_files:
    # Load the audio file
    y, sr = librosa.load(os.path.join(path, audio_file))

    # Plot the waveform diagram of the audio
    plt.figure()
    plt.title(audio_file)
    librosa.display.waveshow(y, sr=sr)
    plt.tight_layout()

plt.show()
