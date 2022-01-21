import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import seaborn as sns
from matplotlib import rc
from scipy.stats import norm
from sympy import *
rc('font',**{'family':'serif','serif':['Times New Roman'], 'size':'20'})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


df_swap = pd.read_table('swapdata.dat', header=0, names=['site', 'type', 'swap', 'energy'], sep=' ')
df_vac  = pd.read_table('vacdata.dat', header=0, names=['site', 'vacancy exchange energy'], sep=' ')
ChemicalPotential = pd.DataFrame(columns=['site', 'mu1', 'mu2', 'mu3', 'mu4', 'mu5', 'VFE'])
# ---------------------------------------
E_ref = {'W': [-13.52034736],
'Nb': [-10.361288195],
'Mo': [-11.467995385],
'Ta': [-12.32091286],
'Ti': [-8.03647692],
'V':  [-9.38685391],
'Cr': [-9.979455835],
'Zr': [-8.807683205],
'Hf': [-10.25020523],
'Fe': [-8.62838345],
'Co': [-7.4161202]}
REF = pd.DataFrame(data=E_ref)
# NbMoTaHfW pristine energy
E_pristine = -1447.37646993
N = 125
C = 5
for i in range(1,N+1):
    df_sites = df_swap.loc[df_swap['site'] == i]
    df_site = df_sites.reset_index(drop=True)
    df_vacsites = df_vac.loc[df_vac['site'] == i]
    df_vacsite = df_vacsites.reset_index(drop=True)
    swapmatrix = zeros(6,7)
    swapmatrix[0, 0] = 1
    swapmatrix[0, df_site['type'][0]] = -1
    swapmatrix[0, 6] = df_vacsite['vacancy exchange energy'][0] - E_pristine
    for ind in df_site.index:
        swapmatrix[ind+1, df_site['type'][ind]] = -1
        swapmatrix[ind+1, df_site['swap'][ind]] = 1
        swapmatrix[ind+1, 6] = df_site['energy'][ind] - E_pristine
        swapmatrix[5, 5] = 1
        swapmatrix[5, 1] = 1
        swapmatrix[5, 2] = 1
        swapmatrix[5, 3] = 1
        swapmatrix[5, 4] = 1
        swapmatrix[5, 6] = E_pristine/(N/C)

    reduced = []
    reduced = swapmatrix.rref()
    matrix = []
    num = []
    matrix, num = reduced
    mu = []
    mu = matrix[0:6, 6]
    swapresults = []
    swapresults = pd.DataFrame([[i, mu[1], mu[2], mu[3], mu[4], mu[5], mu[0]]], columns=['site', 'mu1', 'mu2', 'mu3', 'mu4', 'mu5', 'VFE'])
    ChemicalPotential = ChemicalPotential.append(swapresults, ignore_index=True)

# --------------------------------------------------------------
Nb = ChemicalPotential['mu1'].astype(float) - REF['Nb'][0]
Mo = ChemicalPotential['mu2'].astype(float) - REF['Mo'][0]
Ta = ChemicalPotential['mu3'].astype(float) - REF['Ta'][0]
Hf = ChemicalPotential['mu4'].astype(float) - REF['Hf'][0]
W  = ChemicalPotential['mu5'].astype(float) - REF['W'][0]
mu_Va = ChemicalPotential['VFE'].astype(float)
# --------------------------------------------------------------
print(ChemicalPotential)

#axNb = sns.kdeplot(Nb, shade=True,color='blue', label='$Nb$', linewidth=3.0)
#axMo = sns.kdeplot(Mo, shade=True,color='red', label='$Mo$', linewidth=3.0)
#axTa = sns.kdeplot(Ta, shade=True,color='black', label='Ta', linewidth=3.0)
#axHf = sns.kdeplot(Hf, shade=True,color='yellow', label='Hf', linewidth=3.0)
#axW  = sns.kdeplot(W, shade=True,color='green', label='W', linewidth=3.0)
#axNb2 = sns.kdeplot(Nb, shade=True, color='blue', label='Va$\mu_{Nb}$', linewidth=3.0)#
#axMo = sns.kdeplot(Mo, shade=True, color='red', label='Va$\mu_{Mo}$', linewidth=3.0)
#axTa = sns.kdeplot(Ta, shade=True, color='black', label='Va$\mu_{Ta}$', linewidth=3.0)
#axHf = sns.kdeplot(Hf, shade=True, color='yellow', label='Va$\mu_{Hf}$', linewidth=3.0)
#axW  = sns.kdeplot(V, shade=True, color='purple', label='Va$\mu_{V}$', linewidth=3.0)
#axCr = sns.kdeplot(Cr, shade=True, color='magenta', label='Cr', linewidth=3.0)
#axMn = sns.kdeplot(Mn,shade=True, color='green', label='Mn', linewidth=3.0)
#axFe = sns.kdeplot(Fe,shade=True, color='red', label='Fe', linewidth=3.0)
#axCo = sns.kdeplot(Co,shade=True, color='blue', label='Co', linewidth=3.0)
#axNi = sns.kdeplot(Ni,shade=True, color='black', label='Ni', linewidth=3.0)
Vaplot = mu_Va.hist(bins=7)
#plt.vlines(0.0,ymin=0, ymax=28, linestyles='dashed', linewidth=4.0)

#plt.xlabel('$\Delta \mu^{\mathrm mix}$ [eV/atom]')
plt.xlabel('$E_{\mathrm v}^f$')
plt.ylabel('Counts')
plt.title('NbMoTaHfW 125 atom SQS, PBEsol functional')

plt.legend()
#plt.show()

