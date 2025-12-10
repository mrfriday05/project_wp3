from shell import Shell
import math

def calculate_Q(self):
        E=self.material_props.E
        return self.p/E*(self.R/self.t)**2
Shell.calculate_Q = calculate_Q

def calculate_lambd(self):
    nu=self.material_props.nu
    lambd=math.sqrt(12/math.pi**4*(1-nu**2)*self.L**4/(self.R*self.t)**2)
    return lambd
Shell.calculate_lambd = calculate_lambd
    
def calculate_k(self):
    lambd=self.calculate_lambd()
    nu = self.material_props.nu
    k=lambd+12/math.pi**4*self.L**4/(self.R*self.t)**2*(1-nu**2)/lambd
    return k
Shell.calculate_k = calculate_k
    
def calculate_critical_stress(self):
    Q=self.calculate_Q()
    k=self.calculate_k()
    nu = self.material_props.nu
    E = self.material_props.E
    sigma_cr=(1.983-0.983*math.exp(-23.14*Q))*k*math.pi**2*E*self.t**2/(12*(1-nu**2)*self.L**2)
    return sigma_cr
Shell.calculate_critical_stress = calculate_critical_stress