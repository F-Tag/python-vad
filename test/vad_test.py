#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

import numpy as np
from librosa import load

from pyvad import vad

fs_vads = (8000, 16000, 32000, 48000)
hops = (10, 20, 30)
vad_modes = (0, 1, 2, 3)
fss = [16000, 22050]

name = "voice/arctic_a0007.wav"

for fs in fss:

    data, fs_r = load(name, sr=fs)
    for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
        vact = vad(data, fs_r, fs_vad=fs_vad,
                   hop_length=hop, vad_mode=vad_mode)
        assert vact.any()

    data = (np.random.rand(fs*3)-0.5)*0.1
    for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
        vact = vad(data, fs, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
        assert not vact.any()
