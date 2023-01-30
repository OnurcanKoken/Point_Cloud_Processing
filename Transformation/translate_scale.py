import copy
import open3d as o3d

# read the point cloud
pcd = o3d.io.read_point_cloud("../../test_data/fragment.pcd")
origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

# The translate method takes a single 3D vector "t" as input and
# translates all points/vertices of the geometry by this vector, v_t = v + t.

# x y z -> red green blue
pcd_tx = copy.deepcopy(pcd).translate((1.3, 0, 0)) # x direction
pcd_ty = copy.deepcopy(pcd).translate((0, 1.3, 0)) # y direction
pcd_tz = copy.deepcopy(pcd).translate((0, 0, 1.3)) # z direction

pcd.paint_uniform_color([1, 0, 0])              # red
pcd_tx.paint_uniform_color([1, 0.706, 0])       # yellow
pcd_ty.paint_uniform_color([0, 0.651, 0.929])   # blue
pcd_tz.paint_uniform_color([0, 0.951, 0])       # green

o3d.visualization.draw_geometries([pcd, pcd_tx, origin])

# Scale
# Vertices and points of Open3D geometry types can also be scaled using scale, v_s = s⋅v.
# get_center() is used to get the actual center of points in the point cloud, not the
# center parameter is set to True by default. If it is set to False,
# then the object is not centered prior to scaling
# such that the center of the object can move due to the scaling operation.
pcd_scaled = copy.deepcopy(pcd).scale(0.5, center=pcd.get_center())
pcd_scaled.paint_uniform_color([0, 0, 1])              # blue

o3d.visualization.draw_geometries([pcd, pcd_scaled, origin])

# Reference: http://www.open3d.org/docs/0.10.0/tutorial/Basic/transformation.html
# access date: 30.01.2023