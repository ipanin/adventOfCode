# Graphics utils for AoC
from PIL import Image


def draw_image(image: dict, w: int, h: int):
    img = Image.new('RGB', (w, h), "blue")  # Create a new image with blue background
    pixels = img.load()  # Create the pixel map

    for k, v in image.items():
        if v == 0:
            color = (0, 0, 0)
        elif v == 1:
            color = (255, 255, 255)  # white
        elif v == 2:
            color = (255, 0, 0)  # red
        elif v == 3:
            color = (0, 255, 0)  # green
        elif v == 4:
            color = (255, 255, 0)  # yellow
        else:
            color = (128, 128, 128)  # gray

        pixels[k] = color
        
    img.resize((w*20, h*20), resample=Image.Resampling.BOX).show()


def draw_image_bw(coords: list, w: int, h: int):
    img = Image.new('L', (w, h), "black")
    pixels = img.load()  # Create the pixel map

    for c in coords:
        pixels[c] = 250

    img_r = img.resize((w*5, h*5), resample=Image.Resampling.BOX)
    img_r.show()
