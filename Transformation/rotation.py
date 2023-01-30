import copy
import numpy as np
import open3d as o3d
# read the point cloud
pcd = o3d.io.read_point_cloud("../../test_data/fragment.pcd")
origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

"""
It takes as first argument a rotation matrix R. 
As rotations in 3D can be parametrized in a number of ways, 
Open3D provides convenience functions to convert from different parametrizations to rotation matrices:
- Convert from Euler angles with get_rotation_matrix_from_xyz (where xyz can also be of the form yzx zxy, xzy, zyx, and yxz)
- Convert from Axis-angle representation with get_rotation_matrix_from_axis_angle
- Convert from Quaternions with get_rotation_matrix_from_quaternion
"""
# x y z -> red green blue -> pitch roll yaw

# 1. Euler angles
# simplest but mind "gimbal lock" or "wrist flip" problem, where parallel axes occur
R_1 = pcd.get_rotation_matrix_from_xyz((0, 0, -0.250 * np.pi))

# 2. Axis-angle representation
# axis direction and angle
# robustness against singularities
R_2 = pcd.get_rotation_matrix_from_axis_angle((0, 0, -0.250 * np.pi))

# 3. Quaternions
# 4 parameters, w x y z, w is the scalar part, the rest is the vector part
# most efficient computation compared to 1 and 2.
# robustness against singularities
R_3 = pcd.get_rotation_matrix_from_quaternion((0, 0, 0, 0))

# rotate, 3 by 3 matrix
rotated_pcd = copy.deepcopy(pcd).rotate(R_1, center=(0, 0, 0))

pcd.paint_uniform_color([1, 0.706, 0])              # yellow
rotated_pcd.paint_uniform_color([0, 0.651, 0.929])  # blue

o3d.visualization.draw_geometries([pcd, rotated_pcd, origin])

# Reference: http://www.open3d.org/docs/0.10.0/tutorial/Basic/transformation.html
# access date: 30.01.2023