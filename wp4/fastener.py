import data

class Fastener:
    def __init__(self,x,z,type, material='Steel'):
        self.x = x
        self.z = z
        d, A_nom, A_minor, A_eff, d_head = data.fastener_geometry(type)
        E, yield_stress, _, alpha = data.material_properties(material)
        self.A = A_nom
        self.A_minor = A_minor
        self.A_eff = A_eff
        self.D2 = d
        self.D_out = d_head
        self.E=E
        self.yield_stress=yield_stress
        self.alpha=alpha
        self.yield_handling=True
        self.bearing_t2 = True
        self.bearing_t3 = True