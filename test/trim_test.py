#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

import numpy as np
from librosa import load
from pyvad import trim

fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)

name = "voice/arctic_a0007.wav"
data, fs = load(name, sr=None)

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = trim(data, fs, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact[1] - vact[0] > 0, vact


fs = 16000
data = (np.random.rand(fs*3)-0.5)*0.05
for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = trim(data, fs, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact[1] - vact[0] == 0, vact
