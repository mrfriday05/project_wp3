# --- Constants ---
g_0 = 9.81
g = 9.81 # Change depending on height

# --- Initialize all variables ---
a_y = 8.5 * g_0
a_x = 3 * g_0
a_z = a_x
# MASS
m_A = 0.5
m_SA = 4.575
# DIMENSIONS [m]
h_A = 0.5
l_A = 0.1
l_SA = 1.25         #NOTE: this is only assumption that do not include any arm, just the total length of the solar array and arm from the pin joint
width_SA = 0.03

def loads (a_y=8.5,a_x=3,a_z=3,m_A=0.5,m_SA=4.575,h_A=0.5,l_A=0.1,l_SA=1.25,width_SA=0.03, g=9.81):
    # -------------------- XY PLANE --------------------
    # --- From System FBD ---

    R_x = a_x * (m_A + m_SA)

    R_y = g * (m_A + m_SA) + a_y * (m_A + m_SA)

    M_1 = m_SA*g * (l_A - width_SA / 2) + m_A*g * (l_A / 2) + a_y * (m_SA * (l_A - width_SA / 2) + m_A * (l_A / 2)) -a_x * (m_SA * (l_A - width_SA / 2))

    # --- From Attachment FBD ---

    N_x = R_x - m_A * a_x

    N_y = R_y - m_A * g - m_A * a_y

    # --- From Solar Array FBD --- UNNECESSARY

    M_2 = m_SA * a_x * (l_SA / 2)

    # -------------------- XY PLANE --------------------
    # --- From System FBD ---

    M_3 = m_SA * a_z * (l_A - width_SA/2) + m_A * a_z * l_A/2

    M_5 = -m_SA * a_z * (l_SA/2 - h_A/2)

    R_z = (m_A + m_SA) * a_z

    # --- From Solar Array FBD --- 

    M_6 = -(l_SA/2 * m_SA * a_z)

    M_4 = 0

    N_z = m_A * a_z
    #change of coordinate systems
    
    loads = { 
    "R_x": 149.4, #R_z,
    "R_y": 149.4, #R_x,
    "R_z": 473, #R_y,
    "N_x": 134.6,#N_z,
    "N_y": 134.6,#N_x,
    "N_z": 426.4,#N_y,
    "M_1": 84.2,#M_3,
    "M_2": 84.2,#M_1,
    "M_3": 27.1, #M_2,
    "M_4": M_6,
    "M_5": M_4,
    "M_6": M_5
    }
    return loads
    #return R_x, R_y, R_z, N_x, N_y, N_z, M_1, M_2, M_3, M_4, M_5, M_6

