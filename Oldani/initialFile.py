#auto dizionario
#corse, init
#!/usr/bin/python3
from collections import namedtuple
from operator import attrgetter


def getDistance(start,end):
    return abs(start[1]-end[1])+abs(start[0]-end[0])


def remove(self, id=None, value=None):
    for elem in self:
        if (id is not None and elem.id == id or
                value is not None and elem.value == value):
            super(Orders, self).remove(elem)
            break

def mostraDati(R,C,F,N,B,T,corse):
    print("R: %d C: %d F: %d N: %d B: %d T: %d" % (R,C,F,N,B,T))

    for c in corse:
        print("%d) partenza:(%d,%d) arrivo:(%d,%d) min:%d max:%d" % (c.init,c.a,c.b,c.x,c.y,c.s,c.f))


corsa = namedtuple('corsa','a b x y s f init')
corse = []

R,C,F,N,B,T = map(int,input().strip().split())
getted=True
auto={}
scritti=[]
for i in range(F):
    auto[i]=[0,0,[],T,0]


for n in range(N):
    a,b,x,y,s,f = map(int,input().strip().split())
    tmpC = corsa(a,b,x,y,s,f,n)
    corse.append(tmpC)
    scritti.append(False)

corse=sorted(corse, key=attrgetter('s'))
#distanza= quella dall'auto al suo punto di partenza
#distanzaStartFinish= quella dall'inizo alla fine della corsa
while (getted):
    getted=False
    for val,macchina in auto.items():
        for run in corse:

            distanza=getDistance((macchina[0],macchina[1]),(run.a,run.b))
            distanzaStartFinish=getDistance((run.a,run.b),(run.x,run.y))
            if(not(scritti[run.init]) and run.s>=macchina[4]+distanza and ((macchina[3]-distanza-distanzaStartFinish)>0) and  (macchina[4]+distanza+distanzaStartFinish)<run.f ):
                macchina[2].append(run.init)
                macchina[0]=run.x
                macchina[1]=run.y
                macchina[3] = macchina[3] - distanza - distanzaStartFinish
                getted=True
                if(run.s>(macchina[4]+distanza)):
                    macchina[4]=run.s + distanzaStartFinish
                else:
                    macchina[4]=macchina[4] + distanza + distanzaStartFinish
                scritti[run.init]=True
                #corse = sorted(corse, key=attrgetter('init'))
                #corse.remove(run.init)
                #corse = sorted(corse, key=attrgetter('s'))

            elif(not(scritti[run.init]) and ((macchina[3]-distanza-distanzaStartFinish)>0) and  (macchina[4]+distanza+distanzaStartFinish)<run.f ):
                macchina[2].append(run.init)
                macchina[0] = run.x
                macchina[1] = run.y
                macchina[3] = macchina[3] - distanza - distanzaStartFinish
                getted = True
                if (run.s > (macchina[4] + distanza)):
                    macchina[4] = run.s + distanzaStartFinish
                else:
                    macchina[4] = macchina[4] + distanza + distanzaStartFinish
                scritti[run.init]=True
               # corse = sorted(corse, key=attrgetter('init'))
              #  corse.remove(run.init)
              #  corse = sorted(corse, key=attrgetter('s'))


for val,m in auto.items():
    print(val,m[2])


