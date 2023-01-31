import pyrealsense2 as rs
import numpy as np

def initialize_camera():
    # start the frames pipe
    p = rs.pipeline()
    conf = rs.config()
    conf.enable_stream(rs.stream.accel)
    conf.enable_stream(rs.stream.gyro)
    prof = p.start(conf)
    return p

def gyro_data(gyro):
    return np.asarray([gyro.x, gyro.y, gyro.z])

def accel_data(accel):
    return np.asarray([accel.x, accel.y, accel.z])

p = initialize_camera()
try:
    while True:
        f = p.wait_for_frames()
        # in the referred discussion, f[0] is for accel data, f[1] is for gyro data
        # however, I experienced reverse, check both and test
        accel = accel_data(f[0].as_motion_frame().get_motion_data())
        gyro = gyro_data(f[1].as_motion_frame().get_motion_data())
        print("accelerometer: ", accel)
        print("gyro: ", gyro)

finally:
    p.stop()

# Reference: https://github.com/IntelRealSense/librealsense/issues/3409
# access date: 31.01.2023