import math
from material_properties import Material

class Shell:
    def __init__(self, p, t, L, R, material_name):
        self.p = p      # pressure
        self.material_props = Material(material_name)  # material properties
        self.t = t      # thickness
        self.L = L      # length
        self.R = R      # radius
        self.mass = self.calculate_mass()

    def calculate_mass(self):
        if self.p >=0:
            volume = 2*math.pi * self.R * self.t * (self.L-2*self.R) + 4*math.pi*self.R**2*self.t  # Volume of the shell with hemispherical ends
        else:
            volume = 2 * math.pi * self.R * self.L * self.t  # Volume of the shell
        mass = volume * self.material_props.density 
        self.mass = mass
        return mass