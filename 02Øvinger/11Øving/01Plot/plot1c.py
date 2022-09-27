import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return np.exp(1j*(5/np.pi)*x)+np.exp(1j*(5/np.pi)*x)+np.exp(-1j*(10*np.sqrt(2)/np.pi)*x)+np.exp(1j*(10*np.sqrt(2)/np.pi)*x)

x = np.linspace(-50, 50, 100)

plt.plot(x, f(x), color='red')

plt.show()