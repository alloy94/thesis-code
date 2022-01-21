import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import seaborn as sns
from matplotlib import rc
from scipy.stats import norm
rc('font',**{'family':'serif','serif':['Times New Roman'], 'size':'16'})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


x = np.linspace(-2.0, 2)


Zr = np.loadtxt('Delta_mu_mix_Zr.dat', delimiter=',')
Nb = np.loadtxt('Delta_mu_mix_Nb.dat', delimiter=',')
Ti = np.loadtxt('Delta_mu_mix_Ti.dat', delimiter=',')
Ta = np.loadtxt('Delta_mu_mix_Ta.dat', delimiter=',')
Mo = np.loadtxt('Delta_mu_mix_Mo.dat', delimiter=',')

#plt.hist(Cr, bins=5, density=True, alpha=0.5, color='magenta')
#plt.hist(Mn, bins=5, density=True, alpha=0.5, color='green')
#plt.hist(Fe, bins=5, density=True, alpha=0.5, color='red')
#plt.hist(Co, bins=5, density=True, alpha=0.5, color='blue')
#plt.hist(Ni, bins=5, density=True, alpha=0.5, color='black')

#plt.plot(x, Ti_pdf, color='green', label='Va$_{Ti}$')
#axNb  = sns.kdeplot(Nb, shade=True, color='blue', label='Va$_{Nb}$', linewidth=3.0)#
#axMo = sns.kdeplot(Mo, shade=True, color='red', label='Va$_{Mo}$', linewidth=3.0)
#axTa = sns.kdeplot(Ta, shade=True, color='black', label='Va$_{Ta}$', linewidth=3.0)
#axHf = sns.kdeplot(Hf, shade=True, color='yellow', label='Va$_{Hf}$', linewidth=3.0)
#axV  =sns.kdeplot(V, shade=True, color='purple', label='Va$_{V}$', linewidth=3.0)
axZr = sns.kdeplot(Zr, shade=True, color='green', label='Zr', linewidth=3.0)
axNb = sns.kdeplot(Nb, shade=True, color='blue', label='Nb', linewidth=3.0)
axTi = sns.kdeplot(Ti,shade=True, color='red', label='Ti', linewidth=3.0)
axTa = sns.kdeplot(Ta,shade=True, color='purple', label='Ta', linewidth=3.0)
axMo = sns.kdeplot(Mo,shade=True, color='magenta', label='Mo', linewidth=3.0)

plt.vlines(0.0,ymin=0, ymax=8, linestyles='dashed')

#axZr = sns.kdeplot(Zr, shade=True, color='green', label='Va$_{Zr}$', linewidth=3.0)
#axW = sns.kdeplot(W, shade=True, color='orange', label='Va$_{W}$', linewidth=3.0)
plt.ylabel('Counts [a.u.]')
plt.xlabel('$\Delta \mu^{\mathrm{mix}}$ [eV/atom]')
plt.title('Refractory HEA NbMoTaTiZr 30 atom BCC SQS')
plt.xlim(-0.8, 0.2)
plt.legend()
plt.show()
#plt.hist(W, [5.0, 5.25, 5.5, 5.75, 6.0, 6.25], facecolor='green', alpha=0.2)
#plt.show()
