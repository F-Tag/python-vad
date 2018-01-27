# [py-webrtcvad](https://github.com/wiseman/py-webrtcvad) wrapper for Easy to use of Voice activity detection in python
[![Build Status](https://travis-ci.org/F-Tag/python-vad.svg?branch=master)](https://travis-ci.org/F-Tag/python-vad)

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

via sorce
```sh
$ git clone https://github.com/F-Tag/python-vad.git
$ cd python-vad
$ python setup.py install
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
