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

def washer_method(x_pos, big_R, lit_R ):
    lit_R = min(lit_R, big_R)
    return np.trapz(np.pi * (big_R**2 - lit_R**2), x_pos)

def compute_vol(x_cords, big_R, lit_R = None):
    if lit_R is None or np.all(lit_R == 0):
        return disk_method(x_cords, big_R)
    else: 
        return washer_method(x_cords, big_R, lit_R)

def rotate_solid(con_px, pixel_cm, inner_con_px = None):
    con_cm = convert_pix(np.array(con_px), pixel_cm)

    x_axis, y_axis, orientation = find_axis(con_cm)

    if orientation == 'Top - Bottom':
        x_vals = con_cm[:, 1]
        big_R = np.abs(con_cm[:, 0] - x_axis)
    else:
        x_vals = con_cm[:, 1]
        big_R = np.abs(con_cm[:, 1] - y_axis)

    sort_idx = np.argsort(x_vals)
    x_vals = x_vals[sort_idx]
    big_R = big_R[sort_idx]

    if inner_con_px is not None:
        in_cm = convert_pix(np.array(inner_con_px), pixel_cm)
        if orientation == 'Top - Bottom':
            Lit_R = np.abs(in_cm[:, 0] - x_axis)
        else:
            Lit_R = np.abs(in_cm[:, 1] - y_axis)

            Lit_R = np.interp(x_vals, np.sort(in_cm[:, 1]), Lit_R[np.argsort(in_cm[:, 1])])
            return compute_vol(x_vals, big_R, Lit_R)
        
    return compute_vol(x_vals, big_R)