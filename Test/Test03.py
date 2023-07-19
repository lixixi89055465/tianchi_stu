from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
z = X ** 2 + Y ** 2


C=plt.contour(x, y,z,[2,5,8,10])
plt.clabel(C, inline=True, fontsize=10)

fig=plt.figure()
fig = plt.figure(figsize=(10,10))
ax1 = plt.axes(projection='3d')

ax1.scatter3D(X,Y,z, cmap='Blues')

print("0"*100)
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
z = (np.exp(-X**2 - Y**2) - np.exp(-(X - 1)**2 - (Y - 1)**2))*2

fig=plt.figure()
fig = plt.figure(figsize=(10,10))
ax1 = plt.axes(projection='3d')
ax1.scatter3D(X,Y,z, cmap='Blues')
plt.show()
