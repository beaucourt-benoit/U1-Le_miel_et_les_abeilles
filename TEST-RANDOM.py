
import numpy as np
from numpy import genfromtxt
import random 

#Mélange le génome de start à stop
def shuffle_slice(a, start, stop):
    i = start
#    while (i < stop-1):
    for i in range(1, stop-1):
        idx = random.randrange(i, stop)
        a[i], a[idx] = a[idx], a[i]
        i += 1

test = [1,2,3,4,5,6,7,8,9,10,11,12]
tab = reshape(np.array([]), (52, -1))
lt = len(test)
print("init test \n", test)

for z in range(5):
    shuffle_slice(test, 1, n-1)
    print(" test - avant append \n", test)
    print(" tab - avant append \n", tab)
    tab = np.append(tab, test)
    print(" test - apres append\n", test)
    print(" tab - apres append \n", tab)

tab = reshape(tab, (5, 12))
print("Final tab \n", tab)
