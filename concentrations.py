import numpy as np
import matplotlib.pyplot as plt
from becla import *


#plt.plot(alco, bons_peaks, label = '''Courbe théorique de l'éthanol''')
plt.plot(x, projection, "--", label = '''Concentrations affichées''')
plt.plot(x, projection, "--", color="black", label = '''Régression linéaire''')
plt.plot(abso_vodk_true, abso_vodk_peak, 'o', color = 'black', label = 'Vodka Absolut')
#plt.plot(smir_vodk_theo, smir_vodk_peak, 'v', color = 'pink')
plt.plot(smir_vodk_true, smir_vodk_peak, 'o', color = 'pink', label = 'Vodka Smirnoff')
#plt.plot(abso_vodk_theo, abso_vodk_peak, 'v', color = 'black')
plt.plot(x_rhum_blanc_true, rhum_blanc_peak, 'o', color = 'red', label = 'Rhum blanc Baccardi')
#plt.plot(x_rhum_blanc_theo, rhum_blanc_peak, 'v', color = 'red')
plt.plot(x_rhum_brun_true, rhum_brun_peak, 'o', color = 'green', label = 'Rhum brun Havana Club')
#plt.plot(x_rhum_brun_theo, rhum_brun_peak, 'v', color = 'green')
plt.plot(x_good_alc_true, good_alc_peak, 'o', color = 'purple', label = 'Alcool artisanal 93 %')
#plt.plot(x_good_alc_theo, good_alc_peak, 'v', color = 'purple')
#plt.plot(x_bad_alc_true, bad_alc_peak, 'o', color = 'blue', label = 'Alcool artisanal mauvais')
#plt.plot(x_bad_alc_theo, bad_alc_peak, 'v', color = 'blue')
plt.xlabel('''Pourcentage d'alcool''')
plt.ylabel('Nombre de photons')
plt.legend()
for xc in liste_theo:
    plt.axvline(x=xc, linestyle = '--')
plt.show()
