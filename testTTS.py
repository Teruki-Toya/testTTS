# -*- coding: utf-8 -*-
"""
Python によるTTSのテスト
Created on Sat. Feb. 07, 2026.

@author: Teruki Toya, University of Yamanashi
"""
# %%
import sounddevice as sd
import soundfile as sf
import numpy as np
import pyopenjtalk

text = "当研究室は、音に興味がある人なら、間違いなく楽しめます。いま音に興味がなくても、配属後に基礎知識、技能を身に着けることができます。当研究室の活動を通じて、高いプレゼン能力が身に付きます。当研究室の卒研生は、2024年度・2025年度と、2年連続で、卒論発表会の優秀発表賞を受賞しています。先輩、同級生とコミュニケーションをとり、皆さんの理想とする研究室の雰囲気を作り上げてください。人生の転機となる1年間となることを祈ります。"
x, fs = pyopenjtalk.tts(text)
x = 0.45 * (x / np.max(np.abs(x)))

sd.play(x, fs)
sf.write('p18.wav', x, fs)
# %%
