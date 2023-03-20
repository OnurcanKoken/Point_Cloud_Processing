import numpy as np
import open3d as o3d

pcd1 = o3d.io.read_point_cloud("data\DemoICPPointClouds\cloud1.pcd")

origin = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.5)

vis = o3d.visualization.VisualizerWithEditing()
vis.create_window()
vis.add_geometry(pcd1)
vis.run()

vis.destroy_window()
print(vis.get_picked_points())

# for example:
#pcd_point_index = [68461, 34211, 32476, 109543, 82416, 77840, 72361, 63780, 27196, 31052, 92, 2604, 79505, 91671, 113529, 59625]
#cloud_points = np.asarray(pcd1.points)
#for i in range(len(pcd_point_index)):
#    # print each point corresponding to each index
#    print(cloud_points[pcd_point_index[i]])

# Reference: https://stackoverflow.com/questions/56183844/how-can-we-pick-3d-points-from-point-cloud-data-from-a-pcd-file-using-python
# access date: 17.02.2023

# for VisualizerWithEditing: https://github.com/isl-org/Open3D/blob/d7341c4373e50054d9dbe28ed84c09bb153de2f8/src/Visualization/Visualizer/VisualizerWithEditing.cpp#L124
# acess date: 20.03.2023
