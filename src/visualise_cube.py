import matplotlib.pyplot as plt
from src.create_cube import create_cube
import numpy as np

def visualize_cube(cube: np.ndarray = create_cube(size=1)):
    # Initialize the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each edge
    for edge in cube:
        ax.plot(edge[:, 0], edge[:, 1], edge[:, 2], color='violet')

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()
