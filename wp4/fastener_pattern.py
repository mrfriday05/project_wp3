# As for the 27.11 this is almost working :>, 
#NOTE : THIS TEST WORKS ONLY FOR METAL 
#NOTE : THIS TEST INCLUDES ONLY 4 fasteners in the symmetrical array 
from lug import  Lug # imports the lug object

# pattern_check : takes the size of the lug and the placement of the fasteners and checks if it complies with the expectations

def pattern_check (lug, xdist_lug,zdist_lug): # req arguments: lug (object), xdist_lug and zdist_lug (these are the fasteners' centers ) 
    
   # ___ OLD (BACKUP)____
    #x_length = lug.x_length
    #z_length = lug.z_length
    #x_coordinate = lug.fastenerlst[0].x
    #z_coordinate = lug.fastenerlst[0].z
    #d2 = lug.D2
    #e1 = e2 = 1.5 * d2
    
   #___ NEW ___
    x_length = lug.x_length
    z_length = lug.z_length
    x_coordinate = xdist_lug
    z_coordinate = zdist_lug
    d2 = lug.D2
    e1 = e2 = 1.5 * d2
    
# ___ FROM READER ___
# the fastener spacing, center to center, should be 2-3xD2
# the edge distance (distance between edge of the plate and nearest fastener should be minimum 1.5 D2). These are represented as e1 and e2.

    if abs(x_coordinate) > (x_length / 2 - e2) or abs(z_coordinate) > (z_length / 2 - e1) or abs(x_coordinate)*2 < 3*d2 or abs(z_coordinate)*2 < 3*d2:
        return False
    else:
        return True
