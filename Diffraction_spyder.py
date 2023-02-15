import Dans_Diffraction as dif
import matplotlib.pyplot as plt
import numpy as np

xtl = dif.Crystal('structures/NiTiH12_Ti_ISIF2.cif')
xtl.info() # print Crystal structure parameters

# Choose scattering options (see help(xtl.Scatter.setup_scatter))
xtl.Scatter.setup_scatter(scattering_type="x-ray", energy_kev=8.0)
# Allowed radiation types:
#    'xray','neutron','xray magnetic','neutron magnetic','xray resonant'
xtl.Scatter.intensity([0,0,1]) # Returns intensity
#xtl.Scatter.print_all_refelctions() # Returns formated string of all allowed reflections
# Plot Experimental Intensities
xtl.Plot.simulate_hk0()
plt.clim(0,10)
plt.show()

