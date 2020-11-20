import numpy as np
from numpy import genfromtxt
import random 

fleurs = genfromtxt('Flowers.csv', delimiter=',')
print(fleurs)
essaim = np.array()
bee = np.array()

for i in range(100):
    bee = np.concatenate(bee, [500,500])
    bee = np.concatenate(bee, np.random.permutation(fleurs))
    bee = np.concatenate(bee, [500,500])
    print("\n", bee, "\n")
    essaim = np.concatenate(essaim, bee)
print("\n", essaim, "\n") 
