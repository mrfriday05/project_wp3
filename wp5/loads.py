from shell import Shell
#Constants
g=9.81  #[m/s^2] gravitational acceleration

accelerations=(3.0*g, 3.0*g, 8.5*g)  #[m/s^2] accelerations in (x,y,z


m0 = 1525-34  #[kg] mass witzhout the structure

def forces(shell: Shell):
    mass = m0 + shell.mass
    fx = mass * accelerations[0]
    fy = mass * accelerations[1]
    fz = mass * accelerations[2]
    return {"fx": fx, "fy": fy, "fz": fz}
