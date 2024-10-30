from src.video.video import Video
from src.video.program import Program

if __name__ == '__main__':
    cam1 = Video(1, 'cam1.mp4', -200)
    cam2 = Video(2, 'cam2.mp4', 1343)

    prog = Program('prog.mp4', [cam1, cam2])

    while not prog.done():
        prog.print_if_new_cut()
        prog.all_next()

