import copy
import numpy as np
import open3d as o3d

# Open3D also supports a general transformation defined by
# a 4×4 homogeneous transformation matrix using the method transform().

# read the point cloud
pcd = o3d.io.read_point_cloud("../../test_data/fragment.pcd")
origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

# 4 by 4 matrix
T = np.eye(4)
# rotation 3 by 3
T[:3, :3] = pcd.get_rotation_matrix_from_xyz((0, np.pi / 3, np.pi / 2))
# translation 3 by 1
T[0, 3] = 1
T[1, 3] = 1.3
print(T)

# perform transform operation
pcd_t = copy.deepcopy(pcd).transform(T)
pcd.paint_uniform_color([1, 0, 0])              # red
pcd_t.paint_uniform_color([0, 0, 1])              # blue
o3d.visualization.draw_geometries([pcd, pcd_t, origin])

# Reference: http://www.open3d.org/docs/0.10.0/tutorial/Basic/transformation.html
# access date: 30.01.2023