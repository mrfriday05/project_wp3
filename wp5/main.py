from shell import Shell
import buckling
import loads

MyShell = Shell(p=5e5, 
                t=0.001, 
                L=1.5, 
                R=0.2, 
                material_name="Steel"
                )


#Buckling margin
buckling_margin = MyShell.buckling_force() / loads.forces(MyShell)["fz"]
print(f"Critical Stress: {MyShell.calculate_critical_stress():.2f} Pa")
print(f"Buckling Force: {MyShell.buckling_force():.2f} N")
print(f"Buckling Margin: {buckling_margin:.2f}")