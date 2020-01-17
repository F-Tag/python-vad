#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

import numpy as np
from librosa import load
from pyvad import split

fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)

name = "voice/arctic_a0007.wav"
data, fs = load(name, sr=None)
data = np.tile(data, 2)

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = split(data, fs, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact.size >= 0, vact


data = (np.random.rand(fs*3)-0.5)*0.05
for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = split(data, fs, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact.size == 0, vact
