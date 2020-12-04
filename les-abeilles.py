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
        self.bb = ()
        print('\n a1', a1, '\n')
        print('\n a2', a2, '\n')
        count = 0
        for i in range(len(a1)-1):
            for j in range(len(a2)-1):
                print(range(len(a1)-1))
                print('\n a1[', i, ']', a1[i], '\n')
                print('\n a1[', i+1, ']', a1[i+1], '\n')
                print('\n a2[', j, ']', a2[j], '\n')
                print('\n a2[', j+1, ']', a2[j+1], '\n')

                if all((a1[i], a1[i+1])) == all((a2[j], a2[j+1])):
                    count = count +1
                    self.bb = np.append(self.bb, (a1[i], a1[i+1]))
                    print('\n YEAH! bb', self.bb, '\n')
                print('\n counter J', j, '\n')
            print('\n counter I', i, '\n')
        print('\n FINAL bb', self.bb, '\n')
        print('\n Nombre de boucle IF', count, '\n')
        return self.bb

    def crossover(self):
        print('\n meetbees', self.meetbees, '\n')
        print('\n meetgene', self.meetgene, '\n')
        self.babies = ()
        for i in range(int(len(self.meetbees)-1)):
            print('\n meetbees i ', self.meetbees[i], '\n')
            print("\n genoome de l'abeille i", self.meetgene[i].score, '\n')
            print("\n parcours de l'abeille i", nuee.meetgene[i].parcours, '\n')

            self.repro(self.meetgene[i].genome, self.meetgene[i+1].genome)
            self.babies = np.append(self.babies, self.bb)
        print('\n les bébés', self.babies, '\n')
        return self.babies

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

#maya = Abeille()
#maya.printtest()
#maya.draw_bee()

nuee = Essaim()
print('ESSAIM', nuee.essaim, '\n')
nuee.meetbee()

print("\n genoome de l'abeille 1", nuee.meetgene[0].score, '\n')
print("\n parcours de l'abeille 1", nuee.meetgene[0].parcours, '\n')

nuee.crossover()

#test1 = ((0, 0), (2, 3), (9, 6), (3, 8))
#test2 = ((2, 3), (0, 0), (9, 6), (3, 8))
#testbb = test1, test2


#print('test1', test1)
#print('test2', test2)



Essaim.repro(testbb, test1, test2)
