import matplotlib.pyplot as plt
import numpy as np
import main

# ==================== USER INPUTS - CHANGE THESE ====================
START_ANGLE = main.angvec         # Starting angle (degrees)
TARGET_ANGLE = np.array([0.0,0.0,0.0])       # Target angle (degrees) 
INITIAL_RATE = main.omega      # Initial rotation speed (degrees/second)

# Physical properties
MOMENT_OF_INERTIA = 432.221    # kg·m² (how hard it is to rotate the satellite)
MAX_TORQUE = 0.265          # Nm (maximum torque the reaction wheel can produce)

# Controller gains
PROPORTIONAL_GAIN = 0.1     # How aggressively to correct angle error
DERIVATIVE_GAIN = 0.2       # How aggressively to damp rotation rate
DAMPING_FACTOR = 0.95       # Natural space damping (0.95 = 5% loss per second)
# ==================== END USER INPUTS ====================

# Convert gains for degrees (instead of radians)
kp = PROPORTIONAL_GAIN
kd = DERIVATIVE_GAIN

# Initialize satellite state
angle = START_ANGLE
angular_rate = INITIAL_RATE

error = TARGET_ANGLE - angle
control_signal = error * kp - angular_rate * kd  # This will damp rate even when error=0
    

