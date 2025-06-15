from vectors import Vector3D, edge_3d
from src.create_cube import create_cube

if __name__ == '__main__':
    origin = Vector3D.create([2, 2, 1])  # Use the create method
    cube = create_cube(1, origin)