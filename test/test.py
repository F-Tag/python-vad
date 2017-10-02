#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyvad import vad
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import IPython.display


name = "C-28.wav"
fs, data = read(name)
data = np.mean(data, axis=1).astype(data.dtype)  # stereo to mono
time = np.linspace(0, len(data) / fs, len(data))  # time axis

vact = vad(data, fs, fs_vad=16000, hoplength=30, vad_mode=0)

dataf = data.astype('float') / 2**15
vact = vad(dataf, fs, fs_vad=16000, hoplength=30, vad_mode=0)
