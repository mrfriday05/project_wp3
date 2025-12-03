import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi, tau

def pull_through_forces(Mz,Fy,lug):
    # Variables 
    nf=len(lug.fastenerlst)
    rlst=[]
    for i in range(len(lug.fastenerlst)):
        rlst.append(sqrt(lug.fastenerlst[i].x**2+lug.fastenerlst[i].z**2))
    
    # Pull through forces
    Fpi=Fy/nf
    s=0.0
    for j in range(nf):
        s=s+lug.fastenerlst[j].A*rlst[j]**2

    # Equations
    k=0
    for i in range(nf):
        FpMz=(Mz*lug.fastenerlst[i].A*rlst[i])/s
        F=Fpi+FpMz
        lug.fastenerlst[i].pull_through_force=F
        k+=1

        tau=F/(pi*lug.fastenerlst[i].D2/2*(lug.t2+lug.t3))
        print(tau)
        if tau>lug.sigma_allow/sqrt(3) or tau>lug.sigma_allow_wall/sqrt(3):
            lug.fastenerlst[i].pull_through=False
    return
# ------------------------------------------------
# Shear stress

''' 
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

    
    # iterate with t2,t3
'''