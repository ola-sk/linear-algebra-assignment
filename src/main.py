from vectors import Vector3D
from src.create_cube import create_cube
from src.visualise_cube import visualize_cube
from src.transformations import rotate
import numpy as np

if __name__ == '__main__':
    origin = Vector3D.create([2, 2, 1])  # Use the create method
    cube = create_cube(1, origin)

    rotation_matrix = rotate(45, 0, 1)
    rotation_matrix2 = rotate(45, 0, 2)
    rotated_matrix = []
    for edge in cube:
        rotated_matrix.append((rotation_matrix @ edge.T).T)
    rotated_ndarray = np.array(rotated_matrix)
    visualize_cube(rotated_ndarray)
