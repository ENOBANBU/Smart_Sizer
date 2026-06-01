import numpy as np

def disk_method(x_cords, r_cords):

    return np.trapz(np.pi * r_cords**2, x_cords)