import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



#2D circle
center = (0, 0)
radius = 3
theta = np.linspace(0, 2*np.pi, 100)

x = radius * np.cos(theta) + center[0]
y = radius * np.sin(theta) + center[1]

plt.figure(figsize=(6, 6)) 
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Circle')
plt.grid(True)
plt.axis('equal') 
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



#3D circle
circle_radius = 3 
circle_center = (0, 0, 0)  
circle_theta = np.linspace(0, 2 * np.pi, 100)
circle_x = circle_radius * np.cos(circle_theta) + circle_center[0]
circle_y = circle_radius * np.sin(circle_theta) + circle_center[1]
circle_z = np.zeros_like(circle_x) + circle_center[2]

ax.plot(circle_x, circle_y, circle_z, color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Circle')

plt.show()



#3D shere
center = (0, 0, 0)
radius = 5 

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

theta, phi = np.meshgrid(theta, phi)
x = radius * np.sin(theta) * np.cos(phi) + center[0]
y = radius * np.sin(theta) * np.sin(phi) + center[1]
z = radius * np.cos(theta) + center[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', alpha=.4)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Sphere')

plt.show()
