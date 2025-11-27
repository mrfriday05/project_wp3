from lug import Lug
from fastener import Fastener
from equilibrium import loads 
from fastener_pattern import pattern_check
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import bearing_check as bc
import fastener_selection as fs

#========== Design Inputs (everything should be SI) =============


#Lug configuration (list of the coordinates centre of the lugs)

xdist_lug = 0.05        #m
zdist_lug = 0.025       #m
fastener_d=0.004        #m

luglst=[
    Lug(x_length=0.15,  #m
        z_length=0.08,  #m
        t1=0.004,       #m
        t2=0.001,       #m
        t3=0.001,       #m
        D1=0.01,        #m
        D2=fastener_d,  #m
        h=0.05,         #m   
        x=0,            #m
        z=0,            #m
        sigma_allow=300e6,  #Pa
        sigma_allow_lug_wall=300e6,  #Pa
        fastenerlst=[
            Fastener(x=-xdist_lug,z=-zdist_lug, type='M4', material='Steel'),
            Fastener(x= xdist_lug,z=-zdist_lug, type='M4', material='Steel'),
            Fastener(x=-xdist_lug,z= zdist_lug, type='M4', material='Steel'),
            Fastener(x= xdist_lug,z= zdist_lug, type='M4', material='Steel')
        ]
    )
]

#========== End of Design Inputs =============
#========== Loads Calculation ============

loads_ = {
    "R_x": loads()[0],
    "R_y": loads()[1],
    "R_z": loads()[2],
    "N_x": loads()[3],
    "N_y": loads()[4],
    "N_z": loads()[5],
    "M_1": loads()[6],
    "M_2": loads()[7],
    "M_3": loads()[8],
    "M_4": loads()[9],
    "M_5": loads()[10],
    "M_6": loads()[11]
    }

#========== Bearing Check ============

fig, ax = plt.subplots()

for lug in luglst:
    # Run bearing checks
    bc.bearing_check(lug, Fx=1000, Fz=500)
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