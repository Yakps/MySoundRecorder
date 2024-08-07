import sounddevice as sd
from pydub import AudioSegment
from scipy.io.wavfile import write
import wavio as wv
#sampling frequency
freq = 44100

#recording duration
duration = 5
#Start the recorder for the given time and sample frequency value.
recording = sd.rec(int(duration*freq),
                   samplerate=freq, channels=2)
#record audio for a given number of seconds
sd.wait()
#numpy array data sampling frequency
write("recording0.wav", freq, recording)
#Convert numpy array to audio recording
wv.write("recording1.wav", recording, freq, sampwidth=2)

# WAV file downland
wav_file = "recording0.wav'  # Enter your wav file here"
output_file = "output_audio_file.mp3"
audio = AudioSegment.from_wav(wav_file)

# sound recording open
audio.export(output_file, format='mp3')
print(f'{wav_file} success {output_file} converted to format')
