import open3d as o3d 
# ICP (Iterative Closest Point)
# The input are two point clouds and an initial transformation that roughly aligns the source point cloud to the target point cloud. 
# The output is a refined transformation that tightly aligns the two point clouds. 

# visualizes a target point cloud and a source point cloud transformed with an alignment transformation
def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source) # use it not to change the original point cloud
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])

demo_icp_pcds = o3d.data.DemoICPPointClouds() # if you cant download, just use any point cloud, give the path in str format, read_point_cloud("pcd_path")
source = o3d.io.read_point_cloud(demo_icp_pcds.paths[0])
target = o3d.io.read_point_cloud(demo_icp_pcds.paths[1])
threshold = 0.02
trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                         [-0.139, 0.967, -0.215, 0.7],
                         [0.487, 0.255, 0.835, -1.4], [0.0, 0.0, 0.0, 1.0]])
draw_registration_result(source, target, trans_init)

print("Initial alignment")
evaluation = o3d.pipelines.registration.evaluate_registration(
    source, target, threshold, trans_init)
print(evaluation)
# fitness, which measures the overlapping area (# of inlier correspondences / # of points in target). The higher the better.
# inlier_rmse, which measures the RMSE of all inlier correspondences. The lower the better.

# In case if you dont have the normals for the point cloud,
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=16), fast_normal_computation=True)

############################ Point-to-Point ICP
print("Apply point-to-point ICP")
reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)

# By default, registration_icp runs until convergence or reaches a maximum number of iterations (30 by default). 
# It can be changed to allow more computation time and to improve the results further.
reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)

############################ Point-to-Plane ICP
# uses a different objective function
# The point-to-plane ICP algorithm uses point normals. 
# In this tutorial, we load normals from files. If normals are not given, they can be computed with Vertex normal estimation.
# mesh.compute_vertex_normals()

print("Apply point-to-plane ICP")
reg_p2l = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPlane())
print(reg_p2l)
print("Transformation is:")
print(reg_p2l.transformation)
draw_registration_result(source, target, reg_p2l.transformation)

# Reference: http://www.open3d.org/docs/release/tutorial/pipelines/icp_registration.html
# access date: 13.01.2023