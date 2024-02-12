# workbench
"""To find the specified number of nearest points from the long_list 
    to each point in the short_list and to plot them in three dimensions, 
    you can use the scipy.spatial.distance module for calculating distances
      and matplotlib for plotting. 
"""

import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_nearest_points(short_list, k_number, long_list):
    nearest_points = []

    for short_point in short_list:
        distances = cdist([short_point], long_list)
        nearest_indices = np.argsort(distances)[0][:k_number]
        nearest_points.append([long_list[i] for i in nearest_indices])

    return nearest_points

def plot_points(short_list, long_list, nearest_points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    short_list = np.array(short_list)
    long_list = np.array(long_list)

    ax.scatter(short_list[:, 0], short_list[:, 1], short_list[:, 2], c='r', marker='o', label='Short List')
    ax.scatter(long_list[:, 0], long_list[:, 1], long_list[:, 2], c='b', marker='x', label='Long List')

    for i, nearest_set in enumerate(nearest_points):
        nearest_set = np.array(nearest_set)
        ax.scatter(nearest_set[:, 0], nearest_set[:, 1], nearest_set[:, 2], s=50, alpha=0.5, label=f'Nearest to Short Point {i + 1}')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.legend()

    plt.show()

# Example data:
short_list = [(0,0,0), (1,1,1), (2,2,2)]
k_nearest = 2
long_list = [(0,0,1), (0,1,1), (1,1,2), (1,2,2), (2,1,0), (2,2,3), (2,2,1)]

nearest_points = find_nearest_points(short_list, k_number, long_list)
plot_points(short_list, long_list, nearest_points)


      

