# spin-analysis-py-snte

This repository contains Python scripts developed during my undergraduate thesis in Physics at UFRN. The goal was to analyze impedance measurements from magnetic thin film samples using contour plots and interpolation techniques.

## 🧪 Project Overview

The samples studied were based on Py/Ag and Py/SnTe multilayers, with data obtained from experimental setups. The scripts focus on:

- **Contour plots of real part of impedance (ΔZ)** as a function of magnetic field (H) and frequency (ω)
- **Comparison of two samples** (Py/Ag vs. Py/SnTe)
- **Data interpolation** using `scipy.interpolate.griddata`

## 📊 Visualizations

### 1. Density Plot of ΔZ vs. Field and Frequency

The script generates smooth 2D contour plots showing the behavior of the real part of the impedance (ΔZ) for each sample.

| Py/Ag Sample | Py/SnTe Sample |
|-------------|----------------|
| ![PyAg plot](img/pyag.png) | ![PySnTe plot](img/pysnte.png) |

### 2. Real and Imaginary Part vs. Magnetic Field

Plots showing how the real and imaginary components of the impedance vary with the magnetic field for selected frequencies.


## 🛠️ Technologies

- **Python 3.10+**
- `pandas`
- `numpy`
- `matplotlib`
- `scipy`

## 📁 File Structure

```
├── data/              # Raw experimental data 
├── notebooks/         # Jupyter Notebooks with full analysis
├── img/               # Output figures
├── README.md
```

## 🚀 Getting Started

1. Clone the repository  
2. Install requirements:  
   ```bash
   pip install pandas matplotlib scipy numpy
   ```
3. Run the notebook or Python script

## 📌 Notes

- Due to confidentiality reasons, the original data used in this project is not available. However, the analysis scripts are fully functional and structured to work with similarly formatted data.
- The 3D plotting code was exploratory and is not the focus of this repository.

## 👩‍🔬 Author

**Amannda Laura**  
[LinkedIn](https://www.linkedin.com/in/amanndalaura) • [GitHub](https://github.com/lauraspin)
