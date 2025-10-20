import numpy as np
import matplotlib.pyplot as plt
from ADCS_simulation import SatSym

Simulator = SatSym(                         MoI=np.diag([432.2,237.8,495.1]),
                                            cp_to_cm=np.array([0.018,0.0,0.011]),
                                            A_max=1.5**2*np.sqrt(2),
                                            solar_constant=2601,
                                            reflectivity=0.2,
                                            c=3e8,
                                            theta_eclipse=np.radians(139),
                                            drag_force=2.319e-4 
                                            )
dt=1
T=1000
omega=np.array([0.0,0.0,0.0])
ttab=[]

thetatab=[]
omegatab=[]


for i in range (int(T/dt)):
    
    Simulator.step(Simulator.theta, omega, dt)
    ttab.append(i*dt)
    thetatab.append(Simulator.theta)
    omegatab.append(Simulator.omega)

plt.plot(ttab, thetatab)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.grid()
plt.show()