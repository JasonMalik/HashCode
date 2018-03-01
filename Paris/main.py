#!/usr/bin/python3
from collections import namedtuple
from operator import attrgetter

def mostraDati(R,C,F,N,B,T,corse):
    print("R: %d C: %d F: %d N: %d B: %d T: %d" % (R,C,F,N,B,T))

    for c in corse:
        print("%d) partenza:(%d,%d) arrivo:(%d,%d) min:%d max:%d" % (c.init,c.a,c.b,c.x,c.y,c.s,c.f))

#Calcola la distanza tra due nodi ed un grafo dato
#Start: Tupla (x,y)
#End: Tupla (x,y)
#Esempio: getDistance((0,0),(4,2))
def getDistance(start,end):
    return abs(start[1]-end[1])+abs(start[0]-end[0])

corsa = namedtuple('corsa','a b x y s f init')
corse = []
town = None #Qui ci va il grafo della città

R,C,F,N,B,T = map(int,input().strip().split())

for n in range(N):
    a,b,x,y,s,f = map(int,input().strip().split())
    tmpC = corsa(a,b,x,y,s,f,n)
    corse.append(tmpC)


corse = sorted(corse, key=attrgetter('s'))

#mostraDati(R,C,F,N,B,T,corse)
