from lug import  Lug

def pattern_check ():
    x_length = Lug.x_length
    z_length = Lug.y_length
    x = Lug.x
    z = Lug.y
    d2 = Lug.D2
    e1 = e2 = 1.5 * d2

    if abs(x) > (x_length / 2 - e2) or abs(y) > (y_length / 2 - e1):
        return False
    else:
        return True
    
    
