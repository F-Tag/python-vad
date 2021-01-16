#!/usr/bin/env python

from setuptools import setup


setup_requires = []
install_requires = [
    'numpy',
    'librosa',
    'webrtcvad'
]

tests_requires = [
    'mock',
    'nose']


setup(
    name='pyvad',
    version='0.1.2',
    description='py-webrtcvad wrapper for trimming speech clips',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Fumiaki Taguchi',
    author_email='fumiaki.taguchi@gmail.com',
    url='https://github.com/F-Tag/python-vad',
    license='MIT License',
    packages=['pyvad'],
    zip_safe=False,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)
