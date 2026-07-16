from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0')
# print(lidar.get_info())
# print(lidar.get_health())
# lidar.stop()
# lidar.disconnect()
print("Starting scan... (Ctrl+C to stop)")
try:
    for i, scan in enumerate(lidar.iter_scans()):
        print(f"Scan {i}: {len(scan)} points")
        if i > 5:
            break
finally:
    lidar.stop()
    lidar.disconnect()
# Random comment for push test!