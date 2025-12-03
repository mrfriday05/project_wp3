import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi, tau

def pull_through_forces(Mx,Mz,Fy,lug):
    # Variables 
    nf=len(lug.fastenerlst)
    rlst=[]
    for k in range(len(lug.fastenerlst)):
        rlst.append(sqrt(lug.fastenerlst[k].x**2+lug.fastenerlst[k].z**2))
    
    # Pull through forces
    Fpi=Fy/nf
    sx=0.0
    sz=0.0
    for j in range(nf):
        sx=sx+lug.fastenerlst[j].A*lug.fastenerlst[j].x**2
        sz=sz+lug.fastenerlst[j].A*lug.fastenerlst[j].z**2
    print(f"sx: {sx}, sz: {sz}")
    # Equations
    k=0
    for n in range(nf):
        print (n)
        FpMz=(Mz*lug.fastenerlst[n].A*lug.fastenerlst[n].x)/sx
        print(f"FpMz for fastener {n}: {FpMz}")
        FpMx=(Mx*lug.fastenerlst[n].A*lug.fastenerlst[n].z)/sz
        print(f"FpMx for fastener {n}: {FpMx}")
        F_tot=Fpi+FpMz+FpMx
        #lug.fastenerlst[i].pull_through_force=F

        print(f"Total pull through force for fastener {n}: {F_tot}")
        tau=F_tot/(3.14*lug.fastenerlst[n].D2/2*(lug.t2+lug.t3))
        print(f"Shear stress for fastener {n}: {tau}")
        print(lug.sigma_allow/sqrt(3))
        if abs(tau)>(lug.sigma_allow/sqrt(3)) or abs(tau)>(lug.sigma_allow_lug_wall/sqrt(3)):
            lug.fastenerlst[n].pull_through=False
            print(f"Fastener {n} fails pull through check.")
        
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