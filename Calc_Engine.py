import numpy as np

def disk_method(x_cords, r_cords):

    return np.trapz(np.pi * r_cords**2, x_cords)

"""
x = np.linspace(0, 10, 100)
r = np.full(100, 5.0)
vol = disk_method(x, r)
print(f"Got: {vol:.2f}") #should print 785.40
print(f"Expected: {np.pi * 5**2 * 10:.2f}")
"""
def convert_pix(pixel_cords, pixel_cm):
    return pixel_cords/pixel_cm
