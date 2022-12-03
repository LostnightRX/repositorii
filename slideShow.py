import os
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import random

font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',  size = 50)
directory = 'C:/Users/Student/Desktop/SlideShow'
clips = []
col = list('0123456789ABCDEF')
for i in range(10):
    im = Image.new('RGB', (1000,1000), color = '#' + ''.join([random.choice(col) for _ in range(6)]))
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (500 - i * 10, 500 - i * 10),
    'HELLO',
    font = font,
    fill = ('#FFFFFF')
    )
    im.save(f'{directory}/new{i}.jpg')
images = list(filter(lambda x: x.endswith('.jpg'), os.listdir(directory)))
clips = [ImageClip(m).set_duration(1) for m in images]
final_clip = concatenate_videoclips(clips, method = 'compose')
final_clip.write_videofile('slides.mp4', fps = 30)

