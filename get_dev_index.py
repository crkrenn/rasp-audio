#!/usr/bin/env python3
"""
code to identify usb `dev_index` 

Hrisko, J. (2018). Recording Audio on the Raspberry Pi with Python and
    a USB Microphone. Maker Portal. 
    https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
"""

import pyaudio
p = pyaudio.PyAudio()
for ii in range(p.get_device_count()):
    print(p.get_device_info_by_index(ii).get('name'))

