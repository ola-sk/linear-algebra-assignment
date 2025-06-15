import numpy as np

from src.vectors import Vector3D, edge_3d

def create_cube(size: float = 1, origin: Vector3D = Vector3D.create((0, 0, 0))) -> np.ndarray:
    half_size = size / 2
    cube = np.array([
        # top

        # alongside x axis
        edge_3d(
            Vector3D.create((half_size, half_size, half_size), origin),
            Vector3D.create((-half_size, half_size, half_size), origin)
        ),
        edge_3d(
            Vector3D.create((half_size, half_size, -half_size), origin),
            Vector3D.create((-half_size, half_size, -half_size), origin)
        ),
        # alongside z axis
        edge_3d(
            Vector3D.create((half_size, half_size, half_size), origin),
            Vector3D.create((half_size, half_size, -half_size), origin),
        ),
        edge_3d(
            Vector3D.create((-half_size, half_size, half_size), origin),
            Vector3D.create((-half_size, half_size, -half_size), origin)
        ),

        # bottom

        # alongside x axis
        edge_3d(
            Vector3D.create((half_size, -half_size, half_size), origin),
            Vector3D.create((-half_size, -half_size, half_size), origin)
        ), # front
        edge_3d(
            Vector3D.create((half_size, -half_size, -half_size), origin),
            Vector3D.create((-half_size, -half_size, -half_size), origin)
        ), # back
        # alongside z axis
        edge_3d(
            Vector3D.create((half_size, -half_size, half_size), origin),
            Vector3D.create((half_size, -half_size, -half_size), origin),
        ), # right
        edge_3d(
            Vector3D.create((-half_size, -half_size, half_size), origin),
            Vector3D.create((-half_size, -half_size, -half_size), origin),
        ), # left

        # connecting top and bottom
        edge_3d(
            Vector3D.create((half_size, half_size, half_size), origin),
            Vector3D.create((half_size, -half_size, half_size), origin)
        ), # front-right
        edge_3d(
            Vector3D.create((-half_size, half_size, half_size), origin),
            Vector3D.create((-half_size, -half_size, half_size), origin)
        ), # front-left
        edge_3d(
            Vector3D.create((half_size, half_size, -half_size), origin),
            Vector3D.create((half_size, -half_size, -half_size), origin)
        ), # back-right
        edge_3d(
            Vector3D.create((-half_size, half_size, -half_size), origin),
            Vector3D.create((-half_size, -half_size, -half_size), origin)
        ), # back-left
    ])
    print("Cube created with following edges: \n", cube)
    return cube

create_cube()
