from math import *

def circle_to_square(u, v):
    u2 = u * u
    v2 = v * v
    twosqrt2 = 2.0 * sqrt(2.0)
    subtermx = 2.0 + u2 - v2
    subtermy = 2.0 - u2 + v2
    termx1 = subtermx + u * twosqrt2
    termx2 = subtermx - u * twosqrt2
    termy1 = subtermy + v * twosqrt2
    termy2 = subtermy - v * twosqrt2

    sqrt_termx1 = sqrt(max(0, termx1))
    sqrt_termx2 = sqrt(max(0, termx2))
    sqrt_termy1 = sqrt(max(0, termy1))
    sqrt_termy2 = sqrt(max(0, termy2))
    
    x = 0.5 * sqrt_termx1 - 0.5 * sqrt_termx2
    y = 0.5 * sqrt_termy1 - 0.5 * sqrt_termy2
    
    return x, y

def convert_coordinates(radius, u, v):
    u_normalized = u / radius
    v_normalized = v / radius
    
    x_normalized, y_normalized = circle_to_square(u_normalized, v_normalized)
    
    x = x_normalized * radius
    y = y_normalized * radius
    
    return x, y

def main():
    radius = 256
    
    #input coords, u=x, v=y
    u = float(-60)
    v = float(160)
    
    x, y = convert_coordinates(radius, u, v)
    
    print(f"Input (u, v): ({u}, {v})")
    print(f"Output (x, y): ({x:.2f}, {y:.2f})")

main()
