from fastener import Fastener
class Lug:
    def __init__(self,x_length, z_length, t1, t2, t3, D1, D2, h, x, z,sigma_allow, sigma_allow_lug_wall, fastenerlst):
        self.x_length = x_length
        self.z_length = z_length
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.D1 = D1
        self.D2 = D2
        self.h = h
        self.x = x
        self.z = z
        self.sigma_allow = sigma_allow  
        self.sigma_allow_lug_wall = sigma_allow_lug_wall
        self.fastenerlst = fastenerlst
