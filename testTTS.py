# -*- coding: utf-8 -*-
"""
Python によるTTSのテスト
Created on Sat. Feb. 07, 2026.

@author: Teruki Toya, University of Yamanashi
"""
# %%
import sounddevice as sd
import numpy as np
import pyopenjtalk

text = "小澤・トヤ研究室の研究紹介です。"
x, fs = pyopenjtalk.tts(text)
x = 0.45 * (x / np.max(np.abs(x)))

sd.play(x, fs)
# %%
