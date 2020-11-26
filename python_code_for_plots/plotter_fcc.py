import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 30}

mlt.rc('font', **font)
plt.style.use("ggplot")
data = np.genfromtxt("Co.dos",usecols = (0,1,2))
x = 200
plt.plot(data[x:,0]-18.6664 ,data[x:,1],color = "r",linestyle = "--",label = "Spin up")
plt.plot(data[x:,0]-18.6664 ,-data[x:,2],color = "b", linestyle = "--", label = "Spin down")
plt.plot(np.zeros((100)) ,np.linspace(-2.5,2.5,100),color = "k", linestyle = "--", label = "Fermi energy")

plt.xlabel("Energy (eV)",fontweight = "bold")
plt.ylabel("Density of States (1/eV)",fontweight = "bold")
plt.title("DOS - Cobalt fcc ",fontweight = "bold")
plt.grid(True)
plt.tight_layout()
plt.legend()

plt.show()
