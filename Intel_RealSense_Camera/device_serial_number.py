import pyrealsense2 as rs

# Configure depth and color streams...
# The context encapsulates all of the devices and sensors, and provides some additional functionalities.
realsense_ctx = rs.context()
connected_devices = []
# get serial numbers of connected devices
for i in range(len(realsense_ctx.devices)):
    detected_camera = realsense_ctx.devices[i].get_info(rs.camera_info.serial_number)
    connected_devices.append(detected_camera)

# Reference: https://stackoverflow.com/questions/67976611/how-to-get-intel-realsense-d435i-camera-serial-numbers-from-frames-for-multiple
# access date: 31.01.2023