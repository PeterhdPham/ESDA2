import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
# Define Transfer Function
wb = 10 #rad/s
Tf = 1/wb
num = np.array([1])
den = np.array([Tf , 1])
H = signal.TransferFunction(num, den)
print ('H(s) =', H)
# Frequencies
w_start = 0.01
w_stop = 100
step = 0.01
N = int ((w_stop-w_start )/step) + 1
w = np.linspace (w_start , w_stop , N)
# Frequency Response Plot
w, mag, phase = signal.bode(H, w)
plt.figure()
plt.semilogx(w, mag)
plt.axvline(x=1)
plt.axvspan(1, 100, facecolor='b', alpha=0.5)
plt.text(2, -12, 'Overgangsbånd', fontsize = 16)
plt.text(0.03, -12, 'Båndpass', fontsize = 16)
# plt.title("Lowpass Filter")
plt.grid(b=None, which='major', axis='both')
plt.grid(b=None, which='minor', axis='both')
plt.ylabel("Magnitude (dB)")
plt.show()