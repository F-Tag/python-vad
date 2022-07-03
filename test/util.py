from pysptk.util import example_audio_file

from librosa import load
import numpy as np

fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)

def load_sp():
    name = example_audio_file()
    data, fs = load(name, sr=16000)
    data = np.tile(data, 2)
    data = np.hstack([data, -data])
    return data, fs

def load_noise():
    data, fs = load("noise.wav", sr=16000)
    return data, fs
