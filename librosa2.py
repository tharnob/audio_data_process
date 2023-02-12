import glob
import librosa
import matplotlib.pyplot as plt

path = "audio data/*.mp3"
all_files = glob.glob(path)

for file in all_files:
    # Load the audio file
    y, sr = librosa.load(file)
    # Compute the intensity (root mean square) of the audio signal
    intensity = librosa.feature.rms(y=y)
    # Display the intensity
    plt.figure()
    plt.plot(intensity[0])
    plt.title('Intensity of audio file')
    plt.xlabel('Frame')
    plt.ylabel('Intensity')
    plt.show()
