# --- Constants ---
g_0 = 9.81
g = 9.81 # Change depending on height

# --- Initialize all variables ---
a_x = 8.5 * g_0
a_y = 3 * g_0
m_A = 0
m_SA = 0
l_A = 0
l_a = 0
l_SA = 0
omega_SA = 0

# --- From System FBD ---

R_x = a_x * (m_A + m_SA)

R_y = g * (m_A + m_SA) + a_y * (m_A + m_SA)

M_1 = m_A*g * (l_A - m_SA*g / 2) + m_A*g * (l_A / 2) + a_y * (m_SA * (l_a - omega_SA / 2) + m_A * (l_A / 2)) -a_x * (m_SA * (l_a - omega_SA / 2))

# --- From Attachment FBD ---

N_x = R_x - m_A * a_x

N_y = R_y - m_A * g - m_A * a_y

M_2 = m_A*g * (l_A / 2) + N_y * (l_A - omega_SA / 2) + m_A * a_y * (l_A / 2) - M_1

# --- From Solar Array FBD --- UNNECESSARY

# eq7 = (N_x == m_SA * a_x)
# eq8 = (N_y - W_SA == m_SA * a_y)
# eq9 = (-M_2 == -m_SA * a_x * (l_SA / 2))

# PLEASE DOUBLE CHECK FORMULAS
