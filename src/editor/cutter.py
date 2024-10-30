from src.editor.actor import Resolve

# om man trenger ting, sjekk ut https://github.com/IgorRidanovic/smpte

editor = Resolve()

cuts = []

# Assumes we start at the livecut beginning
# Possibly jump by the largest -offset? to make it automatic

current_frame = 0
for frame, cameraId in enumerate(cuts):
    print(f"Cutting at frame {frame} to camera {cameraId}")
    editor.forward_frames(frame - current_frame)

    # TODO verify at man er på riktig frame?

    current_frame += frame
    editor.cut(cameraId)

print("Done!")