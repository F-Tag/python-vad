
import numpy as np

from .vad import vad


def _get_edges(vact):

    edges = np.flatnonzero(np.diff(vact.astype(int)))
    edges = edges + 1

    if vact[0]:
        edges = np.hstack((0, edges))

    if vact[-1]:
        edges = np.hstack((edges, vact.size))

    edges = np.minimum(edges, vact.size).reshape(-1, 2)
    edges = edges[(edges[:, 1] - edges[:, 0]) > 0]

    return edges


def _rms(arr):
    return np.sqrt((arr**2.0).mean())


def _drop_silence(waveform, edges, threshold_db):

    rms = []
    for s, e in edges:
        rms.append(_rms(waveform[s:e]))

    rms = 20 * np.log10(rms)

    return edges[rms >= threshold_db]


def _merge_short_silence(edges, max_samples):
    if len(edges) == 0:
        return edges

    ret = [edges[0].tolist()]
    for s, e in edges[1:]:
        if s - ret[-1][-1] < max_samples:
            ret[-1][-1] = e
        else:
            ret.append([s, e])

    return np.asarray(ret)


def trim(data, fs, fs_vad=16000,
         hop_length=30, vad_mode=0,
         threshold_db=-35.0, min_dur=0.2):
    """
    Trim leading and trailing silence from an speech waveform by using vad.
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
    hop_length : int, optional
        Step size[milli second].
        hop_length must be 10, 20, or 30.
        Default is 0.1.
    vad_mode : int, optional
        set vad aggressiveness.
        As vad_mode increases, it becomes more aggressive.
        vad_mode must be 0, 1, 2 or 3.
        Default is 0.
    threshold_db : float, optional
        The threshold level (in dB) below reference to consider as silence.
        Default is -35.0.
    min_dur : float, optional
        The minimum duration (in seconds) of each speech segment.
        Default is 0.5.

    Returns
    -------
    (start_index, end_index) : int
        trimed waveform is data[start_index:end_index]
        If voice activity can't be detected, return 0, 0.
    """

    vact = vad(data, fs, fs_vad, hop_length, vad_mode)

    edges = _get_edges(vact)
    edges = _merge_short_silence(edges, fs*0.1)
    edges = edges[(edges[:, 1] - edges[:, 0]) > fs*min_dur]
    edges = _drop_silence(data, edges, threshold_db)

    edges = edges.ravel()

    if edges.any():
        return edges[0], edges[-1]
    else:
        return 0, 0


def split(data, fs, fs_vad=16000,
          hop_length=30, vad_mode=0,
          threshold_db=-35.0, min_dur=0.5):
    """ 
    Split a speech waveform into non-silent intervals by using vad.

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
    hop_length : int, optional
        Step size[milli second].
        hop_length must be 10, 20, or 30.
        Default is 0.1.
    vad_mode : int, optional
        Set vad aggressiveness.
        As vad_mode increases, it becomes more aggressive.
        vad_mode must be 0, 1, 2 or 3.
        Default is 0.
    threshold_db : float, optional
        The threshold level (in dB) below reference to consider as silence.
        Default is -35.0.
    min_dur : float, optional
        The minimum duration (in seconds) of each speech segment.
        Default is 0.5.

    Returns
    -------
    edges : np.ndarray, shape=(m, 2)
        `edges[i] == (start_i, end_i)` are the start and end time
        (in samples) of non-silent interval `i`.
    """

    vact = vad(data, fs, fs_vad, hop_length, vad_mode)

    edges = _get_edges(vact)
    edges = _merge_short_silence(edges, fs*0.1)
    edges = edges[(edges[:, 1] - edges[:, 0]) > fs*min_dur]
    edges = _drop_silence(data, edges, threshold_db)

    return edges
