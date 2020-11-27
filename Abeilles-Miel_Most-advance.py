
import numpy as np
from numpy import genfromtxt
from copy import deepcopy
from pylab import *
import random 

#Nombre d'abeille
nba = int(input("Nombre d'abeille :"))

#20% du nombre d'abeille
l = round(nba * 0.2)

#Liste des fleurs
fleurs = genfromtxt('Flowers.csv', delimiter=',')
fleurs = fleurs[1:]

#Distance entre deux fleurs
dist = int()
#Distance totale = fitness
disttotal = int()
#Liste des fitness
listedesfitness = np.array([ ])

# Définition de l'essaim

essaim = np.array(np.array([]))

for i in range(nba):
    dfleurs = deepcopy(fleurs)
    np.random.shuffle(dfleurs)
    dfleurs = np.insert(dfleurs, 0, [500, 500])
    dfleurs = np.append(dfleurs, [500,500])
    essaim = np.append(essaim, dfleurs)

essaim = essaim.reshape( nba, int((len(dfleurs) / 2)), 2)

##########################################

# Calcul du fitness

for i in range(len(essaim)):
    absx = np.array([])
    ordy = np.array([])
    disttotal = 0
    
    absx = np.append(absx, essaim[i, :, 0])
    ordy = np.append(ordy, essaim[i, :, 1])

    #plt.plot(absx, ordy)
    #plt.scatter(absx, ordy)
    #plt.scatter(absx[0], ordy[0], color="red") #La Ruche
    #plt.show()
    #print(essaim[i], "\n")
    #print(absx, "\n")
    #print(ordy, "\n")
    for j in range(int(len((essaim[i]))-1)):
        dist = ((absx[j] - absx[j+1])**2) + ((ordy[j] - ordy[j+1])**2)
        #print("distance = ", dist)
        disttotal = disttotal + dist

 # agrégation des fitness de l'essaim

    listedesfitness = np.append(listedesfitness, disttotal)
    print(listedesfitness, "\n")

########################################################################

# Tri (sort) des index des fitness de l'essaim
    
inlistedesfitness = np.argsort(listedesfitness, axis=None)
print(inlistedesfitness,"\n")

########################################################################

# Afichage des meilleurs 20%
bestfit = np.array([])
bestfitin = np.array([])
p = float()

for k in range(l):
    #print("essaim ", inlistedesfitness[k], "\n fitness :", listedesfitness[inlistedesfitness[k]], "\n genome :", essaim[inlistedesfitness[k]])
    print("Abeille :",k,"index :", inlistedesfitness[k])
    bestfit = np.append(bestfit, listedesfitness[inlistedesfitness[k]])
    bestfitin = np.append(bestfitin, inlistedesfitness[k])
    print(bestfit)
    print(bestfitin)

########################################################################

# Crossover 
sdfleurs = sorted(dfleurs)
enfants = np.array([])

for i in range(int(l-1)):
    genea = np.array([])
    print("DEBUT enfant", i)
    for j in range(52):
        print("i,j", i, j)
        print(essaim[int(bestfitin[i])][j])
        print(essaim[int(bestfitin[i+1])][j])
        geneplayers = [essaim[int(bestfitin[i])][j], essaim[int(bestfitin[i+1])][j]]
        aux = random.choice(geneplayers)
        print("aux", aux)
        lotre = geneplayers.remove(aux)
        print("lotre", lotre)

# DEBUT Test si le gene existe deja dans le genome
        if aux in genea:
            lotre = geneplayers.remove(aux)
            print("lotre", lotre)
        else:
            if lotre in genea:
                haz = random.choice(fleurs)
                while haz in gena:
                    genea = np.append(genea, haz)
            else:
                genea = np.append(genea, lotre)
            genea = np.append(genea, aux)
# FIN Test si le gene existe deja dans le genome

        genea = np.append(genea, aux)
        print(genea)
    print("FIN enfant", i)
    enfants  = np.append(enfants, genea)
    print("enfants", enfants)

enfants = np.reshape(enfants, (int((nba * 0.2) - 1), 52,2))
print("enfants fin", enfants)
#if sorted(geneb) == sorted(dfleurs):
    #    essaim = np.concatenante(essaim, geneb)
    #else:
    #    print("FAIL") 




##################################################################################
    #    print(len(geneb))
    #print(len(geneb))
    
    #print(len(essaim))  
    #geneb = []
 

########################################################################
    


#print("TEST1", essaim[0][25], "\n")
#print("TEST2", essaim[1][25], "\n")
#p1 = essaim[inlistedesfitness[0]][1:52]
#p2 = essaim[inlistedesfitness[1]][1:52]
#pp  = np.array([])
#p3 = np.array([])
#fl = np.array([])

## Python code t get difference of two lists
## Using set()
#def Diff(li1, li2):
#    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

#for m in range(50):
#    print("Parent1 :", p1[m], "Parent2 :", p2[m],"\n")
#    print(p1[m], p2[m])
#    print(np.random.shuffle(p1[m], p2[m]))
#    pp = np.random.shuffle(p1[m], p2[m])
#    print(pp)
#    #if pp[0] in fl:
#    #    p3 = np.append(pp[1])
#    #elif pp[1] in fl:
#    #    p3 = np.append(pp[0])
#    #elif:
#    #    p3 = np.append(random(Diff(fleurs, fl))
    

            

    
#p3 = np.insert(p3, 0, [500, 500])
#p3 = np.append(p3, [500,500])
