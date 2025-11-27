from lug import  Lug


#NOTE : THIS TEST WORKS ONLY FOR METAL 
def pattern_check (lug, xdist_lug,):
    x_length = lug.x_length
    z_length = lug.z_length
    x = lug.fastenerlst[0].x
    z = lug.fastenerlst[0].z
    d2 = lug.D2
    e1 = e2 = 1.5 * d2

    if abs(x) > (x_length / 2 - e2) or abs(z) > (z_length / 2 - e1) or abs(x)*2 < 3*d2 or abs(z)*2 < 3*d2:
        return False
    else:
        return True