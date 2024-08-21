import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to generate the vertices of a 4D hypercube
def generate_hypercube_vertices():
    return np.array([[x, y, z, w] for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] for w in [-1, 1]])

# Function to rotate the hypercube in 4D space
def rotate_hypercube(vertices, angle1, angle2):
    rotation_matrix_1 = np.array([
        [np.cos(angle1), 0, 0, np.sin(angle1)],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-np.sin(angle1), 0, 0, np.cos(angle1)]
    ])
    
    rotation_matrix_2 = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle2), 0, np.sin(angle2)],
        [0, 0, 1, 0],
        [0, -np.sin(angle2), 0, np.cos(angle2)]
    ])
    
    return np.dot(np.dot(vertices, rotation_matrix_1), rotation_matrix_2)

# Function to project 4D vertices onto 3D space
def project_to_3d(vertices):
    projection_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])
    return np.dot(vertices, projection_matrix.T)

# Generate the vertices of a hypercube
vertices = generate_hypercube_vertices()

# Prepare the figure and 3D axis for animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    
    # Rotate the hypercube
    rotated_vertices = rotate_hypercube(vertices, np.radians(frame), np.radians(frame / 2))
    
    # Project to 3D
    projected_vertices = project_to_3d(rotated_vertices)
    
    # Plot the vertices
    ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2])

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 360, 2), interval=50)

plt.show()
