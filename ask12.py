# Convex hull of a random set of points:

import numpy as np
from scipy.spatial import ConvexHull
points = np.random.rand(30, 2)   # 30 random points in 2-D
hull = ConvexHull(points)

# Plot it:

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# We could also have directly used the vertices of the hull, which
# for 2-D are guaranteed to be in counterclockwise order:

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')

points2 = np.random.rand(1000, 2)

def in_hull(p, hull):
    from scipy.spatial import Delaunay
    if not isinstance(hull,Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p)>=0

maxpoint = np.amax(points, axis = 0)

maxxx = maxpoint[0]
maxxy = maxpoint[1]

minpoint = np.amin(points, axis = 0)

minxxx = minpoint[0]
minxxy = minpoint[1]

sidex = maxxx - minxxx
sidey = maxxy - minxxy

Embsqr = sidex*sidey

points3 = in_hull(points2, points)

e = np.count_nonzero(points3)


Embpoly = (e/1000.0)*Embsqr
print "To embadon einai ", Embpoly



