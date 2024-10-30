import numpy as np
from imageio import v3 as iio


class Video:
    def __init__(self, camId, path, offset):
        self.camId = camId
        self.path = path
        self.offset = offset
        self.frame_index = 0
        self.reader = iio.imiter(self.path, plugin='pyav')
        self.frame = next(self.reader)
        self.finished = False

    # Possible name: sync
    def catch_up(self):
        while self.frame_index < self.offset:
            self.next()

    def next(self) -> np.ndarray:
        if self.finished:
            raise Exception("is at the end of the video")
        self.frame_index += 1
        self.frame = next(self.reader, None)
        if self.frame is None:
            self.finished = True
        return self.frame

    def diff(self, frame):
        score = np.mean(np.abs(self.frame.astype('float32') - frame.astype('float32')))
        return score
