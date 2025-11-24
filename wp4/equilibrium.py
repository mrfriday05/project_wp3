# --- Constants ---
g_0 = 9.81
g = 9.81 # Change depending on height

# --- Initialize all variables ---
# --- ACCELERATIONS
a_x = 8.5 * g_0
a_y = 3 * g_0
a_z = a_x           # NOTE: a_z nad a_x have the same magnitude but act in different directions and can have different signs
# ---MASSES
m_A = 0.5
m_SA = 9.15
# --- Dimensions 
l_A = 0.2 #  [mm]
l_SA = 0
w_SA = 0.03
h_A = 2


# -------------------- XY PLANE --------------------
# --- From System FBD ---

R_x = a_x * (m_A + m_SA)

R_y = g * (m_A + m_SA) + a_y * (m_A + m_SA)

 - w_SA / 2) + m_A*g * (l_A / 2) + a_y * (m_SA * (l_A - o_SA / 2) + m_A * (l_A / 2)) -a_x * (m_SA * (l_A - w_SA / 2))

# --- From Attachment FBD ---

N_x = R_x - m_A * a_x

N_y = R_y - m_A * g - m_A * a_y

M_2 = m_A*g * (l_A / 2) + N_y * (l_A - w_SA / 2) + m_A * a_y * (l_A / 2) - M_1


# -------------------- XZ PLANE --------------------
# --- From System FBD ---

R_z = (m_A + m_SA) * a_z

M_5 = -m_SA * a_z * (L_SA / 2 - h_a / 2)

M_3 = m_SA * a_z * (L_A - w_SA / 2) + m_A * a_z * L_A / 2

# --- From Attachment FBD ---

N_z = R_z - m_A * a_z

M_6 = -m_SA * a_z * (L_SA / 2 - h_a / 2)

M_4 = -(M_3 + R_z * (L_A - w_SA / 2) + m_A * a_z * (L_A / 2 - w_SA / 2))

def get_eq(N_x, N_y, N_z):
    return N_x, N_y, N_z
# --- From Solar Array FBD --- UNNECESSARY

# eq7 = (N_x == m_SA * a_x)
# eq8 = (N_y - W_SA == m_SA * a_y)
# eq9 = (-M_2 == -m_SA * a_x * (l_SA / 2))

# PLEASE DOUBLE CHECK FORMULAS

print(M_2)