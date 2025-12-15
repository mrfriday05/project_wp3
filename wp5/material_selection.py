from shell import Shell
import math

def calculate_hoop_stress(self):
    sigma_hoop = self.p * self.R / self.t
    return sigma_hoop
Shell.calculate_hoop_stress = calculate_hoop_stress

def calculate_longitudinal_stress(self):
    sigma_longitudinal = self.p * self.R / (2 * self.t)
    return sigma_longitudinal
Shell.calculate_longitudinal_stress = calculate_longitudinal_stress

