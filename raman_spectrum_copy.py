"Fichier qui implémente la classe d'objets raman_spectum qui sert à analyser les spectres raman"
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from scipy import stats, interpolate
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

    def codeDan(self):
        px = [625, 882, 1134, 1149]
        nm = [671, 690, 708, 709]

        slope, intercept, r_value, p_value, std_err = stats.linregress(px, nm)
        print(f"a={slope:.5f}", f"b={intercept:.3f}",f"σ={std_err:.3e}")

        x_new = np.array(range(1339))
        nm = x_new*slope+intercept

        cm = 1/(632.8e-7) - 1/(nm*1e-7)
        i=0

        # Spectre
        for file in glob.glob(self.name):
            soln = file.split("_")[2]
            df = pd.read_csv(file)
            y = df.iloc[:, 2]
            y = y / max(abs(y))
            #plt.plot(nm, y, label=f"{soln}", linewidth=0.5)

        #plt.xlabel("$\lambda$ [nm]")
        #plt.ylabel("Intensité relative [-]")
        #plt.legend(loc="upper center", ncol=5, bbox_to_anchor=(0.5, 1.1))
        #plt.savefig("Spectre_huiles.png")
        #plt.show()
        #plt.clf()


        for file in glob.glob(self.name):
            soln = file.split("_")[2]
            print(soln)
            df = pd.read_csv(file)
            y = df.iloc[:, 2]
            # plt.plot(cm, y, label=f"{soln}", linewidth=0.5) # Spectre
            d = 25
            f2 = interpolate.interp1d(cm[200:][::d], y[200:][::d], kind='quadratic')
            y = y[200:1200]-f2(cm[200:1200])
            # y = y / max(y)
            mask_1444 = (cm[200:1200] > 1400) & (cm[200:1200] < 1500)
            mask_1661 = (cm[200:1200] > 1600) & (cm[200:1200] < 1700)
            I_1444 = max(y[mask_1444])
            I_1661 = max(y[mask_1661])
            # plt.plot(cm[200:1200], f2(cm[200:1200]), label=f"{soln}", linewidth=0.5) # Background
            # plt.plot(cm[200:1200], y+2*i, label=f"{soln}", linewidth=0.5)
            print(f"r: {I_1444/I_1661*100:.2f}%")
            i += 1

        self.data_Dan = np.array([cm[200:1200], y]).T

        #plt.xlabel("ν [1/cm]")
        #plt.ylabel("Intensité relative [-]")
        #plt.legend(loc="upper center", ncol=i, bbox_to_anchor=(0.5, 1.1))
        #plt.savefig("Raman_huiles.png")
        #plt.show()
        #plt.clf()

    def getDanPeaks(self):
        self.codeDan()
        promi = self.promi
        ens_ini = list(zip(self.data_Dan[:, 0], self.data_Dan[:, 1]))
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

