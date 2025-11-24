from lug import Lug
from fastener import Fastener
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import bearing_check as bc
#========== Design Inputs (everything should be SI) =============


#Lug configuration (list of the coordinates centre of the lugs)

xdist_lug = 0.05        #m
ydist_lug = 0.025       #m
fastener_d=0.005        #m
luglst=[
    Lug(x_length=0.15,    #m
        z_length=0.08,   #m
        t1=0.004,       #m
        t2=0.01,        #m
        t3=0.001,        #m
        D1=0.01,        #m
        D2=fastener_d,  #m
        h=0.05,         #m   
        x=0,            #m
        z=0,            #m
        sigma_allow=300e6,  #Pa
        sigma_allow_lug_wall=300e6,  #Pa
        fastenerlst=[
            Fastener(x=-xdist_lug,z=-ydist_lug,A=fastener_d**2*np.pi/4),
            Fastener(x= xdist_lug,z=-ydist_lug,A=fastener_d**2*np.pi/4),
            Fastener(x=-xdist_lug,z= ydist_lug,A=fastener_d**2*np.pi/4),
            Fastener(x= xdist_lug,z= ydist_lug,A=fastener_d**2*np.pi/4)
        ]
    )
]
#========== End of Design Inputs =============
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
ax.set_aspect('equal', adjustable='box')
ax.relim()
ax.autoscale_view()
plt.show()
