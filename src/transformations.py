import math
import numpy as np


def rotate(angle: float, dimension1: int, dimension2: int) -> np.ndarray:
    """
    dimension1 and dimension2 parameters to set the values in the rotation matrix.
    For example, if rotation happens in the XY plane, function would be called with dimension1=0 and dimension2=1.
    :param angle: angle of rotation in radians.
    :param dimension1: first dimension of rotation plane.
    :param dimension2: second dimension of rotation plane,
    :return: a rotation matrix of type numpy.ndarray.

    to apply the rotation:
    rotated_vector = rotation_matrix @ v
    Transpose appropriately.
    '@' is the operator for dot product for NumPy ndarrays.
    """
    matrix = np.identity(3)
    angle = np.radians(angle)
    matrix[dimension1, dimension1] = math.cos(angle)
    matrix[dimension1, dimension2] = -math.sin(angle)
    matrix[dimension2, dimension1] = math.sin(angle)
    matrix[dimension2, dimension2] = math.cos(angle)
    return matrix
