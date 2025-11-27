import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi

# Ranking creation
nf=len(Lug.fastenerlst)
rank=np.zeros(nf)

def pull_through_forces(Mz,Fy,nf,A,r):
    global rank
    # Variables 
    for i in range(nf):
        A[i]=Lug.fastenerlst[i].A
        r[i]=sqrt(Lug.fastenerlst[i].x**2+Lug.fastenerlst[i].z**2) # This assumes the cg of the fasteners is the center of the lug
    
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
    return rank

# ------------------------------------------------
# Shear stress 
def pull_through_shear_stress(Y,dfo,dfi,t2,t3,nf):
    global rank

    # Shear stress calc
    fail=np.zeros(nf)
    for i in range(nf):
        # pls make sure Y(tension yield stress for selected material) is known,
        # formula is too ugly and long
        tau=rank[i]/(pi*dfi*(t2+t3))
        if tau<Y:
            fail[i]=1

    for i in range(nf):
        if fail[i]==0:
            return 'fastener nr.:',i+1,' failed'
    # iterate with t2,t3
