import open3d as o3d

pcd = o3d.io.read_point_cloud("../../test_data/fragment.pcd")
plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pcd.select_by_index(inliers)
inlier_cloud.paint_uniform_color([1.0, 0, 0])
outlier_cloud = pcd.select_by_index(inliers, invert=True)
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

# Reference: http://www.open3d.org/docs/latest/tutorial/Basic/pointcloud.html#Plane-segmentation
# access date: 11.01.2023
