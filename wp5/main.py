from shell import Shell
from material_properties import Material
import material_selection
import buckling
import loads
import matplotlib.pyplot as plt
import numpy as np

MyShell = Shell(p=5e5, 
                t=0.001, 
                L=1.5, 
                R=0.25, 
                material_name="Titanium"
                )


#Buckling margin
buckling_margin = MyShell.buckling_force() / loads.forces(MyShell)["fz"]
hoop_margin = MyShell.material_props.yield_stress / MyShell.calculate_hoop_stress()
print(f"Critical Stress (Euler Buckling): {MyShell.calculate_critical_stress_euler()/1e6:.2f} MPa")
print(f"Critical Stress (Shell Buckling): {MyShell.calculate_critical_stress_shell()/1e6:.2f} MPa")
print(f"Buckling Force: {MyShell.buckling_force():.2f} N")
print(f"Buckling Margin: {buckling_margin:.2f}")
print(f"Hoop Stress: {MyShell.calculate_hoop_stress()/1e6:.2f} MPa")
print(f"Hoop Margin: {hoop_margin:.2f}")
print(f"Mass: {MyShell.mass:.2f} kg")
