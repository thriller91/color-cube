#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, copy

configs = []
polya = []
rot = []
dim = 6

# Gestion des arguments du programme (le nombre de couleurs)

if len(sys.argv)>1:
    n = int(sys.argv[1])
else:
    print "USAGE: ./cube.py number-of-colors"
    sys.exit(0)


# Début de la définition des fonctions

# Fonction générant l'ensemble des rotation physiques du cube, elle sont au nombre de 24
def Isom():
    cube = [0, 1, 2, 4 , 3, 5]

    for i in range(6):
        '''
        for j in range(4):
            cube[0] = i
            cube[5] = (5-i)%6 # la face opposée à i est 5-i (modulo 6)
            temp = cube[1]
            cube[1] = cube[2]
            cube[2] = cube[3]
            cube[3] = cube[4]
            cube[4] = temp
            rot.append(copy.copy(cube))
        temp = cube[1]
        cube[1] = cube[2]
        cube[2] = temp
        '''
        for j in range(4):
            cube[0] = i
            cube[5] = (5-i)%6 # la face opposée à i est 5-i (modulo 6)
            temp = cube[1]
            cube[1] = cube[2]
            cube[2] = cube[3]
            cube[3] = cube[4]
            cube[4] = temp
            rot.append(copy.copy(cube)) # on utilise "copy" parce que sinon, "rot" contient 24 fois la même liste
        # Il faut que le cube reste réel, les deux nouvelles faces seront donc opposées
        cube[cube.index((i+1)%6)] = i
        cube[cube.index((5-(i+1))%6)] = (5-i)%6
    #rot.remove([0, 1, 2, 4 , 3, 5])

# Fonction générant l'ensemble des cubes à n couleurs possible, il y a n**6 possibilités
def ConfigGen(n):
    cube = []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    for e in range(n):
                        for f in range(n):
                            cube.append(a)
                            cube.append(b)
                            cube.append(c)
                            cube.append(d)
                            cube.append(e)
                            cube.append(f)

                            configs.append(Rotat(cube, [0, 1, 2, 4 , 3, 5])) # On utilise un codage particulier pour les faces du cube, pour que la somme des points de deux faces opposées soit toujours égal à 5. (Mais ça ne doit pas avoir d'incidence sur le résultat final.)
                            cube = []

# Définition de l'action d'une rotation sur un cube
def Rotat(cube, rotation):
    new = []
    for i in range(dim):
        new.append(cube[rotation[i]])
    return new # on renvoit le nouveau cube, après rotation

if __name__ == '__main__':

    print "Number of colors: " + str(n) # Pour le fun

    # On commence par fabriquer l'ensemble des rotations du cube
    Isom()
    print "Number of physical symetries of the cube: " + str(len(rot))

    # On constuit ensuite toutes les configurations
    ConfigGen(n)
    print "Number of configurations: " + str(n) + "**6 = " + str(len(configs))

    # Et on élimine enfin les configurations redondantes
    checklist = []
    for cube in configs:
        if cube not in checklist:
            polya.append(copy.copy(cube))
            for rotation in rot:
                old = Rotat(cube,rotation)
                if not old in checklist:
                    checklist.append(copy.copy(old))

    print "Result: " + str(len(polya))
