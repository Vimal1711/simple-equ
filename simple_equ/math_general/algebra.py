import math

def power(base: int | float, exponent: int | float) -> int | float:
    return base ** exponent

#Takes a number and until it is equal to 0 it multiplies it with its previous in order storing the new result.
def factorial(number: int | float):
    result = 1
    while number > 0:
        result *= number
        number -= 1    
    return result

#Implementation based on the Eucledean algorithm.
def gcd(a: int | float, b: int | float):
    if b == 0: 
        return a
    return gcd(b, a % b)

#Use Newton's method to closely approximate the square root of a number
def sqrt(number: int | float):
    if number > 0:
       x = number 
       tolerance = 0.000000000001

       while True: 
           next = (x + number / x) / 2

           if abs(next - x) < tolerance: 
               return next
           
           x = next
    elif number == 0: 
        return 0; 
    else: 
        raise ValueError("Not a real number")
    
def cbrt(x):
    return x**(1/3) if x >= 0 else -(-x)**(1/3)

#Forms of basic linear,quadratic and cubic equations
def basic_quadratic(a: int | float, b: int | float, c: int | float): 
    d = (b**2) - (4*a*c)
    sqrt_d = sqrt(d)

    root1 = (-b + sqrt_d) / (2*a)
    root2 = (-b - sqrt_d) / (2*a)
    return root1, root2

def basic_qubic(a: int | float, b: int | float, c: int | float, d: int | float):
    q = (2 * b**3 - 9*a*b*c + 27*a*a*d) / (27 * a**3)
    p = (3 * a * c - (b*b)) / (3 * (a*a))

    delta = (q/2)**2 + (p/3)**3

    roots = []

    if delta >= 0:
        sqrt_delta = sqrt(delta)
        t1 = cbrt(-q/2 + sqrt_delta)
        t2 = cbrt(-q/2 - sqrt_delta)
        t = t1 + t2

        #Real root 
        x1 = t - (b / (3*a))
        roots.append(x1)

        # 2 Complex roots using cube roots of unity
        omega = complex(-0.5, sqrt(3)/2)
        x2 = t1*omega + t2*omega.conjugate() - (b / (3*a))
        x3 = t1*omega.conjugate() + t2*omega - (b / (3*a))
        roots.extend([x2, x3])

    else: 
        #Three real square roots (trig solution)
        r = sqrt(-p/3)
        phi = math.acos(-q/(2*r**3))
        #All real
        x1 = 2*r*math.cos(phi/3) - b/(3*a)
        x2 = 2*r*math.cos((phi + 2*math.pi)/3) - b/(3*a)
        x3 = 2*r*math.cos((phi + 4*math.pi)/3) - b/(3*a)
        roots.extend([x1, x2, x3])

    #It just removes the artifacts from floating point innacuracies here 
    roots = [round(x, 10) for x in roots]
    return roots

def basic_linear(a: int | float, b: int | float):
    x = -b/a
    return x

def is_divisible(a: int | float, b: int | float) -> bool:
    # Checks if a is divisible by b by checking if the remainder of a divided by b is 0.
    # Raise ValueError if b is zero.

    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b == 0
