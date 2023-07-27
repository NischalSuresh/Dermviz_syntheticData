# creates a 3d scatter plot of the lesion with z axis being the brightness value of the pixel
import cv2
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

image_path = '/Users/ngandige/Documents/Veytel/Dermviz/Synthetic_data/snippets/G16_2003_03_31_001043_000266 (1).jpg'  # Replace with the actual image file path
image_bgr= cv2.imread(image_path)

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

y, x = np.meshgrid(range(image_gray.shape[1]), range(image_gray.shape[0]))
z_gray = image_gray


x_flat = x.flatten()
y_flat = y.flatten()
z_gray_flat = z_gray.flatten()
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
image_rgb = image_rgb.astype(float) / 255.0 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_flat, y_flat,z_gray_flat,c=image_rgb.reshape(-1,3), s=0.1)  
# ax.axis('off')
ax.set_title('Scatter Plot of lesion')
plt.show()