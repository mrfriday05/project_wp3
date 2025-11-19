from lug import Lug
def cg(lug):
    Ax = 0
    x=0
    Ay = 0
    y=0
    for fastener in lug.fastenerlst:
        Ax+=fastener.A*fastener.x
        Ay+=fastener.A*fastener.y
        x+=fastener.x
        y+=fastener.y
    cgx = Ax/sum([fastener.A for fastener in lug.fastenerlst])
    cgy = Ay/sum([fastener.A for fastener in lug.fastenerlst])
    return (cgx,cgy)

def Finplane(lug, F):
    finplane = F/len(lug.fastenerlst)
    return finplane
def Finplanetot(lug, Fx, Fz):
    finplanex=Finplane(lug, Fx)
    finplanez=Finplane(lug, Fz)
    cgx,cgy = cg(lug)
    Mcgy = cgx*Fz+ cgy*Fx
    Ar2 =0
    Fx_lst = []
    Fz_lst = []
    for fastener in lug.fastenerlst:
        r2 = fastener.x**2 + fastener.y**2
        Ar2 += r2*fastener.A

    for fastener in lug.fastenerlst:
        Fx_lst.append(Mcgy*fastener.A*fastener.x/Ar2+finplanex)
        Fz_lst.append(Mcgy*fastener.A*fastener.z/Ar2+finplanez)
    return Fx_lst, Fz_lst

def bearing_check(lug, Fx, Fz, sigma_allow):
    Fx_lst, Fz_lst = Finplanetot(lug, Fx, Fz)
    for i in range (len(lug.fastenerlst)):
        fastener = lug.fastenerlst[i]
        Fx_M = Fx_lst[i]
        Fz_M = Fz_lst[i]
        sigma_bearing = (Fx_M**2 + Fz_M**2)**0.5 / lug.t2/lug.D2
        if sigma_bearing > sigma_allow:
            return False
    return True