# Projet le miel et les abeilles
# Algorithme génétique

import numpy as np
from copy import deepcopy, copy
import matplotlib.pyplot as plt
import pandas as pd


class Fleurs:
    #Classe représentant un champ de fleurs
    def __init__(self):
        self.flowers, self.nbrflrs, self.fetchflowers()

    #Constructeur de Fleurs
    def fetchflowers(self):
        df = pd.read_csv('Flowers.csv')
        subset = df[['x', 'y']]
        flowers = [tuple(x) for x in subset.to_numpy()]
        print('flowers', flowers)
        nbrflrs = len(flowers)
        print('nombre de fleurs', nbrflrs)
        return flowers, nbrflrs

class Abeille:
    # Classe représentant une abeille
    def __init__(self):
        #init abeille
        self.genome, self.parcours = self.buildgenes()
        self.fitness = self.fitness()

    def printtest(self):
        print(self.fitness)
        return

    def buildgenes(self):
        f = flowers
        genome = deepcopy(f)
        np.random.shuffle(genome)
        parcours = np.insert(copy(genome), 0, (500, 500))
        parcours = np.append(parcours, (500, 500))
        print('Parcours', parcours)
#        print()
        return genome, parcours

    #Calcul de la distance
    def distance(self, pt1, pt2):

        print()
        dist = (int((pt1[0] - pt2[0])**2) + int((pt1[1] - pt2[1])**2))
        return dist

    #Calcul de la fitness
    def fitness(self):
        fitness = 0
        for i in range(len(self.parcours) - 1):
            dist = self.distance(self.parcours[i], self.parcours[i+1])
            print("distance = ", dist)
            fitness = fitness + dist
        return fitness

    #Dessiner le parcours d'une abeille
    def draw_bee(self):
        for i in range(len(self.parcours)):
            absx = np.array([])
            ordy = np.array([])
            disttotal = 0
            absx = np.append(absx, self.parcours[i, :, 0])
            ordy = np.append(ordy, self.parcours[i, :, 1])
            plt.plot(absx, ordy)
            plt.scatter(absx, ordy)
            plt.scatter(absx[0], ordy[0], color="red") #Dessine la position de la Ruche
            plt.show()

class Essaim(Abeille):
    # Classe représentant un essaim de N abeilles
    def __init__(self):
        self.nba = int(input("Nombre d'abeille :"))
        self.birate = int(input("Birthrate :"))
        self.murate = int(input("Mutation rate :"))
        self.mucoef = int(input("Mutation coefficient :"))

    def essaim(self):
        self.essaim = np.array([])
        for i in range(self.nba):
            self.essaim = np.append(self.essaim, self.genome)

    #choix des abeilles pour le crossover
    def meetbee(self, essaim):
        self.nbrmeetbees = int(self.nba * self.birate)
        self.essaim = sorted(self.essaim)
        self.meetbees = self.essaim[:self.nbrmeetbees]

    def repro(self, a1, a2):
        for i in range(2):
            self.bb1 = a1
            self.bb2 = a2
        return self.bb1, self.bb2

    def crossover(self, meetbees):
        for i in range(int(len(meetbees)-1)):
            self.repro(self.meetbees[i], self.meetbees[i+1])

    def mutation(self, genome):
        self.genome = np.radom.shuffle(self.genome)
        return genome

class generation:
    # Classe représentant une generation
    def __init__(self):
        self.nbrgeneration = 0
        self.besta = self.essaim[0]
        self.bestfit = self.fitness(self.besta)
#        self.moyfitparents =
#        self.moyfitbb =
#        self.fitnessaim =

maya = Abeille()
maya.printtest()
