import matplotlib.pyplot as plt
# for typing
from matplotlib.figure import Figure
from numpy import ndarray
# for the default value of `cube`—the arg to `visualise_cube` function.
from src.create_cube import create_cube


def visualize_cube(cube: ndarray = create_cube(size=1), color: str = 'violet'):
    # Initialize the 3D plot
    fig: Figure = plt.figure()
    # specify placement of the plot on canvas and its projection
    ax = fig.add_subplot(111, projection='3d')

    # Plot each edge
    for edge in cube:
        ax.plot(edge[:, 0], edge[:, 1], edge[:, 2], color=color)

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()
