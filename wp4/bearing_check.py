from lug import Lug
import matplotlib.pyplot as plt
def cg(lug):
    Ax = 0
    Az = 0
    
    for fastener in lug.fastenerlst:
        Ax+=fastener.A*fastener.x
        Az+=fastener.A*fastener.z

    cgx = Ax/sum([fastener.A for fastener in lug.fastenerlst])
    cgz = Az/sum([fastener.A for fastener in lug.fastenerlst])
    return (cgx,cgz)

def Finplane(lug, F):
    finplane = F/len(lug.fastenerlst)
    return finplane

def Finplanetot(lug, Fx, Fz):
    finplanex=Finplane(lug, Fx)
    finplanez=Finplane(lug, Fz)
    cgx,cgz = cg(lug)
    Mcgy = cgx*Fz+ cgz*Fx
    Ar2 =0
    Fx_lst = []
    Fz_lst = []
    for fastener in lug.fastenerlst:
        r2 = fastener.x**2 + fastener.z**2
        Ar2 += r2*fastener.A
    
    for fastener in lug.fastenerlst:
        Fx_lst.append(Mcgy*fastener.A*fastener.x/Ar2+finplanex)
        Fz_lst.append(Mcgy*fastener.A*fastener.z/Ar2+finplanez)
    return Fx_lst, Fz_lst

def bearing_check(lug, Fx, Fz, margin = 1.0):
    Fx_lst, Fz_lst = Finplanetot(lug, Fx*(1+margin), Fz*(1+margin))
    
    for i, fastener in enumerate(lug.fastenerlst):
        fastener.bearing_t2 = True
        fastener.bearing_t3 = True
        Fx_tot = Fx_lst[i]
        Fz_tot = Fz_lst[i]
        sigma_bearing = (Fx_tot**2 + Fz_tot**2)**0.5 / (lug.t2*lug.D2)
        sigma_bearing_wall = (Fx_tot**2 + Fz_tot**2)**0.5 / (lug.t3*lug.D2)
        if sigma_bearing > lug.sigma_allow:
            fastener.bearing_t2 = False
        if sigma_bearing_wall > lug.sigma_allow_lug_wall:
            fastener.bearing_t3 = False
    return