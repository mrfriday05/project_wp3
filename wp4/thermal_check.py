import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi
from pull_through_check import pull_through_forces as ptf
import fastener_selection as fs

# Reference temp of Delft is Tref=288.15 K and Twork are temp from wp2
# Alphas are the thermal expansions coeff of the fastener, back-up wall and s/c wall
# Asw is the stiffness area of the fastener(???) and Ef is Young modulus of fastener
# phi is smth from app B(???)

# Thermal stress in back-up wall
def thermal_load_bakcupwall(fastener, lug, Tref=288.15,Twmax=284.4,Twmin=272.15):
    dTmax=Twmax-Tref
    dTmin=Twmin-Tref
    phi=fs.force_ratio(fastener, lug)
    
    Fmax=dTmax*fastener.E*fastener.A*(1-phi)*(fastener.alpha-lug.alpha)
    Fmin=dTmin*fastener.E*fastener.A*(1-phi)*(fastener.alpha-lug.alpha)
    return max(abs(Fmax),abs(Fmin))

def thermal_load_scwall(fastener, lug, Tref=288.15,Twmax=284.4,Twmin=272.15):
    dTmax=Twmax-Tref
    dTmin=Twmin-Tref
    phi=fs.force_ratio(fastener, lug)
    Fmax=dTmax*fastener.E*fastener.A*(1-phi)*(fastener.alpha-lug.alpha_back)
    Fmin=dTmin*fastener.E*fastener.A*(1-phi)*(fastener.alpha-lug.alpha_back)
    return max(abs(Fmax),abs(Fmin))

def thermal_stress_check_oup(lug, Tref=288.15,Twmax=284.4,Twmin=272.15, Mz=0, Fy=0):
    
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
        F_t_fastener=thermal_load_bakcupwall(lug.fastenerlst[0], lug, Tref,Twmax,Twmin)
        F_t_fastener_sc=thermal_load_scwall(lug.fastenerlst[0], lug, Tref,Twmax,Twmin)
        FpMz=(Mz*lug.fastenerlst[i].A*rlst[i])/s
        F=Fpi+FpMz+F_t_fastener+F_t_fastener_sc
        lug.fastenerlst[i].pull_through_force=F
        k+=1

        tau=F/(pi*lug.fastenerlst[i].D2/2*(lug.t2+lug.t3))
        #print(tau)
        if tau>lug.sigma_allow/sqrt(3) or tau>lug.sigma_allow_lug_wall/sqrt(3):
            lug.fastenerlst[i].pull_trough_thermal=False
    return
    

# Thermal check in plane
def thermal_stress_check_ip(strength_bw,strength_sw,t2,t3,nf,Mz,Fy,A,r,alpha_f,alpha_bw,Asw,Ef,phi,alpha_sw):
    sigma_bw=np.zeros(nf)
    sigma_bw=np.zeros(nf)
    # I HAVE NO CLUE HOW TO DO THIS