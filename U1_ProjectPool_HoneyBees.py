import csv 
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from numpy import genfromtxt
import random 
import copy 

#Mélange le génome de start à stop
def shuffle_slice(a, start, stop):
    i = start
#    while (i < stop-1):
    for i in range(1, stop-1):
        idx = random.randrange(i, stop)
        a[i], a[idx] = a[idx], a[i]
        i += 1

#Le champs, les fleurs et la ruche
fleurs = np.array([])
absx = np.array([])
ordy = np.array([])
id = np.array([])

fleurs = genfromtxt('Flowers.csv', delimiter=',')
fleurs[0] = [500, 500]
r = [[500,500]]
champ = np.concatenate((fleurs, r))
n = len(fleurs)

print("fleurs \n", fleurs)
print("len fleurs\n",len(fleurs))
print("champ \n",champ)
print("len champ",len(champ))


for j in range(n):
    absx = np.append(absx, int(fleurs[j][0]))
    ordy = np.append(ordy, int(fleurs[j][1]))
    id = np.append(id, (int(j)))

absx = np.append(absx, 500)
ordy = np.append(ordy, 500)

# Essaim
essaim = np.array([])

for i in range(10):  
    shuffle_slice(champ, 1, 51)
    print("Champ avant le append :", champ)
    print("Essaim avant le append :", essaim)
    essaim = np.append(essaim, champ)
    print("Champ après le append :", champ)
    essaim = reshape(essaim, (52, -1))
    print("Essaim après le append :", essaim)
        
essaim = reshape(essaim, (20, 52))
print("Final essaim \n", essaim)
