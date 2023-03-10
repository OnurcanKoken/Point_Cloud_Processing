import open3d as o3d

def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (green): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0, 1, 0])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("../../test_data/ICP/cloud_bin_2.pcd")
o3d.visualization.draw_geometries([pcd])

# Voxel Downsampling
print("Downsample the point cloud with a voxel of 0.02")
voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.02)
o3d.visualization.draw_geometries([voxel_down_pcd])

# Uniform Downsampling
print("Every 5th points are selected")
uni_down_pcd = pcd.uniform_down_sample(every_k_points=5)
o3d.visualization.draw_geometries([uni_down_pcd])

# Statistical outlier removal
print("Statistical oulier removal")
cl, ind = voxel_down_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
display_inlier_outlier(voxel_down_pcd, ind)

# Radius outlier removal
print("Radius oulier removal")
cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)
display_inlier_outlier(voxel_down_pcd, ind)

# Reference: http://www.open3d.org/docs/latest/tutorial/Advanced/pointcloud_outlier_removal.html
# access date: 11.01.2023




