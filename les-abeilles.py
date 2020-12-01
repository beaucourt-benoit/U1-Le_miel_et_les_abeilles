# Projet le miel et les abeilles
# Algorithme génétique

import numpy as np
from copy import deepcopy, copy
import matplotlib.pyplot as plt
import pandas as pd

class Abeille:
    # Classe représentant une abeille
    def __init__(self):
        #init abeille
        self.genome = self.buildgenes()
        self.parcours = self.path()
        self.score = self.fitness()

    def printtest(self):
        print('genome', self.genome)
        print('fitness', self.fitness)
        return

    def buildgenes(self):
        df = pd.read_csv('Flowers.csv')
        subset = df[['x', 'y']]
        flowers = [tuple(x) for x in subset.to_numpy()]
        f = flowers
        genome = deepcopy(f)
        np.random.shuffle(genome)
        return genome

    def path(self):
        parcours = [(500, 500)] + self.genome + [(500, 500)]
        #print('Parcours', parcours, '\n')
        return parcours

    #Calcul de la distance
    def distance(self, pt1, pt2):
        print()
        dist = (int((pt1[0] - pt2[0])**2) + int((pt1[1] - pt2[1])**2))
        return dist

    #Calcul de la fitness
    def fitness(self):
        score = 0
        for i in range(len(self.parcours) - 1):
            dist = self.distance(self.parcours[i], self.parcours[i+1])
            print("distance = ", dist, '\n')
            score = score + dist
            print("fitness = ", score, '\n')
        return score

    #Dessiner le parcours d'une abeille
    def draw_bee(self):
        absx = np.array([])
        ordy = np.array([])
        for i in range(len(self.parcours)):
            disttotal = 0
            absx = np.append(absx, int(self.parcours[i][0]))
            ordy = np.append(ordy, int(self.parcours[i][1]))
        plt.plot(absx, ordy)
        plt.scatter(absx, ordy)
        plt.scatter(absx[0], ordy[0], color="red") #Dessine la position de la Ruche
        plt.show()

class Essaim:
    #Classe représentant un essaim de N abeilles
    def __init__(self):
        self.nba = int(input("Nombre d'abeille :"))
        self.birate = float(input("Birthrate dans ]0:1[ :"))
        self.murate = float(input("Mutation rate :"))
        self.mucoef = float(input("Mutation coefficient :"))
        self.essaim = self.makeessaim()
        self.bb = ()
        self.meetgene = ()
        self.F = []

    def makeessaim(self):
        essaim = [Abeille() for i in range(self.nba)]
        print('\n essaim', essaim, '\n')
        return essaim

    def makefitness(self):
        for maya in self.essaim:
            print(maya.score)
            self.F.append(copy(maya.score))
        return self.F

    #choix des abeilles pour le crossover
    def meetbee(self):
        self.nbrmeetbees = int(round(self.nba * self.birate))
        print('\n Nbrmeetbees', self.nbrmeetbees, '\n')
        F = self.makefitness()
        self.tri = np.argsort(F, axis=None)
        print('\n liste triée', self.tri,"\n")

        #self.essaim = sorted(self.essaim)
        print('\n Sorted essaim', self.essaim, '\n')
        self.meetbees = self.tri[:self.nbrmeetbees]
        print('\n Sorted meetbees', self.meetbees, '\n')

        for i in self.meetbees:
            self.meetgene = np.append(self.meetgene, self.essaim[i])
        print("\n meet genome", self.meetgene, '\n')
        return self.meetgene

    def repro(self, a1, a2):
        for i in range(2):
            self.bb1 = a1
            print('\n bb1', self.bb1, '\n')
            self.bb2 = a2
            print('\n bb2', self.bb2, '\n')
        return self.bb1, self.bb2

    def crossover(self):

        for i in range(int(len(self.meetbees)-1)):
            self.repro(self.meetbees[i], self.meetbees[i+1])
            self.bb = np.append(self.bb, (self.bb1, self.bb2))
        print('\n les bébés', self.bb, '\n')
        return self.bb

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
#maya.draw_bee()

nuee = Essaim()
#print('ESSAIM', nuee.essaim, '\n')
nuee.meetbee()

print("\n genoome de l'abeille 1", nuee.meetgene[0].score, '\n')
print("\n parcours de l'abeille 1", nuee.meetgene[0].parcours, '\n')

nuee.crossover()
