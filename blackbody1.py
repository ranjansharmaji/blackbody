import numpy as np
import matplotlib.pyplot as ml
from scipy.constants import h,k,c
"""black body spectrum at T=2.725 kelvin."""
def spectrum(x):
    T=2.725
    y=2*h*c**2*x**5/(np.exp(h*c*x/(k*T))-1)
    return y
x=np.linspace(200,2200,100)
ml.plot(x,spectrum(x),label='blackbody spectrum at T=2.725')
file="firas_monopole_spec_vl.txt"
frequency=np.loadtxt(file,usecols=[0])
cmb_flux=np.loadtxt(file,usecols=[1])
p= 100*frequency                   # 100 due to m-1
d=10e-7*cmb_flux                    #si unit
ml.plot(p,d,label='data obtained from firas')
ml.xlabel('wave number is m^-1')
ml.ylabel('cmb_flux in W/(m^2 Hz)')
ml.legend()
ml.show()

q=np.amax(cmb_flux);print(q)
"""at wavenumber 383.4m^-1 frequency 5.45"""
