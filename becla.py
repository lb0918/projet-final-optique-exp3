import numpy as np
import matplotlib.pyplot as plt
from raman_spectrum_copy import RamanSpectrum


eth25 = RamanSpectrum("Mesures bonnes\eth_251_1.txt", 1800)
eth50 = RamanSpectrum("Mesures bonnes\eth_501_1.txt", 1800)
eth75 = RamanSpectrum("Mesures bonnes\eth_751_1.txt", 1800)
eth100 = RamanSpectrum("Mesures bonnes\eth_1001_1.txt", 1800)
eth25.graph_zero()
eth50.graph_zero()
eth75.graph_zero()
eth100.graph_zero()
plt.show()

peaks25 = eth25.getDanPeaks()
peaks50 = eth50.getDanPeaks()
peaks75 = eth75.getDanPeaks()
peaks100 = eth100.getDanPeaks()

danpeaks25 = eth25.codeDan()
danpeaks50 = eth50.codeDan()
danpeaks75 = eth75.codeDan()
danpeaks100 = eth100.codeDan()

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

# plt.plot(alco, bons_peaks)
# plt.show()

pente, valinit = np.polyfit(alco, bons_peaks, 1)

def courbe_theo(x, m, b):
    return x*m + b

rhum_blanc = RamanSpectrum("Mesures bonnes\/rhum_blanc1_1.txt", 1800)
rhum_brun =  RamanSpectrum("Mesures bonnes/rhum_brun1_1.txt", 1800)
abso_vodk = RamanSpectrum("Mesures bonnes/absolut11_1_abso.txt", 1800)
smir_vodk = RamanSpectrum("Mesures bonnes\smirnoff1_1_smir.txt", 1800)
good_alc = RamanSpectrum("Mesures bonnes\good_alcool1_1.txt", 1800)
bad_alc = RamanSpectrum("Mesures bonnes/bad_alcool1_1.txt", 1800)
abso_vodk.graph_zero()
plt.show()

for i in rhum_blanc.getDanPeaks():
    if 840 < i[0] < 850:
        rhum_blanc_peak = i[1]

for i in rhum_brun.getDanPeaks():
    if 840 < i[0] < 850:
        rhum_brun_peak = i[1]

for i in abso_vodk.getDanPeaks():
    if 840 < i[0] < 850:
        abso_vodk_peak = i[1]

for i in smir_vodk.getDanPeaks():
    if 840 < i[0] < 850:
        smir_vodk_peak = i[1]

for i in good_alc.getDanPeaks():
    if 840 < i[0] < 850:
        good_alc_peak = i[1]

for i in bad_alc.getDanPeaks():
    if 840 < i[0] < 850:
        bad_alc_peak = i[1]


print((rhum_blanc_peak-valinit)/pente)
abso_vodk_true = (abso_vodk_peak-valinit)/pente
abso_vodk_theo = 40
smir_vodk_true = (smir_vodk_peak-valinit)/pente
smir_vodk_theo = 40
x_rhum_blanc_true = (rhum_blanc_peak-valinit)/pente
x_rhum_blanc_theo = 40
x_rhum_brun_true = (rhum_brun_peak-valinit)/pente
x_rhum_brun_theo = 40
x_good_alc_true = (good_alc_peak-valinit)/pente
x_good_alc_theo = 93
x_bad_alc_true = (bad_alc_peak-valinit)/pente
x_bad_alc_theo = 93
liste_theo = [x_good_alc_theo, x_bad_alc_theo, x_rhum_blanc_theo, x_rhum_brun_theo]
fig, ax = plt.subplots(2)
x_ = np.linspace(0, 100, 1000)
ax[0].plot(x_, courbe_theo(x_, pente, valinit), '--r')
ax[0].plot(alco, bons_peaks, 'Dr',label = '''Points d'ethanol''')
ax[0].plot(abso_vodk_true, abso_vodk_peak, 'o', color = 'black', label = 'Abso Vodk')
ax[0].plot(smir_vodk_theo, smir_vodk_peak, 'v', color = 'black')
ax[0].plot(smir_vodk_true, smir_vodk_peak, 'o', color = 'pink', label = 'Smir Vodk')
ax[0].plot(abso_vodk_theo, abso_vodk_peak, 'v', color = 'pink')
ax[0].plot(x_rhum_blanc_true, rhum_blanc_peak, 'o', color = 'red', label = 'Rhum blanc')
ax[0].plot(x_rhum_blanc_theo, rhum_blanc_peak, 'v', color = 'red')
ax[0].plot(x_rhum_brun_true, rhum_brun_peak, 'o', color = 'green', label = 'Rhum brun')
ax[0].plot(x_rhum_brun_theo, rhum_brun_peak, 'v', color = 'green')
ax[0].plot(x_good_alc_true, good_alc_peak, 'o', color = 'purple', label = 'Alcool artisanal bon')
ax[0].plot(x_good_alc_theo, good_alc_peak, 'v', color = 'purple')
ax[0].plot(x_bad_alc_true, bad_alc_peak, 'o', color = 'blue', label = 'Alcool artisanal mauvais')
ax[0].plot(x_bad_alc_theo, bad_alc_peak, 'v', color = 'blue')
ax[0].set_xlabel('''Pourcentage d'alcool''')
ax[0].set_ylabel('Nombre de photons')
ax[0].legend()
for xc in liste_theo:
    ax[0].axvline(x=xc, linestyle='--')
ax[1].plot(danpeaks25, label='25')
ax[1].plot(danpeaks50, label='50')
ax[1].plot(danpeaks75, label= '75')
ax[1].plot(danpeaks100, label='100')
ax[1].set_xlim([350,450])
ax[1].set_ylim([0,40000])
ax[1].legend()
plt.show()
print(len(liste_theo))
