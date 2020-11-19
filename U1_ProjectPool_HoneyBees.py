import csv 
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
from numpy import genfromtxt
import random 
import copy 

#Le champs, les fleurs et la ruche

Tableau = []
x = []
y = []
id = []

Tableau = genfromtxt('Flowers.csv', delimiter=',')
#print(Tableau)

Tableau[0] = [500, 500]

n = len(Tableau)

for i in range(n):
    x.append(int(Tableau[i][0]))
    y.append(int(Tableau[i][1]))
    id.append(int(i))

x.append(500)
y.append(500)

#Distance de la ruche à chacune des fleurs
a = int()
b = int()
c = 0

#Fonction Fitness du génome
for i in range(50):
    a = ([(a - b)**2 for a, b in zip(Tableau[0], Tableau[i])])[0] + ([(a - b)**2 for a, b in zip(Tableau[0], Tableau[i])])[1]
    b = b + a
    print(a)
    print(b)


#Individu "abeille", 51 gènes, gène 0 = dist ruche à fleur1, gène 51 = dist fleur50 à ruche
#for i in range(1,100):
#    i = random.shuffle(Tableau)
#    print(i)

#   print(Dist, "\n")
print(Tableau, "\n")
a = copy.deepcopy(Tableau)
np.random.shuffle(a)
print(a, "\n")




#plt.plot(x, y)
plt.scatter(x, y)
plt.scatter(x[0], y[0], color="red") #La Ruche
plt.show()