# Gráfico de densidade da parte real do delta Z
# Py/Ag vs Py/SnTe
'''For those who want to copy and paste the code.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Leitura dos dados
a = pd.read_table('data/PyAgAg_vid.txt', names=['H', 'F', 'dR', 'dIm', 'Z'])
b = pd.read_table('data/PySnTeAg_vid.txt', names=['H', 'F', 'dR', 'dIm', 'Z'])

# Extração das colunas
H = a['H']
F = a['F'] / 1e9  # Frequência em GHz
R = a['dR']
Rb = b['dR']

# Grade para interpolação
H_grid = np.linspace(H.min(), H.max(), 300)
F_grid = np.linspace(F.min(), F.max(), 300)
H_mesh, F_mesh = np.meshgrid(H_grid, F_grid)

# Interpolação dos dados
Z_grid = griddata((H, F), R, (H_mesh, F_mesh), method='cubic')
Zb_grid = griddata((H, F), Rb, (H_mesh, F_mesh), method='cubic')

# Plotagem
plt.figure(figsize=(6, 6))

# Py/Ag
plt.subplot(2, 1, 1)
cp = plt.contourf(H_mesh, F_mesh, Z_grid, levels=100, cmap='plasma')
cbar = plt.colorbar(cp)
cbar.set_label(r'$\Delta Z (\Omega)$')
plt.text(-280, 2.6, "(a)", fontsize=14, color="white")
plt.text(-280, 0.6, "Py/Ag", fontsize=12, color="white")
cbar.set_ticks([0.8, 0.6, 0.4, 0.2, 0.0])
plt.ylabel(r'$\omega$ (GHz)')
plt.xlim(-310, 310)
plt.ylim(0.45, 3.02)
plt.xticks([])
plt.yticks(fontsize=12)

# Py/SnTe
plt.subplot(2, 1, 2)
cp = plt.contourf(H_mesh, F_mesh, Zb_grid, levels=100, cmap='plasma')
cbar = plt.colorbar(cp)
cbar.set_label(r'$\Delta Z (\Omega)$')
plt.text(-280, 2.6, "(b)", fontsize=14, color="white")
plt.text(-280, 0.6, "Py/SnTe", fontsize=12, color="white")
cbar.set_ticks([1.00, 0.75, 0.50, 0.25, 0.0])
plt.ylabel(r'$\omega$ (GHz)')
plt.xlim(-310, 310)
plt.ylim(0.45, 3.02)
plt.xticks([])
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
