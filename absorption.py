import numpy as np
import matplotlib.pyplot as plt
from raman_spectrum_copy import RamanSpectrum

class Absorption():
    def __init__(self, file):
        fich = open(file)
        self.intensity = []
        self.long = []
        if file[-7:-4] == "001":
            for i in fich.readlines()[: -1]:
                l = float(i[0: -1].split('\t')[0])
                self.long.append(l)
                int = float(i[0: -1].split('\t')[1])
                self.intensity.append(int)
        else:
            for i in fich.readlines()[1: -1]:
                l = float(i[0: -2].split('\t')[0])
                self.long.append(l)
                int = float(i[0: -2].split('\t')[1])
                self.intensity.append(int)

    def graph(self, label):
        plt.plot(self.long, self.intensity, label=label)

# vide = Absorption("Absorption/vide_ref.txt")
# vide_raman = RamanSpectrum("Absorption/vide_ref2_1_1.txt", 1800)

# alex = Absorption("Absorption/alex.txt")
# alex_raman = RamanSpectrum("Absorption/alex2_1_1.txt", 1800)

# anne = Absorption("Absorption/anne.txt")
# anne_raman = RamanSpectrum("Absorption/anne2_1_1.txt", 1800)

# jay = Absorption("Absorption/jay.txt")

# momo = Absorption("Absorption/jay.txt")


# saydou = Absorption("Absorption/saydou.txt")
# saydou.graph()
# vide.graph()
# momo.graph()
# jay.graph()
# anne.graph()
# alex.graph()
# plt.title('Absorption de différents alcools en fonction de leur opacité')
# plt.xlabel('''Longueur d'ondes [nm]''')
# plt.ylabel('Counts')
# plt.show()

# vide_data = vide_raman.codeDan()
# anne_data = anne_raman.codeDan()
# alex_data = alex_raman.codeDan()

# plt.plot(vide_data[0], vide_data[1], label='vide')
# plt.plot(vide_data[0], vide_data[1], label='anne')
# plt.plot(vide_data[0], vide_data[1], label='alex')
# plt.legend()
# plt.xlim([820, 860])
# plt.show()