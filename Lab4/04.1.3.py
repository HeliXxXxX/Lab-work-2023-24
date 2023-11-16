from math import pi

def sphere_volume(r):
    ans = (4/3) * pi * r**3
    print(ans)
    return ans

def sphere_surface(r):
    ans = 4 * pi * r**2
    print(ans)
    return ans

def cylinder_volume(r, h):
    ans = pi * r * 2 * h
    print(ans)
    return ans

def cylinder_surface(r, h):
    ans = 2 * pi * r * (r + h)
    print(ans)
    return ans

def cone_volume(r, h):
    ans = (1/3) * pi * r * 2 * h
    print(ans)
    return ans

def cone_surface(r, h):
    ans = pi * r * h + pi * r * 2
    print(ans)
    return ans

