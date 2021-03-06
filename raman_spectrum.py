"Fichier qui implémente la classe d'objets raman_spectum qui sert à analyser les spectres raman"
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


class RamanSpectrum:
    def __init__(self, fich, promi):
        # self.data = np.genfromtxt(fich, delimiter='     ')
        self.data = np.genfromtxt(fich, delimiter=',')
        self.raman = self.data[:, 0]
        self.counts = self.data[:, 2]
        self.promi = int(promi)
        self.peaks = self.getPeaks()
        self.name = fich

    def graph(self, peaks=False):
        plt.plot(self.raman, self.counts, label=f'{self.name}')
        if peaks:
            for x in self.peaks:
                plt.plot(x[0], x[1], 'o', color='red')
                plt.text(x[0], x[1] + 0.5, '({}, {})'.format(x[0], x[1]))
        plt.legend()
        plt.xlabel('Raman shift')
        plt.ylabel('Counts')
    def graph_zero(self, peaks=False):
        liste = list(zip(self.raman, self.counts))
        raman = []
        counts = []
        for x in liste:
            if x[0] >= 0:
                raman.append(x[0])
                counts.append(x[1])
        plt.plot(raman, counts, label=f'{self.name}')
        if peaks:
            for x in self.peaks:
                plt.plot(x[0], x[1], 'o', color='red')
                plt.text(x[0], x[1] + 0.5, '({}, {})'.format(x[0], x[1]))
                plt.legend()
                plt.xlabel('Raman shift')
                plt.ylabel('Counts')


    def getPeaks(self):
        promi = self.promi
        ens_ini = list(zip(self.data[:, 0], self.data[:, 2]))
        raman = []
        counts = []
        for x in ens_ini:
            if x[0] >= 0:
                raman.append(x[0])
                counts.append(x[1])
        raman, counts = np.array(raman), np.array(counts)
        ens_fin = list(zip(raman, counts))
        points_maxi = []
        b = find_peaks(counts, prominence=promi)
        for x in b[0]:
            points_maxi.append(ens_fin[int(x)])
        return points_maxi

    def red_fluo(self):
        raman = []
        counts = []
        liste = list(zip(self.raman, self.counts))
        for x in liste:
            if x[0] > 0 :
                raman.append(x[0])
                counts.append(x[1])
        raman = np.array(raman)
        counts = np.array(counts)
        fit = np.polyfit(raman, counts, 60)
        print(fit)
        val = np.polyval(fit, raman)
        plt.plot(raman, counts-val)
        plt.show()
    
    # def pic_pourc(self):


iso50 = RamanSpectrum("Vrai\iso_50_100s6.TXT", 10000)
iso75 = RamanSpectrum('Vrai\iso_75_100s5.TXT', 10000)
iso25 = RamanSpectrum('Vrai\iso_25_100s5.TXT', 10000)
iso100 = RamanSpectrum('Vrai\iso_100_100s5.TXT', 10000)
eau = RamanSpectrum('Vrai\eau_dist_robinet2.TXT', 10000)
meth = RamanSpectrum('meth.TXT', 10000)
absolut = RamanSpectrum('Mesures bonnes/absolut11_1.txt', 1000)
rhum_brun = RamanSpectrum('Mesures bonnes/rhum_brun1_1.txt', 1000)
coors = RamanSpectrum('Mesures bonnes\coors3_1.txt', 10000)
eth25 = RamanSpectrum('Mesures bonnes\eth_251_1.txt', 10000)
eth50 = RamanSpectrum('Mesures bonnes\eth_501_1.txt', 10000)
eth75 = RamanSpectrum('Mesures bonnes\eth_752_1.txt', 10000)
eth100 = RamanSpectrum('Mesures bonnes\eth_1001_1.txt', 10000)
# iso50.graph_zero(peaks=True)
# iso75.graph_zero(peaks=True)
# iso25.graph_zero(peaks=True)
# iso100.graph_zero(peaks=True)
# eau.graph_zero(peaks=True)
# meth.graph_zero(peaks=True)
# Hg.graph_zero(peaks=True)
# rhum_brun.graph_zero(peaks=True)
# absolut.graph_zero(peaks=True)
# coors.graph_zero(peaks=True)
eth25.graph_zero(peaks=True)
eth50.graph_zero(peaks=True)
eth75.graph_zero(peaks=True)
eth100.graph_zero(peaks=True)
plt.show()
# rhum_brun.red_fluo()
coors.red_fluo()
plt.show()
