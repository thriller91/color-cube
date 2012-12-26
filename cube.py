#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, copy

configs = []
rot = []
dim = 6

if len(sys.argv)>1:
    n = int(sys.argv[1])
else:
    print "USAGE: ./cube.py number-of-colors"
    sys.exit(0)

def Isom():
    cube = [0, 1, 2, 4 , 3, 5]

    for i in range(6):
        for j in range(4):
            cube[0] = i
            cube[5] = (5-i)%6
            temp = cube[1]
            cube[1] = cube[2]
            cube[2] = cube[3]
            cube[3] = cube[4]
            cube[4] = temp
            rot.append(copy.copy(cube))
        cube[cube.index((i+1)%6)] = i
        cube[cube.index((5-(i+1))%6)] = (5-i)%6
    rot.remove([0, 1, 2, 4 , 3, 5])

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

                            configs.append(Rotat(cube, [0, 1, 2, 4 , 3, 5]))
                            cube = []

def Rotat(cube, rotation):
    new = []
    for i in range(dim):
        new.append(cube[rotation[i]])
    return new

if __name__ == '__main__':

    print "Number of colors: " + str(n)

    Isom()
    print "Number of physical symetries of the cube: " + str(len(rot))

    ConfigGen(n)
    print "Number of configurations: " + str(n) + "**6 = " + str(len(configs))

    L0 = 0
    while len(configs) != L0:
        L0 = len(configs)
        print str(L0)
        for cube in configs:
            i = configs.index(cube)
            for rotation in rot:
                new = Rotat(cube,rotation)
                if new in configs:
                    if configs.index(new) != i:
                        configs.remove(new)



    print "Result: " + str(len(configs))

    quit()
