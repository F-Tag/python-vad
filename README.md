# [py-webrtcvad](https://github.com/wiseman/py-webrtcvad) wrapper for trimming speech clips
[![Build Status](https://travis-ci.org/F-Tag/python-vad.svg?branch=master)](https://travis-ci.org/F-Tag/python-vad)
[![PyPI version](https://badge.fury.io/py/pyvad.svg)](https://badge.fury.io/py/pyvad)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyvad.svg)](https://pypi.org/project/pyvad/)

## Requirement
[numpy](https://github.com/numpy/numpy), 
[librosa](https://github.com/librosa/librosa) and 
[py-webrtcvad](https://github.com/wiseman/py-webrtcvad).

## Installation
via pip
```sh
$ pip install pyvad
```

or

from github repository
```sh
$ pip install git+https://github.com/F-Tag/python-vad.git
```

## Usage
```python
from pyvad import vad
vact = vad(speech_data, speech_data_fs)
```


## Example
Please see `example.ipynb` jupyter notebook.

## License
MIT License (see `LICENSE` file).
