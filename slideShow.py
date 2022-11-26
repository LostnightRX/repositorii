from moviepy.editor import *

import os

directory = 'C:/Users/student/Desktop/Степанов/slideShow'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'),files))
clips = [ImageClip(m).set_duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method = 'compose')
final_clip.write_videofile('slides.mp4', fps = 24)
