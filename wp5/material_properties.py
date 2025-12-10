class Material:
    name: str
    density: float
    E: float
    yield_stress: float
    nu: float

    def __init__(self, name):
        self.name = name
        if name == "Steel":              #D6AC   
            self.E = 210e9               # Pa
            self.yield_stress = 1724e6   # Pa
            self.density = 7870          # kg/m^3
            self.nu = 0.32               # Poisson's ratio
        
        elif name == "Aluminum":         #AA2024-T3
            self.E = 70e9                # Pa
            self.yield_stress = 345e6    # Pa
            self.density = 2780          # kg/m^3
            self.nu = 0.33               # Poisson's ratio
        
        elif name == "Titanium":        #Ti-6Al-4V
            self.E = 114e9               # Pa
            self.yield_stress = 880e6    # Pa
            self.density = 4430          # kg/m^3
            self.nu = 0.34               # Poisson's ratio

        elif name == "Magnesium":       #AZ31B-H24
            self.E = 45e9                # Pa
            self.yield_stress = 221e6    # Pa
            self.density = 1740          # kg/m^3
            self.nu = 0.35               # Poisson's ratio
        
        '''
        elif name == "CFRP":
            self.E = 70e9                # Pa
            self.yield_stress = 600e6    # Pa
            self.density = 1600          # kg/m^3
            self.nu = 0.28               # Poisson's ratio
        '''
        