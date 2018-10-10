
import numpy as np

from .vad import vad

def trim(data, fs, fs_vad=16000, hoplength=30, vad_mode=0, thr=0.015, return_sec=False):
    """ Voice activity detection.
    Trim leading and trailing silence from an audio signal by using vad.
    Parameters
    ----------
    data : ndarray
        numpy array of mono (1 ch) speech data.
        1-d or 2-d, if 2-d, shape must be (1, time_length) or (time_length, 1).
        if data type is int, -32768 < data < 32767.
        if data type is float, -1 < data < 1.
    fs : int
        Sampling frequency of data.
    fs_vad : int, optional
        Sampling frequency for webrtcvad.
        fs_vad must be 8000, 16000, 32000 or 48000.
        Default is 16000.
    hoplength : int, optional
        Step size[milli second].
        hoplength must be 10, 20, or 30.
        Default is 0.1.
    vad_mode : int, optional
        set vad aggressiveness.
        As vad_mode increases, it becomes more aggressive.
        vad_mode must be 0, 1, 2 or 3.
        Default is 0.

    Returns
    -------
    trimed_data : ndarray
        trimed_data. trimed input data.
        If voice activity can't be detected, return None.
    """
    vact = vad(data, fs, fs_vad, hoplength, vad_mode)
    vact_diff = np.diff(vact).astype('int')
    start_i = np.where(vact_diff == 1)[0]
    end_i =   np.where(vact_diff == -1)[0]
    if len(start_i) == 0 and  len(end_i) == 0:
        return None
    if len(start_i) < 1:
        start_i = np.hstack((end_i, 0))
    if len(end_i) < 1:
        end_i = np.hstack((end_i, len(vact)-1))
    if end_i[0] <= start_i[0]:
        start_i = np.hstack((0,start_i))
    if len(start_i) > len(end_i):
        end_i = np.hstack((end_i, len(vact)-1))
    
    thr_ind=[]
    for i, (s, e) in enumerate(zip(start_i, end_i)):
        power = np.mean(data[s:e]**2)**0.5
        if power > thr:
            thr_ind.append(i)

    if len(thr_ind) == 0:
        return None

    sec = (start_i[thr_ind[0]], end_i[thr_ind[-1]])

    if return_sec:
        return data[sec[0]:sec[1]], sec
    else:
        return data[sec[0]:sec[1]]