import numpy as np
from fastener import Fastener
from lug import Lug
from math import sqrt,pi
from pull_through_check import pull_through_forces as ptf


# Reference temp of Delft is Tref=288.15 K and Twork are temp from wp2
# Alphas are the thermal expansions coeff of the fastener, back-up wall and s/c wall
# Asw is the stiffness area of the fastener(???) and Ef is Young modulus of fastener
# phi is smth from app B(???)

# Thermal stress in back-up wall
def thermal_load_bakcupwall(alpha_f,alpha_bw,Tref=288.15,Asw,Ef,phi,Twmax=284.4,Twmin=272.15):
    dTmax=Twmax-Tref
    dTmin=Twmin-Tref
    Fmax=dTmax*Ef*Asw*(1-phi)*(alpha_f-alpha_bw)
    Fmin=dTmin*Ef*Asw*(1-phi)*(alpha_f-alpha_bw)
    return max(abs(Fmax,Fmin))


# Thermal stress in s/c wall
def thermal_load_scwall(alpha_f,alpha_sw,Tref=288.15,Asw,Ef,phi,Twmax=284.4,Twmin=272.15):
    dTmax=Twmax-Tref
    dTmin=Twmin-Tref
    Fmax=dTmax*Ef*Asw*(1-phi)*(alpha_f-alpha_sw)
    Fmin=dTmin*Ef*Asw*(1-phi)*(alpha_f-alpha_sw)
    return max(abs(Fmax,Fmin))

# Thermal stress check

# bearing_strength are the material bearing strength
# D and t are the attach. prop.

# Thermal check out of plane
def thermal_stress_check_oup(Ymat,t2,t3,nf,Mz,Fy,A,r,alpha_f,alpha_bw,Asw,Ef,phi,alpha_sw,dfi):
    tau_bothwalls=np.zeros(nf)
    pload=ptf(Mz,Fy,nf,A,r)
    for i in range(nf):
        tau_bothwalls[i]=(pload[i]+thermal_load_bakcupwall(alpha_f,alpha_bw,Tref=288.15,Asw,Ef,phi,Twmax=284.4,Twmin=272.15)+thermal_load_scwall(alpha_f,alpha_sw,Tref=288.15,Asw,Ef,phi,Twmax=284.4,Twmin=272.15))/(pi*dfi*(t2[i]+t3[i]))
        if tau_bothwalls[i]<Ymat:
            return 'Fastener nr. ',i+1,'failed oup+thermal load'

# Thermal check in plane
def thermal_stress_check_ip(strength_bw,strength_sw,t2,t3,nf,Mz,Fy,A,r,alpha_f,alpha_bw,Asw,Ef,phi,alpha_sw):
    sigma_bw=np.zeros(nf)
    sigma_bw=np.zeros(nf)
    # I HAVE NO CLUE HOW TO DO THIS