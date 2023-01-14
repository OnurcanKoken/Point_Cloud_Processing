import json
import open3d as o3d

############## sample realsense bag file
bag_reader = o3d.t.io.RSBagReader()
bag_reader.open(bag_filename)
im_rgbd = bag_reader.next_frame()
while not bag_reader.is_eof():
    # process im_rgbd.depth and im_rgbd.color
    im_rgbd = bag_reader.next_frame()

bag_reader.close()

############## list RealSense connected devices to the system and
# get their capabilities (supported resolutions, frame rates, etc.)
o3d.t.io.RealSenseSensor.list_devices()

############## video stream
# config_filename is the RealSense configuration .json file
with open(config_filename) as cf:
    rs_cfg = o3d.t.io.RealSenseSensorConfig(json.load(cf))

rs = o3d.t.io.RealSenseSensor()
rs.init_sensor(rs_cfg, 0, bag_filename)
rs.start_capture(True)  # true: start recording with capture, record as an RS bag file
for fid in range(150): # 150 frames
    im_rgbd = rs.capture_frame(True, True)  # wait for frames and align them
    # process im_rgbd.depth and im_rgbd.color

rs.stop_capture()

# Reference: http://www.open3d.org/docs/release/tutorial/sensor/realsense.html
# access date: 14.01.2023

