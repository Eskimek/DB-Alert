import pyaudio
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time

THRESHOLD_DB = 80
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
COOLDOWN_SECONDS = 3

def rms_to_db(rms):
    return 20 * np.log10(rms) if rms > 0 else -np.inf

def show_popup(db_value):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Noise Detected", f"Noise level exceeded {THRESHOLD_DB} dB!\nYour scream reached {db_value:.1f} dB")
    root.destroy()

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


last_detection_time = 0

try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32)
        rms = np.sqrt(np.mean(np.square(audio_data)))
        db = rms_to_db(rms)

        now = time.time()
        if not np.isnan(db) and db > THRESHOLD_DB and (now - last_detection_time > COOLDOWN_SECONDS):
            print(f"Wykryto hałas: {db:.1f} dB")
            last_detection_time = now
            show_popup(db)
except KeyboardInterrupt:
    print("\nZakończono.")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
