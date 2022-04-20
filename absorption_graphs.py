import numpy as np
import matplotlib.pyplot as plt
from absorption import Absorption


vide = Absorption("Absorption\/vide_ref.txt")
rhum_brun = Absorption("Absorption\/rhum_brun_USB2G573481_001.txt")
rhum_blanc = Absorption("Absorption\Bacardi_USB2G573481_001.txt")
absolut = Absorption("Absorption\Absolut_USB2G573481_001.txt")
smirnoff = Absorption("Absorption\smirnoff_USB2G573481_001.txt")

# rhum_brun_abs = np.array(vide.intensity) - np.array(rhum_brun.intensity[:-1])
# rhum_blanc_abs = np.array(vide.intensity) - np.array(rhum_blanc.intensity[:-1])
# smirnoff_abs = np.array(vide.intensity) - np.array(absolut.intensity[:-1])
# absolut_abs = np.array(vide.intensity) - np.array(smirnoff.intensity[:-1])

vide.graph("Faisceau incident")
rhum_brun.graph("Rhum brun")
rhum_blanc.graph("Rhum blanc")
absolut.graph("Vodka Absolut")
smirnoff.graph("Vodka Smirnoff")
plt.xlim(400, 800)
plt.ylabel("Nombre de photons")
plt.xlabel("Longueur d'onde [nm]")
plt.legend()
plt.show()


# plt.plot(vide.long, rhum_brun_abs)
# plt.plot(vide.long, rhum_blanc_abs)
# plt.plot(vide.long, smirnoff_abs)
# plt.plot(vide.long, absolut_abs)
# plt.xlim(400, 800)
# plt.ylabel("Nombre de photons absorbés")
# plt.xlabel("Longueur d'onde [nm]")
# plt.legend()
# plt.show()