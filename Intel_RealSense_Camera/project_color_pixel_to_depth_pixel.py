import pyrealsense2 as rs

# Create a pipeline
pipeline = rs.pipeline()

# Create a config and configure the pipeline to stream
#  different resolutions of color and depth streams
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
profile = pipeline.start(config)

# There values are needed to calculate the mapping
depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
print("Depth Scale is: " , depth_scale)

depth_min = 0.11 #meter
depth_max = 1.0 #meter

# get frames, noticed that it is not aligned, test if it works well, otherwise align them
frames = pipeline.wait_for_frames()
depth_frame = frames.get_depth_frame()
color_frame = frames.get_color_frame()

depth_intrin = profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()
color_intrin = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()

depth_to_color_extrin =  profile.get_stream(rs.stream.depth).as_video_stream_profile().get_extrinsics_to( profile.get_stream(rs.stream.color))
color_to_depth_extrin =  profile.get_stream(rs.stream.color).as_video_stream_profile().get_extrinsics_to( profile.get_stream(rs.stream.depth))

color_points = [
    [400.0, 150.0],
    [560.0, 150.0],
    [560.0, 260.0],
    [400.0, 260.0]
]
depth_point_ = []

for color_point in color_points:
   depth_point_.append(
       rs.rs2_project_color_pixel_to_depth_pixel(
           depth_frame.get_data(), depth_scale, depth_min, depth_max,
           depth_intrin, color_intrin, depth_to_color_extrin, color_to_depth_extrin, color_point)
   )

# Reference: https://github.com/IntelRealSense/librealsense/issues/5603#issuecomment-574019008
# access date: 04.02.2023