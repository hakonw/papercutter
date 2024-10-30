from src.video.video import Video


class Program(Video):
    def __init__(self, path, children: list[Video]):
        super().__init__(0, path, 0)
        self.children = children
        for video in self.children:
            video.catch_up()
        self.current_camera = None

    def active_videos(self):
        return [video for video in self.children if not video.finished]

    def all_next(self):
        self.next()
        for video in self.active_videos():
            if self.frame_index > video.offset:
                video.next()
                assert video.frame_index + video.offset == self.frame_index

    def best_cut(self):
        best_score = float('inf')
        best_cam_id = None
        for video in self.active_videos():
            score = self.diff(video.frame)
            if score < best_score:
                best_score = score
                best_cam_id = video.camId
        if best_score > 1000:
            print(f"Warning: Could not find any good match for frame {self.frame_index}")

        return best_cam_id

    def print_if_new_cut(self):
        best_cam_id = self.best_cut()
        if best_cam_id != self.current_camera:
            self.current_camera = best_cam_id
            print(f"Cutting at frame {self.frame_index} to camera {self.current_camera}")


    def done(self) -> bool:
        if self.finished:
            return True
        if len(self.active_videos()) == 0:
            return True
        return False
