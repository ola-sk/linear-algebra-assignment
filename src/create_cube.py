from src.vectors import Vector3D, edge_3d

def create_cube(size: float = 1, origin: Vector3D = Vector3D.create((0, 0, 0))) -> list[
    tuple[Vector3D[float], Vector3D[float]]]:
    half_size = size / 2
    cube = [
        # top

        # x
        edge_3d(
            Vector3D.create((half_size, half_size, half_size), origin),
            Vector3D.create((-half_size, half_size, half_size), origin)
        ),
        edge_3d(
            Vector3D.create((half_size, half_size, -half_size), origin),
            Vector3D.create((-half_size, half_size, -half_size), origin)
        ),
        # z
        edge_3d(
            Vector3D.create((half_size, half_size, half_size), origin),
            Vector3D.create((half_size, half_size, -half_size), origin),
        ),
        edge_3d(
            Vector3D.create((-half_size, half_size, half_size), origin),
            Vector3D.create((-half_size, half_size, -half_size), origin)
        ),
        # bottom

        # x
        edge_3d(
            Vector3D.create((half_size, -half_size, half_size), origin),
            Vector3D.create((-half_size, -half_size, half_size), origin)
        ),
        edge_3d(
            Vector3D.create((half_size, -half_size, -half_size), origin),
            Vector3D.create((-half_size, -half_size, -half_size), origin)
        ),
        # y
        edge_3d(
            Vector3D.create((half_size, -half_size, half_size), origin),
            Vector3D.create((half_size, -half_size, -half_size), origin),
        ),
        edge_3d(
            Vector3D.create((-half_size, -half_size, half_size), origin),
            Vector3D.create((-half_size, -half_size, -half_size), origin),
        )
    ]
    print("Qube created with following edges: \n", cube)
    return cube

create_cube()
