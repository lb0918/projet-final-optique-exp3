import numpy as np
import matplotlib.pyplot as plt
from absorption_graphs import vide, rhum_brun, rhum_blanc, smirnoff, absolut


vide_m = np.mean(vide.intensity[279:286])
rhumbrun_m = np.mean(rhum_brun.intensity[279:286])
rhumblanc_m = np.mean(rhum_blanc.intensity[279:286])
smirnoff_m = np.mean(smirnoff.intensity[279:286])
absolut_m = np.mean(absolut.intensity[279:286])

print("vide", vide_m, "rhumbr", rhumbrun_m, "rhumbl", rhumblanc_m, "smirn", smirnoff_m, "abso", absolut_m)
