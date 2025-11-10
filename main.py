import numpy as np
import matplotlib.pyplot as plt
from ADCS_simulation import SatSym

Simulator = SatSym(                         MoI=np.diag([432.2,237.8,495.1]),
                                            cp_to_cm=np.array([-0.04,0.0,0.03]), #np.array([-0.018,0.0,0.011]),
                                            A_max=1.5**2*np.sqrt(2),
                                            solar_constant=2601,
                                            reflectivity=0.2,
                                            c=3e8,
                                            theta_eclipse=np.radians(139),
                                            drag_force=2.319*10**-5,
                                            gravity_direction=np.array([0.58018, -0.593139, 0.558192]),
                                            gravity_torque=3.308*(10**-6),
                                            rw_inaccuracy=0.05
                                            )
dt=0.3
simulated_time=6000 
T_orbit=6530
orbital_angular_velocity=2*np.pi/T_orbit                                                    
true_anomaly=0.0                                #true anomaly
omega=np.array([0.0,0.0,0.0])       #angular velocity
angvec=np.array([0.0,0.0,0.0])                  #angles between nadir and -w axis
ttab=[]

pointingtab=[]
omegatab=[] 
alphatab=[]



for i in range (int(simulated_time/dt)):
    true_anomaly += orbital_angular_velocity*dt
    if true_anomaly > np.pi:
        true_anomaly -= 2*np.pi
    rw_c=np.array([0.0,0.0,0.0])
    t_c=np.array([0.0,0.0,0.0])

    ttab.append(i*dt)
    angvec, omega, alpha=Simulator.step(true_anomaly=true_anomaly, omega=omega, angvec=angvec, dt=dt, rw_command=rw_c, t_command=t_c)
    
    pointingtab.append(angvec.copy())
    omegatab.append(omega.copy())
    alphatab.append(alpha.copy())

plt.plot(ttab, np.array(omegatab)[:,1])
plt.plot(ttab, np.array(alphatab)[:,1]*1000)
plt.plot(ttab, np.array(pointingtab)[:,1]*100000)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Angle vs Time')
plt.grid()
plt.show()