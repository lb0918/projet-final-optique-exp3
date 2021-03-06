import numpy as np
import matplotlib.pyplot as plt
from raman_spectrum_copy import RamanSpectrum

class Absorption():
    def __init__(self, file):
        fich = open(file)
        self.intensity = []
        self.long = []
        for i in fich.readlines()[1: -1]:
            l = float(i[0: -2].split('\t')[0])
            self.long.append(l)
            int = float(i[0: -2].split('\t')[1])
            self.intensity.append(int)

    def graph(self):
        plt.plot(self.long, self.intensity)

vide = Absorption("Absorption/vide_ref.txt")
vide_raman = RamanSpectrum("Absorption/vide_ref2_1_1.txt", 1800)

alex = Absorption("Absorption/alex.txt")
alex_raman = RamanSpectrum("Absorption/alex2_1_1.txt", 1800)

anne = Absorption("Absorption/anne.txt")
anne_raman = RamanSpectrum("Absorption/anne2_1_1.txt", 1800)

jay = Absorption("Absorption/jay.txt")

momo = Absorption("Absorption/jay.txt")


saydou = Absorption("Absorption/saydou.txt")
saydou.graph()
vide.graph()
momo.graph()
jay.graph()
anne.graph()
alex.graph()
plt.title('Absorption de différents alcools en fonction de leur opacité')
plt.xlabel('''Longueur d'ondes [nm]''')
plt.ylabel('Counts')
plt.show()

vide_data = vide_raman.codeDan()
anne_data = anne_raman.codeDan()
alex_data = alex_raman.codeDan()

plt.plot(vide_data, label='vide')
plt.plot(anne_data, label='anne')
plt.plot(alex_data, label='alex')
plt.legend()
plt.xlim([350,450])
plt.show()