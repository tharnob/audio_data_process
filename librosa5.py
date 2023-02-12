import librosa
import matplotlib.pyplot as plt
import numpy as np
import glob

path = "audio data/*.mp3"
all_files = glob.glob(path)

for file in all_files:
    y, sr = librosa.load(file)
    # Extract the zero-crossing rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    # Plot the zero-crossing rate
    plt.figure(figsize=(10, 4))
    plt.plot(zero_crossing_rate[0])
    plt.title('Zero-crossing rate')
    plt.xlabel('Frame')
    plt.ylabel('Zero-crossing rate')
    plt.tight_layout()
    plt.show()
