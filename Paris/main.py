#!/usr/bin/python3
from collections import namedtuple
from operator import attrgetter
import networkx as nx

def mostraDati(R,C,F,N,B,T,corse):
    print("R: %d C: %d F: %d N: %d B: %d T: %d" % (R,C,F,N,B,T))

    for c in corse:
        print("%d) partenza:(%d,%d) arrivo:(%d,%d) min:%d max:%d" % (c.init,c.a,c.b,c.x,c.y,c.s,c.f))


corsa = namedtuple('corsa','a b x y s f init')
corse = []

R,C,F,N,B,T = map(int,input().strip().split())

for n in range(N):
    a,b,x,y,s,f = map(int,input().strip().split())
    tmpC = corsa(a,b,x,y,s,f,n)
    corse.append(tmpC)


sorted(corse, key=attrgetter('init'))
mostraDati(R,C,F,N,B,T,corse)
