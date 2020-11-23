import numpy as np
from numpy import genfromtxt
import random 

fleurs = genfromtxt('Flowers.csv', delimiter=',')
print(fleurs)
essaim = np.array()
bee = np.array()

for i in range(10):
    bee = np.concatenate(bee, [500,500])
    bee = np.concatenate(bee, np.random.shuffle(fleurs))
    bee = np.concatenate(bee, [500,500])
    print("\n", bee, "\n")
    essaim = np.append(essaim, bee)
print("\n", essaim, "\n") 
