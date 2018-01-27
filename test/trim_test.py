#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

from librosa import load
from pyvad import trim

fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)

name = "voice/arctic_a0007.wav"
data, fs = load(name, sr=None)

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = trim(data, fs, fs_vad=16000, hoplength=30, vad_mode=0)

name = "noise.wav"
data, fs = load(name, sr=None)

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = trim(data, fs, fs_vad=16000, hoplength=30, vad_mode=0)
