import math
import numpy

def rotation_matrix(angle: float, dimension1: int, dimension2: int) -> numpy.ndarray:
    """
    dimension1 and dimension2 parameters to set the values in the rotation matrix.
    For example, if rotation happens in the XY plane, function would be called with dimension1=0 and dimension2=1.
    :param angle: angle of rotation in radians.
    :param dimension1: first dimension of rotation plane.
    :param dimension2: second dimension of rotation plane,
    :return: a rotation matrix of type numpy.ndarray.

    to apply the rotation:
    rotated_vector = rotation_matrix @ v
    '@' is the operator for matrix multiplication for NumPy ndarrays.
    """
    matrix = numpy.identity(3)
    matrix[dimension1, dimension1] = math.cos(angle)
    matrix[dimension1, dimension2] = -math.sin(angle)
    matrix[dimension2, dimension1] = math.sin(angle)
    matrix[dimension2, dimension2] = math.cos(angle)
    return matrix
