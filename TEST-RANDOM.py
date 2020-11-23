
import numpy as np
from numpy import genfromtxt
from copy import deepcopy
from pylab import *
import random 

#Nombre d'abeille
nba = int(input("Nombre d'abeille :"))

#Nombre de fleur
#nbf = input("Nombre de fleur :")

fleurs = genfromtxt('Flowers.csv', delimiter=',')
fleurs = fleurs[1:]
#print("Init fleurs \n", fleurs)

essaim = np.array(np.array([]))

for i in range(nba):
    dfleurs = deepcopy(fleurs)
    np.random.shuffle(dfleurs)
    dfleurs = np.insert(dfleurs, 0, [500, 500])
    dfleurs = np.append(dfleurs, [500,500])
    #print("\n", dfleurs, "\n")
    essaim = np.append(essaim, dfleurs)

essaim = essaim.reshape( nba, 52, 2)
dist = int()
disttotal = int()
listedesfitness = np.array([ ])
#print(len(essaim))

for i in range(len(essaim)):
    absx = np.array([])
    ordy = np.array([])
    
    absx = np.append(absx, essaim[i, :, 0])
    ordy = np.append(ordy, essaim[i, :, 1])

    #plt.plot(absx, ordy)
    #plt.scatter(absx, ordy)
    #plt.scatter(absx[0], ordy[0], color="red") #La Ruche
    #plt.show()
    print(essaim[i], "\n")
    print(absx, "\n")
    print(ordy, "\n")
    for j in range(int(len((essaim[i]))-1)):
        #dist = ([(int(a) - int(b))**2 for a, b in zip(int(absx[j]), int(absx[j+1]))]) + ([(int(c) - int(d))**2 for c, d in zip(int(ordy[j]), int(ordy[j+1]))])
        #print("absx", absx[j], absx[j+1], "ordy", ordy[j], ordy[j+1])
        #print("absx²", (absx[j] - absx[j+1])**2, "ordy²", (ordy[j] - ordy[j+1])**2)
        dist = ((absx[j] - absx[j+1])**2) + ((ordy[j] - ordy[j+1])**2)
        print("distance = ", dist)
        disttotal = disttotal + dist
     
    #print("fitness de l'abeille",[i],"=", disttotal)
    listedesfitness = np.append(listedesfitness, disttotal)
    disttotal = 0
    print(listedesfitness, "\n")
    

print(listedesfitness, "\n")
listedesfitness = np.sort(listedesfitness, axis=None)
print(listedesfitness)