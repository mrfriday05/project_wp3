

def MOI_PIN (lug):

    w = lug.z_length
    D1 = lug.D1
    b = lug.t1
    h = (w-D1)/2
    d = D1/2 + h/2
    MOI = 2 * ((b * h^3)/12) + (b*h) * d**2

    return MOI 