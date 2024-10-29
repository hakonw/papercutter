import imageio.v3 as iio
import numpy as np

# Define the data
data = {
    'liveprogram': {
        'path': 'cam_live_cut.mp4'
    },
    'individuals': [
        {
            'camId': 1,
            'path': 'cam1.mp4',
            'live_frame_to_search': 14311
        },
        {
            'camId': 2,
            'path': 'cam2.mp4',
            'live_frame_to_search': 12311
        },
        # Add more cameras as needed
    ]
}

# Load the target frames from the live program
live_frames = {}
for cam in data['individuals']:
    cam_id = cam['camId']
    frame_idx = cam['live_frame_to_search']
    live_frame = iio.imread(
        data['liveprogram']['path'],
        index=frame_idx,
        plugin='pyav'
    )
    live_frames[cam_id] = live_frame

# Iterate over individual camera videos
for cam in data['individuals']:
    cam_id = cam['camId']
    cam_path = cam['path']
    target_frame = live_frames[cam_id]
    frame_number = 0
    found = False

    # Open the camera video using iio.imiter
    cam_frames = iio.imiter(cam_path, plugin='pyav')

    # Iterate over frames in the camera video
    for frame in cam_frames:
        difference = np.mean(np.abs(frame.astype('float32') - target_frame.astype('float32')))
        threshold = 1000  # Adjust as needed
        if difference < threshold:
            offset = frame_number - cam['live_frame_to_search']
            print(f'Camera {cam_id}: Offset is {offset} frames')
            found = True
            break
        frame_number += 1

    if not found:
        print(f'Match not found for camera {cam_id}')