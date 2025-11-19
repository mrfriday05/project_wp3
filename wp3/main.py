import numpy as np
import matplotlib.pyplot as plt
from ADCS_simulation import SatSym

def command(angvec,omega, accumulated_error, dt,rw_max_toqrue):
    # ==================== USER INPUTS - CHANGE THESE ====================
    angle = angvec         # Starting angle 
    determination_acuracy = 0.0012* np.pi/180  # Determination accuracy 
    target_angle = determination_acuracy*(2*np.random.rand(3)-1)     # Target angle
    
    angular_rate = omega      # Initial rotation speed (rad/second)

    threshold = 0.02
    max_torque = rw_max_toqrue        # Nm (maximum torque the reaction wheel can produce)
             
    kp = 9                  # How aggressively to correct angle error
    kd = 35                 # How aggressively to damp rotation rate
    ki = 0.001              # Integral gain for accumulated error

    error = target_angle - angle
    accumulated_error += error*dt
    signal = error * kp - angular_rate * kd + accumulated_error * ki
    if np.linalg.norm(signal)<threshold:
        return np.array([0.0,0.0,0.0]), accumulated_error
    if np.max(signal)>max_torque:
        signal = signal/np.linalg.norm(signal)*max_torque
    return signal, accumulated_error

def rw_speed(torque, delta_t, I, current_speed):
    new_speed = current_speed.copy()
    for i in range(3):
        new_speed[i] += (torque[i] * delta_t) / I  # ω_new = ω_old + (τ/I) * Δt
    return new_speed

Simulator = SatSym(                         MoI=np.diag([432.2, 237.8, 495.1]),
                                            cp_to_cm=np.array([-0.1, 0.0, 0.1]), #np.array([-0.018,0.0,0.011]),
                                            A_max=1.5**2*np.sqrt(2)+4,
                                            solar_constant=2601,
                                            reflectivity=0.8,
                                            c=3e8,
                                            theta_eclipse=np.radians(139),
                                            drag_force=2.319*10**-5,
                                            gravity_direction=np.array([0.58018, -0.593139, 0.558192]),
                                            gravity_torque=3.038*(10**-4),
                                            rw_inaccuracy=0.02,
                                            )
dt=0.5
simulated_time=653000
T_orbit=6530
orbital_angular_velocity=2*np.pi/T_orbit                                                    
true_anomaly=0.0                                #true anomaly
omega=np.array([0.0,0.0,0.0])                   #angular velocity
angvec=np.array([0.0,0.0,0.0])                  #angles between nadir and -w axis
ttab=[]
accumulated_error = np.array([0.0,0.0,0.0])
pointing_required=np.radians(0.1)
rw_max_speed=np.array([1000,1000,1000])/60*2*np.pi  #rad/s
max_torque=0.265
# max_torque=0.265
MoI_rw=0.1
rw_max_torque=np.array([max_torque,max_torque,max_torque])
speed_rw=omega.copy()

pointingtab=[]
omegatab=[] 
alphatab=[]
alpha0tab=[]
rwtab=[]
time_thrusters=0
rw_activations=0


for i in range (int(simulated_time/dt)):
    true_anomaly += orbital_angular_velocity*dt
    if true_anomaly > np.pi:
        true_anomaly -= 2*np.pi
    rw_c, accumulated_error = command(angvec, omega, accumulated_error,dt, max_torque)
    if rw_c[0]!=0:
        rw_activations+=1
    t_c = np.array([0.0,0.0,0.0])
    
    current_time=i*dt
    time_thrusters=time_thrusters+dt
    speed_rw=rw_speed(rw_c,dt,MoI_rw,speed_rw)
    thruster_needed = 4
    for j in range(3):
        if abs(speed_rw[j]) > rw_max_speed[j]:
            thruster_needed = j
            break

    if thruster_needed < 4:
        if thruster_needed==0:
        
            print(f"Thrusters at {current_time:.1f}s, interval: {time_thrusters:.1f}s")
        time_thrusters = 0
        speed_rw[thruster_needed] = 0.0

    ttab.append(i*dt)
    angvec, omega, alpha, alpha_rw, alpha0=Simulator.step(true_anomaly=true_anomaly, omega=omega, angvec=angvec, dt=dt, rw_command=rw_c, t_command=t_c)
    
    pointingtab.append(angvec.copy())
    omegatab.append(omega.copy())
    alphatab.append(alpha.copy())
    rwtab.append(speed_rw.copy())
    alpha0tab.append(alpha0.copy())

print(f'Average time between RW activations{simulated_time/rw_activations:.4} s')
plt.subplot(4,1,1)
plt.plot(ttab, np.array(alpha0tab)[:,0])
plt.plot(ttab, np.array(alpha0tab)[:,1])
plt.plot(ttab, np.array(alpha0tab)[:,2])
plt.xlabel('(s)')
plt.ylabel('(rad/s^2)')
plt.title('Angular Acceleration vs Time')   
plt.subplot(4,1,2)
plt.plot(ttab, np.array(omegatab)[:,0])
plt.plot(ttab, np.array(omegatab)[:,1])
plt.plot(ttab, np.array(omegatab)[:,2])
plt.xlabel('(s)')
plt.ylabel('(rad/s)')
plt.title('Angular Velocity vs Time')
plt.subplot(4,1,3)
plt.plot(ttab, np.array(pointingtab)[:,0])
plt.plot(ttab, np.array(pointingtab)[:,1])
plt.plot(ttab, np.array(pointingtab)[:,2])
plt.axhline(y=pointing_required, color='r', linestyle='--')
plt.axhline(y=-pointing_required, color='r', linestyle='--')
plt.xlabel('(s)')
plt.ylabel('(rad)')
plt.title('Angle vs Time')


plt.subplot(4,1,4)
plt.title('RW Speed vs Time')
plt.plot(ttab, np.array(rwtab)[:,0])
plt.plot(ttab, np.array(rwtab)[:,1])
plt.plot(ttab, np.array(rwtab)[:,2])
plt.xlabel('(s)')
plt.ylabel('(rad/s)')
plt.title('RW Angular Velocity vs Time')

plt.grid()
plt.tight_layout(pad=0.0)
plt.show()