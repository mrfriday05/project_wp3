import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi

# Variables 
Mz=0.0 # Watch out for the sign!!!
Fy=0.0
nf=len(Lug.fastenerlst)
A=np.zeros(nf) #Fastener prop.
r=np.zeros(nf) #Fastener prop.
for i in range(nf):
    A[i]=Lug.fastenerlst[i].A
    r[i]=sqrt(Lug.fastenerlst[i].x**2+Lug.fastenerlst[i].z**2)

# Ranking creation
rank=np.zeros(nf)

# Pull through forces
Fpi=0.0
FpMz=np.zeros(nf)

# Equations
k=0
for i in range(nf):
    Fpi=Fy/nf
    s=0.0
    for j in range(nf):
        s=s+A[j]*r[j]**2
    FpMz[i]=(Mz*A[i]*r[i])/s
    F=Fpi+FpMz
    rank[k]=F
    k+=1

# Ranking fasteners....
best_fastener=0
for i in range(nf):
    if rank[i]>best_fastener:
        best_fastener=i+1

# ------------------------------------------------
# Shear stress 

# Fastener prop
df0=np.zeros(nf)
dfi=np.zeros(nf)
Y=np.array([])

# Shear stress calc
fail=np.zeros(nf)
for i in range(nf):
    t2=Lug.t2[i]
    t3=Lug.t3[i]
    dfo=0.0 #diameters
    dfi=0.0
    if Y==0:
        # pls make sure Y(tension yield stress for selected material) is known,
        # formula is too ugly and long
    tau=rank[i]/(pi*dfi*t2)
    if tau<Y:
        fail[i]=1

for i in range(nf):
    if fail[i]==0:
        # print('fastener nr.:',i+1,' fauiled')
# iterate with t2,t3
