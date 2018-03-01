#auto dizionario
#corse, init
#!/usr/bin/python3
from collections import namedtuple
from operator import attrgetter


def mostraDati(R,C,F,N,B,T,corse):
    print("R: %d C: %d F: %d N: %d B: %d T: %d" % (R,C,F,N,B,T))

    for c in corse:
        print("%d) partenza:(%d,%d) arrivo:(%d,%d) min:%d max:%d" % (c.init,c.a,c.b,c.x,c.y,c.s,c.f))


corsa = namedtuple('corsa','a b x y s f init')
corse = []

R,C,F,N,B,T = map(int,input().strip().split())

auto={}
for i in range(F):
    auto[i]=[0,0,[],T,0]


for n in range(N):
    a,b,x,y,s,f = map(int,input().strip().split())
    tmpC = corsa(a,b,x,y,s,f,n)
    corse.append(tmpC)

corse=sorted(corse, key=attrgetter('s'))
#distanza= quella dall'auto al suo punto di partenza
#distanzaStartFinish= quella dall'inizo alla fine della corsa
for macchina in auto:
    for corsa in corse:
        if(corsa.s>=macchina[4]+distanza and ((macchina[3]-distanza-distanzaStartFinish)>0) and  (macchina[4]+distanza+distanzaStartFinish)<corsa.f ):
            macchina[2].append(corsa.init)
            macchina[0]=corsa.x
            macchina[1]=corsa.y
            macchina[3] = macchina[3] - distanza - distanzaStartFinish

            if(corsa.s>(macchina[4]+distanza)):
                macchina[4]=corsa.s + distanzaStartFinish
            else:
                macchina[4]=macchina[4] + distanza + distanzaStartFinish
            corse.remove('init' == corsa.init)
        elif(((macchina[3]-distanza-distanzaStartFinish)>0) and  (macchina[4]+distanza+distanzaStartFinish)<corsa.f ):
            macchina[2].append(corsa.init)
            macchina[0] = corsa.x
            macchina[1] = corsa.y
            macchina[3] = macchina[3] - distanza - distanzaStartFinish
            if (corsa.s > (macchina[4] + distanza)):
                macchina[4] = corsa.s + distanzaStartFinish
            else:
                macchina[4] = macchina[4] + distanza + distanzaStartFinish

            corse.remove('init' == corsa.init)
