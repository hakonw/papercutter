import imageio.v3 as iio

from src.video.video import Video


def get_frame(path, index):
    return iio.imread(
        path,
        index=index,
        plugin='pyav'
    )

def find_offset(camera: Video, target_frame, threshold=1000):
    best_score = float('inf')
    best_index = None
    def has_match():
        return best_score < threshold
    frames_to_count_after_match = 200

    while not camera.finished() and frames_to_count_after_match > 0:
        camera.next()
        diff = camera.diff(target_frame)
        if diff < best_score:
            best_score = diff
            best_index = camera.frame_index
        if has_match:
            frames_to_count_after_match -= 1

    if best_index is None:
        print(f"No match found for camera {camera.camId}")
        return None
    print(f"Match found for camera {camera.camId}, path: {camera.path} at index {best_index}")

if __name__ == '__main__':
    camera = Video(1, 'cam1.mp4', 0)

    prog_path = "cam3.mp4"
    frame_cam1 = get_frame(prog_path, 400)

    find_offset(camera, frame_cam1)
