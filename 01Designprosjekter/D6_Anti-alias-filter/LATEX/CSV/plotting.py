import numpy as np
import matplotlib.pyplot as plt
import csv
import os


header = []
data = []
dir_containing_file = 'C:/Users/peter/Documents/ESDA2/01Designprosjekter/D6_Anti-alias-filter/LATEX/CSV'
filename = 'vout.csv'

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
ch2 = [(p[2]) for p in data]
plt.plot(time, ch1)
# plt.plot(time, ch2)
fig, (ax) = plt.subplots(1,1)
ax.plot(time,ch1, label = 'vout')
# ax.plot(time,ch2, label = 'ch2')
ax.grid(True)
ax.set_title('Oscilloskop')
ax.set_xlabel('Tid (s)')
ax.set_ylabel('Spenning (V))')
ax.set_xscale('log')
plt.show()
