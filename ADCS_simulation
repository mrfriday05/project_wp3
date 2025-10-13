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

    def __init__(self, MoI, cp_to_cm, A_max, solar_constant, reflectivity, c, theta_eclipse, drag_force):
        self.MoI=MoI
        self.cp_to_cm=cp_to_cm
        self.phi0=np.arctan(cp_to_cm[0]/cp_to_cm[2])
        self.cp_to_cm_dist=np.linalg.norm(cp_to_cm)
        self.A_max=A_max
        self.solar_constant=solar_constant
        self.reflectivity=reflectivity
        self.c=c
        self.theta_eclipse=theta_eclipse
        self.drag_force=drag_force
        self.drag_torque=[0,drag_force*self.cp_to_cm*self.cp_to_cm[1],0]

    def solar_torque(self, theta):
        if theta>self.theta_eclipse or theta< -self.theta_eclipse:
            return np.array([0,0,0])
        T_y=self.solar_constant/self.c*self.A_max*(1+self.reflectivity)*np.cos(theta-self.phi0)*self.cp_to_cm
        return np.array([0,T_y,0])
    
    def gravity_torque(self):
        return np.array([0,0,0])
    
    def magnetic_torque(self,theta):
        return np.array([0,0,0])
    
    def actuator_torque(self,theta, command):
        return np.array([0,0,0])
    
    def actuator_innacuracy_torque(self,theta):
        return np.array([0,0,0])
    
    def total_torque(self,theta):
        return self.solar_torque(theta) + self.gravity_torque(theta) + self.magnetic_torque(theta) + self.drag_torque + self.actuator_innacuracy_torque(theta)   

    def step(self, angvec, omega, dt):
        alpha=np.linalg.inv(self.MoI)@self.total_torque(angvec)-np.cross(omega, self.MoI@omega)
        omega+=alpha*dt
        angvec+=omega[1]*dt
        return angvec, omega