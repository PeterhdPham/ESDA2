import numpy as np
import matplotlib.pyplot as plt
import csv

header = []
data = []
filename = 'CSV/noninverting100spek.csv'

#Henter data fra csvfil
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    #Leser første linje i csv-fila (den med navn til kanalene)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
#Legger inn data fra hver kanal i hver sin liste
time = [(p[0]) for p in data]
ch1 = [(p[1]) for p in data]
# ch2 = [(p[2]) for p in data]
plt.plot(time, ch1)
# plt.plot(time, ch2)
plt.plot(time,ch1, label = r'$f_{v^-}$')
# plt.plot(time,ch2, label = r'$v_o$')
# plt.set_xscale('log')

plt.grid(True)
# plt.title('Åpen-løkke signal',fontsize=24)
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Magnitude (dB)')
plt.legend(loc='upper right')
plt.show()
