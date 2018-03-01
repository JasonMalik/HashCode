#! /usr/bin/python3
from sys import getsizeof
import numpy as np
import math

def toBool(row):
    tmp = row

    for i,c in enumerate(row):
        tmp[i] = np.uint8(0 if c=='T' else 1)
    return tmp

def printPizza(pizza):
    for r in pizza:
        print(r)

R,C,L,H = map(int,input().strip().split())
pizza = np.empty(shape=(R,C))

#print("R: %d C: %d L: %d H: %d" % (R,C,L,H))

for row in range(R):
    pizza[row] = toBool(list(input()))

inizio(pizza)


#0 tomato
#1 funghi
#nan "come ti pare" LETTURA

def inizio(pizza,r=6,c=7,l=1,h=5):
    #4 tizi angoli matrice
    indici = {1:[0,0,False],2:[0,c-1,False],3:[r-1,c-1,False],4:[r-1,0,False]}
    i = 1 #quale angolo siamo
    j = 0
    k = 0
    while(onealive):
     t = 0
     f = 0


     for j in range(h+1):
         if  M[indici[i][0]+j,indici[i][1]] == 0:
             t = t + 1
         elif M[indici[i][0]+j,indici[i][1]] == 1:
             f = f + 1
         else:
            print("yo")
    if(t>=l and f>=l):
        #Validazione fetts
        i=i+1

    if i == 1 or i == 4:
