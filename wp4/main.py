from lug import Lug
from fastener import Fastener

from fastener_pattern import pattern_check
from pull_through_check import pull_through_forces
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import bearing_check as bc
import fastener_selection as fs
import data as dt
import thermal_check as tc
import MMOI_PIN as moi
import flange_design as fd

#========== Design Inputs (everything should be SI) =============


#Lug configuration (list of the coordinates centre of the lugs)

xdist_lug = 0.007      #m
zdist_lug = 0.0070      #m

fastener_type="M2"
fastener_d = dt.fastener_geometry(fastener_type)[0]  #m
safety_factor=4

lug_material=   "Titanium"
wall_material=  "Titanium"
fastener_material="Steel"

luglst=[
    Lug(x_length=0.02,  #m
        z_length=0.02,  #m
        t1=0.002,       #m
        t2=0.0080,        #m
        t3=0.005,       #m
        D1=0.01,        #m
        D2=fastener_d,  #m
        h=0.05,         #m   
        x=0,            #m
        z=0,            #m
        alpha=dt.material_properties(lug_material)[2],
        alpha_back=dt.material_properties(wall_material)[2],
        sigma_allow=dt.material_properties(lug_material)[1],  #Pa
        sigma_allow_lug_wall=dt.material_properties(wall_material)[1],  #Pa
        fastenerlst=[
            Fastener(x=-xdist_lug,z=-zdist_lug, type=fastener_type, material=fastener_material),
            Fastener(x= xdist_lug,z=-zdist_lug, type=fastener_type, material=fastener_material),
            Fastener(x=-xdist_lug,z= zdist_lug, type=fastener_type, material=fastener_material),
            Fastener(x= xdist_lug,z= zdist_lug, type=fastener_type, material=fastener_material)
        ]
    )
]

#========== End of Design Inputs =============
#========== Loads Calculation ============
loads_ = { 
    "R_x": 149.4,
    "R_y": 149.4,
    "R_z": 473,
    "N_x": 134.6,
    "N_y": 134.6,
    "N_z": 426.4,
    "M_1": 84.2,
    "M_2": 84.2,
    "M_3": 27.1, 
}

#========== Bearing Check ============


fig, ax = plt.subplots()

for lug in luglst:
    # Run checks
    lug_bearing=bc.bearing_check(lug, Fx=loads_["R_x"]*(safety_factor+1), Fz=loads_["R_z"]*(safety_factor+1))
    lug_pattern=pattern_check(lug)
    fs.fastener_yield_check(lug,loads_["R_y"]*(safety_factor+1))
    pull_through_forces(loads_["M_1"]*(safety_factor+1), loads_["M_3"]*(safety_factor+1), loads_["R_y"]*(safety_factor+1), lug)
    tc.thermal_stress_check_oup(lug, Mz=loads_["M_3"]*(safety_factor+1), Fy=loads_["R_y"]*(safety_factor+1))
    print("pull through, fastener_yield, bearing_t2, bearing_t3, thermal")
    for i, fastener in enumerate(lug.fastenerlst):
        print(f"fastener_{i}: {int(fastener.pull_through)} {int(fastener.yield_handling)} {int(fastener.bearing_t2)} {int(fastener.bearing_t3)} {int(fastener.pull_through_thermal)}")        


    # Lug flange dimensions
    M_z = max(loads_["M_1"], loads_["M_2"])
    stress_t = 572  # Material ultimate tensile strength in MPa
    W = 100  # M from the figure in mm, this is what is actually being used for the iteration

    D, T, E = fd.lug_flange_dimensions(W)  # All in mm
    F = fd.lug_tension(stress_t, W, D, T)  # All in N
    stress_b = fd.lug_bending(W, D, T, M_z)  # All in MPa
    load_check = fd.check(stress_t, loads_["N_x"], loads_["N_y"], F, stress_b)

    print(D, T, E, F, stress_b)
    print(load_check)

    # If it spits out true, the material or W can be changed to something smaller / weaker,
    # however, this will probably withstand the loads even if its lead-thin 


    # Lug position offset
    x0 = lug.x
    z0 = lug.z
    # Plotting
    circles = []
    rects = []
    for f in lug.fastenerlst:

        # Determine color based on bearing checks
        if not f.bearing_t2:
            color = 'red'      # fails plate thickness t2
        elif not f.bearing_t3:
            color = 'blue'     # fails lug wall t3
        else:
            color = 'green'    # OK

        # Create circle in *data units*
        circles.append(patches.Circle(
            (f.x + x0, f.z + z0),
            radius = lug.D2 / 2,
            edgecolor='black',
            facecolor=color,
            linewidth=2
        ))

        ax.add_patch(circles[-1])
    rects.append(patches.Rectangle(
        (x0 - lug.x_length / 2, z0 - lug.z_length / 2),
        lug.x_length,
        lug.z_length,
        edgecolor='black',
        facecolor='none',
        linewidth=2
    ))
    ax.add_patch(rects[-1])
# ensure circles are drawn correctly
check = pattern_check(luglst[0])
ax.set_aspect('equal', adjustable='box')
ax.relim()
ax.autoscale_view()
#print (moi.MOI_PIN(luglst[0])) 
plt.show()