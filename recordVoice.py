import pyaudio
import wave

# Set the parameters for the recording
FORMAT = pyaudio.paInt16  # Format of sampling
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate (samples per second)
CHUNK = 1024  # Chunk size (number of frames per buffer)
RECORD_SECONDS = 10  # Duration of the recording
OUTPUT_FILENAME = "recorded_audio2.wav"  # Name of the output file

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Initialize an empty list to store frames
frames = []

# Record the audio in chunks
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
audio.terminate()

# Save the recorded data as a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved as {OUTPUT_FILENAME}")
