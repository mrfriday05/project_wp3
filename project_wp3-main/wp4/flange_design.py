import math
# Constants
K_t = 1
M_s = 0.85
ratio_W_D = 1.5
ratio_e_D = 0.75
ratio_D_t = 4


def lug_flange_dimensions(w):  # getting dimensions from ratios
    d = w / ratio_W_D
    t = d / ratio_D_t
    e = ratio_e_D * d
    return d, t, e


def lug_tension(stress, w, d, t):
    a = t*(w-d)
    f = (stress * K_t * M_s * a)
    return f


def lug_bending(w, d, t, m):
    i_zz = 2*(((((w - d)/2)**3 * t)/12) + ((w - d)/2) * t * ((d/2) + ((w - d)/4))**2)
    y = (w - d)/4
    bending_stress = (m * 1000 * y)/i_zz
    return bending_stress


def check(stress, n_x, n_y, f, bending_stress):
    p = math.sqrt(n_x ** 2 + n_y ** 2)
    if p > f:
        return False
    if stress < bending_stress:
        return False

    return True
