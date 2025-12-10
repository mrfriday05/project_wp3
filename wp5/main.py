from shell import Shell
import buckling

MyShell = Shell(p=500000, 
                t=0.001, 
                L=2.0, 
                R=0.5, 
                material_name="Steel"
                )

print("Calculating buckling properties for the shell...")
critical_stress = MyShell.calculate_critical_stress()
print(f"Critical Buckling Stress: {critical_stress / 1e6:.2f} MPa")
