
import csv 
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from numpy import genfromtxt
import random 
import copy 

#essaim de 100 abeilles
fleurs = genfromtxt('Flowers.csv', delimiter=',')
fleurs = fleurs[1:]
print("Init fleurs \n", fleurs)

essaim = np.array(np.array([]))

for i in range(100):
    dfleurs = deepcopy(fleurs)
    np.random.shuffle(dfleurs)
    dfleurs = np.insert(dfleurs, 0, [500, 500])
    dfleurs = np.append(dfleurs, [500,500])
    print("\n", dfleurs, "\n")
    essaim = np.append(essaim, dfleurs)


for j in essaim:
    print(j)
    #absx.append(int(T[j][0]))
    #ordy.append(int(T[j][1]))
    #id.append(int(j))

absx.append(500)
ordy.append(500)

# Essaim
essain = np.array([])
#e = copy.deepcopy(T)
#print("Valeur avant :", e)

for i in range(10):  
    shuffle_slice(T, 1, 51)
#    print("Avant le append :", T)
    essain = np.append(essain, T)
#    print("Après le append :", T)
#    print("essain :", essain)
    
essain = reshape(essain,(10, -1))
#print("essains", essain)
#print("l'abeille 100 :\n", essain[4])
#print("l'abeille 50 :\n", np.essain[50])
#print("l'abeille 1 :\n", np.essain[0])
    
#Fonction Fitness du génome - Distance de la ruche à la 1ere fleur puis de la fleur n à n+1 puis retour à la ruche
a = int()
b = int()

for i in range(50):
    a = ([(a - b)**2 for a, b in zip(Tableau[i], Tableau[i+1])])[0] + ([(a - b)**2 for a, b in zip(Tableau[i], Tableau[i+1])])[1]
    b = b + a
 #   print(a)
 #   print(b)

#Individu "abeille", 51 gènes, gène 0 = dist ruche à fleur1, gène 51 = dist fleur50 à ruche
#for i in range(1,100):
#    i = random.shuffle(Tableau)
#    print(i)

#   print(Dist, "\n")
#print(T, "\n")
a = copy.deepcopy(Tableau)
np.random.shuffle(a)
#print(a, "\n")

#plt.plot(absx, ordy)
#plt.scatter(absx, ordy)
#plt.scatter(absx[0], ordy[0], color="red") #La Ruche
#plt.show()

#test = [1,2,3,4,5,6,7,8,9,10,11,12]
tab = reshape(np.array([]), (52, -1))
#lt = len(test)
print("init T \n", T)
for z in range(5):
    shuffle_slice(T, 1, n-1)
    print(" test - avant append \n", test)
    print(" tab - avant append \n", tab)
    tab = np.append(tab, T)
    print(" test - apres append\n", test)
    print(" tab - apres append \n", tab)

tab = reshape(tab, (5, -1))
print("Final tab \n", tab)
