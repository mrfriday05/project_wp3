from lug import Lug
from fastener import Fastener
#========== Design Inputs =============
#Geometry:

t1 = 5      #mm
t2 = 5      #mm
t3 = 10     #mm

D1 = 15     #mm
D2 = 5      #mm

h = 20      #mm

#Lug configuration (list of the coordinates centre of the lugs)


luglst=[]

#Fastener configuration (list of the coordinates centre of the fasteners w.r.t center of lug)
e1 = 1.5*D2         #mm     #minimum dist
e2 = 1.5*D2         #mm     #minimum dist
ydist = D2*2.5      #mm     #if back-up is metal
xdist = 30          #mm     
luglst = [[-xdist,-ydist],[xdist,-ydist],[-xdist,ydist],[xdist,ydist]]



