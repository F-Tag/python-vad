#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

import numpy as np
from pyvad import split

from util import fs_vads, hops, vad_modes, load_sp, load_noise

sp, fs_sp = load_sp()
ns ,fs_ns = load_noise()




for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = split(sp, fs_sp, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact.size >= 0, vact

for fs_vad, hop, vad_mode in product(fs_vads, hops, vad_modes):
    vact = split(ns, fs_ns, fs_vad=fs_vad, hop_length=hop, vad_mode=vad_mode)
    assert vact.size == 0, vact
