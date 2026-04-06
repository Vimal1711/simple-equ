def complex_num(real_part, imagineary_part=0):
    """Create a complex number as a tuple (real, imag)"""
    return (real_part, imagineary_part)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(a, b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + a[1]*b[0]
    return (real, imag)

def magnitude(a):
    return (a[0]**2 + a[1]**2)**0.5