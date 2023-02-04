# imports
import pyrealsense2 as rs

# configure
ctx = rs.context()
# single device, or set the index of the preferred device
device = ctx.devices[0]
serial_number = device.get_info(rs.camera_info.serial_number)
config = rs.config()
config.enable_device(serial_number)

# enable streams
config.enable_stream(rs.stream.infrared, 1, 1280,720, rs.format.y8, 6)
config.enable_stream(rs.stream.infrared, 2, 1280,720, rs.format.y8, 6)

# run pipeline
pipeline = rs.pipeline()
profile = pipeline.start(config)

# Reference: https://github.com/IntelRealSense/librealsense/issues/3878#issuecomment-569550710
# access date: 04.02.2023