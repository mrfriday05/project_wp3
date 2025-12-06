import math

def delta_b(fastener, lug):
    L_hsub=fastener.D2/2*0.5 #hexagonal head submersion depth
    L_engsub=fastener.D2/2*0.4 #nut-tightened
    L_nsub=fastener.D2/2*0.4
    delta_b=1/fastener.E*(L_hsub/fastener.A_eff+L_engsub/fastener.A_minor+(lug.t2+lug.t3)/fastener.A_eff)+L_nsub/fastener.E/fastener.A
    return delta_b

def delta_a(fastener, lug):
    delta_a=4*(lug.t2+lug.t3)/(math.pi*fastener.E*(fastener.D_out**2-fastener.D2**2))
    return delta_a

def force_ratio(fastener, lug):
    db=delta_b(fastener, lug)
    da=delta_a(fastener, lug)
    dr=db/(db+da)
    return dr

def fastener_yield_check(lug, F_y):
    for fastener in lug.fastenerlst:
        dr=force_ratio(fastener, lug)
        F_f=F_y*dr/len(lug.fastenerlst)
        if F_f/fastener.A_eff>fastener.yield_stress:
            fastener.yield_handling=False
    return