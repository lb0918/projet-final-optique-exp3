import numpy as np
import matplotlib.pyplot as plt
from becla import *
from transmission_calculs import vide_m, rhumbrun_m, rhumblanc_m, smirnoff_m, absolut_m

print("abso:", abso_vodk_true, abso_vodk_peak)
print("rbrun:", x_rhum_brun_true, rhum_brun_peak,)
print("smirn:", smir_vodk_true, smir_vodk_peak)
print("rblanc:", x_rhum_blanc_true, rhum_blanc_peak)
print("artis:", x_good_alc_true, good_alc_peak)


### CORRECTION ABSORPTION ###
abso_count = abso_vodk_peak * vide_m / absolut_m
smirn_count = smir_vodk_peak * vide_m / smirnoff_m
rbrun_count = rhum_brun_peak * vide_m / rhumbrun_m
rblanc_count = rhum_blanc_peak * vide_m / rhumblanc_m

print("abso peak norm:", abso_vodk_true, abso_vodk_peak)
print("rbrun peak norm:", x_rhum_brun_true, rhum_brun_peak,)
print("smirn peak norm:", smir_vodk_true, smir_vodk_peak)
print("rblanc peak norm:", x_rhum_blanc_true, rhum_blanc_peak)

# Pourcentage d'alcool
abso_norm = (abso_count-valinit)/pente
smirn_norm = (smirn_count-valinit)/pente
rbrun_norm = (rbrun_count-valinit)/pente
rblanc_norm = (rblanc_count-valinit)/pente

print("abso norm:", abso_norm)
print("rbrun norm:", rbrun_norm)
print("smirn norm:", smirn_norm)
print("rblanc norm:", rblanc_norm)


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
