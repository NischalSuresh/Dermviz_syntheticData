# vislauize the brightness, R, G, B in 3 D

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

image_path = '/Users/ngandige/Documents/Veytel/Dermviz/Synthetic_data/snippets/F16_2007_02_15_002226_002711.jpg' 
image_bgr = cv2.imread(image_path)

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

y, x = np.meshgrid(range(image_gray.shape[1]), range(image_gray.shape[0]))
z = image_gray
b, g, r = cv2.split(image_bgr)
fig = plt.figure()
ax = fig.add_subplot(2,2,1, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis') 
ax.set_xlabel('X (Pixel Index)')
ax.set_ylabel('Y (Pixel Index)')
ax.set_zlabel('Brightness Value')
ax.set_title('3D Surface Plot of Image Brightness')
#red
ax_r = fig.add_subplot(2, 2, 2, projection='3d')
ax_r.plot_surface(x, y, r, cmap='Reds')
ax_r.set_xlabel('X (Pixel Index)')
ax_r.set_ylabel('Y (Pixel Index)')
ax_r.set_zlabel('Red Value')
ax_r.set_title('Red Channel')
#green
ax_g = fig.add_subplot(2, 2, 3, projection='3d')
ax_g.plot_surface(x, y, g, cmap='Greens')
ax_g.set_xlabel('X (Pixel Index)')
ax_g.set_ylabel('Y (Pixel Index)')
ax_g.set_zlabel('Green Value')
ax_g.set_title('Green Channel')
#blue
ax_b = fig.add_subplot(2, 2, 4, projection='3d')
ax_b.plot_surface(x, y, b, cmap='Blues')
ax_b.set_xlabel('X (Pixel Index)')
ax_b.set_ylabel('Y (Pixel Index)')
ax_b.set_zlabel('Blue Value')
ax_b.set_title('Blue Channel')

plt.tight_layout()

plt.show()
