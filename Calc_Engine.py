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

def find_axis(con_pts):
    x_cords = con_pts[:, 0]
    y_cords = con_pts[:, 1]

    x_axis = (x_cords.max() + x_cords.min()) / 2
    y_axis = (y_cords.max() + y_cords.min()) / 2

    height = y_cords.max() - y_cords.min()
    width = x_cords.max() - x_cords.min()

    orientation = 'Top - Bottom' if height > width else 'left - right'

    return x_axis, y_axis, orientation
def washer_method():
    pass

def compute_vol():
    pass

def rotate_solid():
    pass

