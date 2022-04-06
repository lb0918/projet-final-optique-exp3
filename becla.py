import numpy as np
import matplotlib.pyplot as plt
from raman_spectrum_copy import RamanSpectrum


eth25 = RamanSpectrum("Mesures bonnes\eth_251_1.txt", 1800)
eth50 = RamanSpectrum("Mesures bonnes\eth_501_1.txt", 1800)
eth75 = RamanSpectrum("Mesures bonnes\eth_751_1.txt", 1800)
eth100 = RamanSpectrum("Mesures bonnes\eth_1001_1.txt", 1800)

peaks25 = eth25.getDanPeaks()
peaks50 = eth50.getDanPeaks()
peaks75 = eth75.getDanPeaks()
peaks100 = eth100.getDanPeaks()

bons_peaks = []
alco = [25, 50, 75, 100]

for i in peaks25:
    if 840 < i[0] < 850:
        bons_peaks.append(i[1])

for i in peaks50:
    if 840 < i[0] < 850:
        bons_peaks.append(i[1])

for i in peaks75:
    if 840 < i[0] < 850:
        bons_peaks.append(i[1])

for i in peaks100:
    if 840 < i[0] < 850:
        bons_peaks.append(i[1])

plt.plot(alco, bons_peaks)
plt.show()