#!/usr/bin/python3
from collections import namedtuple
from operator import attrgetter
import matplotlib.pyplot as plt
import networkx as nx

def mostraDati(R,C,F,N,B,T,corse):
    print("R: %d C: %d F: %d N: %d B: %d T: %d" % (R,C,F,N,B,T))

    for c in corse:
        print("%d) partenza:(%d,%d) arrivo:(%d,%d) min:%d max:%d" % (c.init,c.a,c.b,c.x,c.y,c.s,c.f))

#Calcola la distanza tra due nodi ed un grafo dato
#Start: Tupla (x,y)
#End: Tupla (x,y)
#Esempio: getDistance(town,(0,0),(4,2))
def getDistance(graph,start,end):
    return len(nx.dijkstra_path(graph,start,end)) - 1

corsa = namedtuple('corsa','a b x y s f init')
corse = []
town = None #Qui ci va il grafo della città

R,C,F,N,B,T = map(int,input().strip().split())

town = nx.grid_2d_graph(R,C)

for n in range(N):
    a,b,x,y,s,f = map(int,input().strip().split())
    tmpC = corsa(a,b,x,y,s,f,n)
    corse.append(tmpC)


corse = sorted(corse, key=attrgetter('s'))

#mostraDati(R,C,F,N,B,T,corse)
#nx.draw(town)
