# audio_data_process
used librosa 


### librosa1:

This code is performing audio processing on multiple MP3 files in a directory. It uses the Python library "librosa" for processing audio files and "matplotlib" for visualizing the results.

The code first uses the "glob" library to gather all MP3 files in the directory specified by the "path" variable. Then, for each file in the list of files, the audio data is loaded using the "librosa.load" function.

Next, the code performs several steps to extract the melspectrogram features of the audio file:

1. It calculates the power spectrogram of the audio data using the "librosa.feature.melspectrogram" function.

2. It converts the power spectrogram to decibels using the "librosa.power_to_db" function.

3. Finally, the code displays the melspectrogram using the "librosa.display.specshow" function from the "librosa" library, which is a wrapper for Matplotlib's "imshow" function.

The "plt.tight_layout()" and "plt.show()" calls at the end of the code are used to display the melspectrogram in a well-formatted manner using Matplotlib.




### librosa2:

This code is performing audio processing on multiple MP3 files in a directory. It uses the Python library "librosa" for processing audio files and "matplotlib" for visualizing the results.

The code first uses the "glob" library to gather all MP3 files in the directory specified by the "path" variable. Then, for each file in the list of files, the audio data is loaded using the "librosa.load" function.

Next, the code computes the intensity (root mean square) of the audio signal using the "librosa.feature.rms" function. The intensity is a measure of the energy in the audio signal and is often used as a simple representation of the overall loudness of the signal.

Finally, the code displays the intensity of the audio signal using Matplotlib's "plot" function, with the x-axis representing the frame index and the y-axis representing the intensity value. The "plt.show()" call at the end of the code is used to display the intensity plot in a well-formatted manner using Matplotlib.




### librosa3:

This code is performing audio processing on multiple MP3 files in a directory. It uses the Python library "librosa" for processing audio files and "matplotlib" for visualizing the results.

The code first uses the "glob" library to gather all MP3 files in the directory specified by the "path" variable. Then, for each file in the list of files, the audio data is loaded using the "librosa.load" function.

Next, the code performs several steps to extract the chroma features of the audio file:

1. It calculates the chroma short-time Fourier transform (STFT) of the audio data using the "librosa.feature.chroma_stft" function. Chroma features represent the energy of a specific pitch class in a given audio frame.

2. The code displays the chroma features using the "librosa.display.specshow" function from the "librosa" library, which is a wrapper for Matplotlib's "imshow" function.

The "plt.tight_layout()" and "plt.show()" calls at the end of the code are used to display the chroma features in a well-formatted manner using Matplotlib. The "cmap" argument is used to specify the color map used to display the chroma features, with the "coolwarm" color map selected in this case.



### librosa4:

This code uses the "librosa" library to perform audio processing and the "matplotlib" library to visualize the results.

The code first uses the "glob" library to gather all MP3 files in the directory specified by the "path" variable. Then, for each file in the list of files, the audio data is loaded using the "librosa.load" function.

Next, the code performs several steps to compute the onset strength of the audio file:

1. It computes the onset strength of the audio data using the "librosa.onset.onset_strength" function. Onset strength is a measure of the strength or intensity of audio events, such as the beginning of a sound or note.

2. The code plots the onset strength envelope of the audio file using Matplotlib's "plot" function. The x-axis represents time in samples, while the y-axis represents the onset strength. The "plt.tight_layout()" call at the end of the code is used to display the onset strength envelope in a well-formatted manner.



### librosa5:

This code uses the librosa library to extract the zero-crossing rate of a set of audio files. The zero-crossing rate is the rate at which the audio signal crosses the zero-value axis. This feature is often used in audio analysis and can be useful in characterizing the rhythm and tempo of an audio signal.

The code first defines a path to the audio files, and then uses the glob library to retrieve all files that match the specified pattern. For each audio file, the code loads the file using the librosa.load function, which returns the audio signal y and the sample rate sr. The zero-crossing rate is then computed using the librosa.feature.zero_crossing_rate function, which returns a single-dimensional array representing the zero-crossing rate for each frame of the audio signal. Finally, the code plots the zero-crossing rate using matplotlib.


### librosa6:

The code first imports the necessary libraries (librosa, matplotlib, and os). The path variable is set to the directory where the audio files are stored. The code then gets a list of all the .mp3 files in the directory using a list comprehension and the os.listdir function.

For each audio file in the list, the code loads the audio file using librosa.load and passes the file path to it. The waveform of the audio is then plotted using librosa.display.waveshow and displayed using plt.show. The title of each plot is set to the name of the audio file.


