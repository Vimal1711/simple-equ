from . import constants
import simple_equ.algebra.algebra as algebra
from .two_dimensional import distance

def cube_area(a: int | float):
    """[Summary]: Return the volume of a cube from one edge length.

    [Description]: Multiplies the edge length by itself three times, matching
    the standard formula for the volume of a cube.

    [Usage]: Typical usage example:

        result = cube_area(3)
        print(result)
    """
    return a * a * a


def sphere_area(radius: int | float) -> float:     
    return 4 * constants.pi * (radius ** 2)


def pyramid_surface(length: int | float, width: int | float, height: int | float):
    """[Summary]: Return the surface area of a rectangular pyramid.

    [Description]: Computes the base area and the triangular side areas, then
    sums them to produce the total surface area of the pyramid.

    [Usage]: Typical usage example:

        result = pyramid_surface(3, 4, 5)
        print(result)
    """
    result = (
        length * width
        + length * algebra.sqrt((width / 2) * (width / 2) + height * height)
        + width * algebra.sqrt((length / 2) * (length / 2) + height * height)
    )
    return result


def pyramid_volume(height: int | float, length: int | float, width: int | float):
    """[Summary]: Return the volume of a rectangular pyramid.

    [Description]: Multiplies the base area by the height and divides the result
    by three to compute the pyramid's volume.

    [Usage]: Typical usage example:

        result = pyramid_volume(6, 4, 3)
        print(result)
    """
    return (length * width * height) / 3


def sphere_surface(radius: int | float):
    """[Summary]: Return the surface area of a sphere.

    [Description]: Applies the formula 4 * pi * r^2 to compute the total outer
    surface area of a sphere.

    [Usage]: Typical usage example:

        result = sphere_surface(5)
        print(result)
    """
    return 4 * constants.pi * radius**2
