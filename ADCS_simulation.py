import numpy as np

class SatSym ():
    MoI:np.ndarray
    cp_to_cm:np.ndarray
    cp_to_cm_dist:float
    theta_eclipse:float
    phi0:float
    A_max:float
    solar_constant:float
    reflectivity:float
    c:float

    def __init__(self, MoI, cp_to_cm, A_max, solar_constant, reflectivity, c, theta_eclipse, drag_force,gravity_torque,gravity_direction, rw_inaccuracy):
        self.MoI=MoI
        self.cp_to_cm=cp_to_cm
        self.phi0=np.arctan(cp_to_cm[0]/-cp_to_cm[2])
        self.cp_to_cm_dist=np.linalg.norm(cp_to_cm)
        self.A_max=A_max
        self.solar_constant=solar_constant
        self.reflectivity=reflectivity
        self.c=c
        self.theta_eclipse=theta_eclipse
        self.drag_force=drag_force
        self.drag_torque_magnitude=-drag_force*self.cp_to_cm[2]
        self.gravity_torque_magnitude=gravity_torque
        self.gravity_direction=gravity_direction
        self.rw_inaccuracy=rw_inaccuracy
        

    def solar_torque(self, theta):
        if theta>self.theta_eclipse or theta< -self.theta_eclipse:
            return np.array([0,0,0])
        T_y=self.solar_constant/self.c*self.A_max*(1+self.reflectivity)*np.cos(theta-self.phi0)*self.cp_to_cm_dist
        return np.array([0,T_y,0])
    
    def gravity_torque(self):
        return self.gravity_torque_magnitude*self.gravity_direction
        
    def magnetic_torque(self,theta):
        return np.array([0,0,0])
    
    def drag_torque(self):
        return np.array([0,self.drag_torque_magnitude,0])
    
    def rw_torque(self, rw_command):
        rw_t=rw_command*(1+2*self.rw_inaccuracy*np.random.rand(1)[0]-self.rw_inaccuracy)
        return rw_t
    

    def total_torque(self,theta, rw_command, t_command):
        return self.solar_torque(theta) + self.gravity_torque() + self.magnetic_torque(theta) + self.drag_torque() + self.rw_torque(rw_command)

    def step(self, true_anomaly, angvec, omega, dt, rw_command, t_command):
        alpha=np.linalg.inv(self.MoI)@(self.total_torque(true_anomaly, rw_command, t_command)) #-np.cross(omega, self.MoI@omega))
        alpha_rw= np.linalg.inv(self.MoI)@self.rw_torque(rw_command)
        alpha0=alpha-alpha_rw
        omega+=alpha*dt
        angvec+=omega*dt
        return angvec, omega, alpha, alpha_rw, alpha0