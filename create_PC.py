# creates a 3d scatter plot of the lesion with z axis being the brightness value of the pixel
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
# from mpl_toolkits.mplot3d import Axes3D

# Save the point cloud as a PLY file
def save_ply(filename, points, colors):
    header = 'ply\nformat ascii 1.0\nelement vertex {}\nproperty float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nend_header\n'.format(
        len(points)
    )
    points = np.hstack((points, colors * 255)).astype(np.uint8)
    with open(filename, 'w') as f:
        f.write(header)
        np.savetxt(f, points, fmt='%d %d %d %d %d %d')

crop_image_dir = '/Users/ngandige/Documents/Veytel/Dermviz/synthetic_data/data/crops'
pointcloud_dir = '/Users/ngandige/Documents/Veytel/Dermviz/synthetic_data/data/pointclouds'
histogram_dir = '/Users/ngandige/Documents/Veytel/Dermviz/synthetic_data/data/histograms'

files = os.listdir(crop_image_dir)
files = [file for file in files if not file.startswith('.DS_Store')]

for file in tqdm(files):
    image_path = os.path.join(crop_image_dir, file)
    image_bgr= cv2.imread(image_path)
    image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    y, x = np.meshgrid(range(image_gray.shape[1]), range(image_gray.shape[0]))
    z_gray = image_gray
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_gray_flat = z_gray.flatten()
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_rgb = image_rgb.astype(float) / 255.0 
    points = np.column_stack((x_flat, y_flat, z_gray_flat))
    # print(points.shape)
    # print(image_rgb.reshape(-1,3).shape)
    ## save the point cloud as .ply
    # remove the file extension from the file name
    file_split = file.split('.')
    file_no_ext = file_split[0] + '.' + file_split[1]
    pc_file_name = file_no_ext + '_pc.ply'
    pc_save_path = os.path.join(pointcloud_dir, pc_file_name)
    save_ply(pc_save_path, points, image_rgb.reshape(-1,3))
    bins = 100
    histogram, bin_edges = np.histogram(image_gray.flatten(), bins=bins, range=[0, 256])
    histogram = histogram.astype(float) / histogram.sum()
    # plt.plot(histogram.flatten(), color='r')
    hist_file_name = file_no_ext + '_hist.png'
    hist_save_path = os.path.join(histogram_dir, hist_file_name)
    plt.bar(bin_edges[:-1], histogram, width=(256//bins), align='center', color='gray')
    plt.xlabel('Bin')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.savefig(hist_save_path)
