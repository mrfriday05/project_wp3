from lug import Lug
from fastener import Fastener
from equilibrium import loads 
from fastener_pattern import pattern_check
from pull_through_check import pull_through_forces
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import bearing_check as bc
import fastener_selection as fs
import data as dt

#========== Design Inputs (everything should be SI) =============


#Lug configuration (list of the coordinates centre of the lugs)

xdist_lug = 0.028       #m
zdist_lug = 0.014       #m
fastener_d=0.004        #m
fastener_type="M4"
safety_factor=4

lug_material="Titanium"
wall_material="Aluminum"

luglst=[
    Lug(x_length=0.08,  #m
        z_length=0.04,  #m
        t1=0.002,       #m
        t2=0.002,       #m
        t3=0.002,       #m
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
            Fastener(x=-xdist_lug,z=-zdist_lug, type=fastener_type, material='Steel'),
            Fastener(x= xdist_lug,z=-zdist_lug, type=fastener_type, material='Steel'),
            Fastener(x=-xdist_lug,z= zdist_lug, type=fastener_type, material='Steel'),
            Fastener(x= xdist_lug,z= zdist_lug, type=fastener_type, material='Steel')
        ]
    )
]

#========== End of Design Inputs =============
#========== Loads Calculation ============

loads_ = {
    "R_x": 149, #loads()[0],
    "R_y": 473, #loads()[1],
    "R_z": 149, #loads()[2],
    "N_x": loads()[3],
    "N_y": loads()[4],
    "N_z": loads()[5],
    "M_1": 27.1, #loads()[6],
    "M_2": loads()[7],
    "M_3": loads()[8],
    "M_4": loads()[9],
    "M_5": loads()[10],
    "M_6": loads()[11]
    }

#========== Bearing Check ============

print(loads_["R_x"])

fig, ax = plt.subplots()

for lug in luglst:
    # Run bearing checks
    lug_bearing=bc.bearing_check(lug, Fx=loads_["R_x"]*(safety_factor+1), Fz=loads_["R_z"]*(safety_factor+1))
    lug_pattern=pattern_check(lug)
    fs.fastener_yield_check(lug,loads_["R_y"]*(safety_factor+1))
    pull_through_forces(loads_["M_3"]*(safety_factor+1), loads_["R_y"]*(safety_factor+1), lug)
    print("pull through, fastener_yield, bearing_t2, bearing_t3")
    for i, fastener in enumerate(lug.fastenerlst):
        print(f"fastener_{i}: {int(fastener.pull_trough)} {int(fastener.yield_handling)} {int(fastener.bearing_t2)} {int(fastener.bearing_t3)}")        

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
plt.show()

print(check)