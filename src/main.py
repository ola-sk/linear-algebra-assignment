from vectors import Vector3D, edge_3d

if __name__ == '__main__':
    # Create cube
    origin = Vector3D.create((0,0,0))
    vector1 = Vector3D.create((-1,-1,-1))
    edge1 = edge_3d(origin, vector1)
    print("success")
