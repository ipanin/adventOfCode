from tkinter import Tk, Label
from PIL import Image, ImageTk
import util

WIDTH, HEIGHT = 101, 103  # Image size

def move(robots, W: int, H: int):
    for i,r in enumerate(robots):
        pos = r[0] + r[1]
        r0 = complex(pos.real % W, pos.imag % H)
        robots[i] = (r0, r[1])

def draw(robots):
    # Create a blank image with a black background
    image = Image.new('L', (WIDTH, HEIGHT), 'black')

    # Create the pixel map
    pixels = image.load()

    for p in robots:
        pixels[(p[0].real, p[0].imag)] = 250

    img = image.resize((WIDTH*5, HEIGHT*5), resample = Image.Resampling.BOX)
    img.show()

######################################

robots = []
lines = util.load_int_lists('input.txt')
for x, y, vx, vy in lines:
    robots.append((x + y * 1j, vx + vy * 1j))

seconds = 0
has_upper = True
has_left = True
while seconds < 10000:
    if seconds % 1000 == 0:
        print(f'Seconds: {seconds}')

    seconds += 1
    move(robots, WIDTH, HEIGHT)

    has_upper = False
    for r in robots:
        if r[0].imag == 0:
            has_upper = True
            break
    has_left = False
    for r in robots:
        if r[0].real == 0:
            has_left = True
            break

    if not has_upper and not has_left:
        print(f'Found on time: {seconds}')
        draw(robots)

