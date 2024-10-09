import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import threading

# Set up recording parameters
duration = 10  # seconds
sample_rate = 44100  # 44.1kHz
output_folder = "recordings"
stop_recording = False

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def record_audio(index=1):
    global stop_recording
    while not stop_recording:
        output_filename = os.path.join(output_folder, f'speaker_output_{index}.wav')
        print(f"Recording chunk {index}...")

        output_filename = os.path.join(output_folder, f'speaker_output_{index}.wav')
        print(f"Recording chunk {index}...")

        # Record 5 minutes of audio
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
        sd.wait()  # Wait until the recording is finished

        # Save the audio data as a .wav file
        wav.write(output_filename, sample_rate, audio_data)
        print(f"Saved recording to {output_filename}")

        # Increment the file index
        index += 1


def stop_by_keypress():
    global stop_recording
    input("Press 'q' and Enter to stop recording...\n")
    stop_recording = True

# Run the recording in a separate thread so the keypress check works
recording_thread = threading.Thread(target=record_audio, args=(1,))
recording_thread.start()

# Check for the 'q' keypress to stop recording
stop_by_keypress()

# Wait for the recording thread to finish before exiting
recording_thread.join()

print("Recording stopped.")