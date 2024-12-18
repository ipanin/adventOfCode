# Animate robots in Tkinter

from tkinter import Tk, Label
from PIL import Image, ImageTk
import util


WIDTH, HEIGHT = 101, 103  # Image size
seconds = 0
robots = []

# Function to update and display the next frame
def update_frame():
    global seconds
    global robots

    seconds += 1
    move(robots, WIDTH, HEIGHT)

#    if seconds % 49 == 0:
    text_label.config(text=f"Seconds={seconds}")
    image = generate_frame(robots)

    # Convert the image to ImageTk format for Tkinter
    image_tk = ImageTk.PhotoImage(image)

    # Update the label with the new frame
    img_label.config(image=image_tk)
    img_label.image = image_tk  # Keep a reference to avoid garbage collection

    # Schedule the next frame update
    root.after(100, update_frame)

# Function to generate a new image (frame) dynamically
def generate_frame(points):
    # Create a blank image with a black background
    image = Image.new('L', (WIDTH, HEIGHT), 'black')

    # Create the pixel map
    pixels = image.load()

    for p in points:
        pixels[(p[0].real, p[0].imag)] = 250

    return image.resize((WIDTH*5, HEIGHT*5), resample = Image.Resampling.BOX)

def move(robots, width: int, height: int):
    for i,r in enumerate(robots):
        pos = r[0] + r[1]
        r0 = complex(pos.real % width, pos.imag % height)
        robots[i] = (r0, r[1])

# Initialize the Tkinter window
root = Tk()
root.title("Robots")

text_label = Label(root, text="Seconds=")
text_label.pack(pady=10)

# Create a Label widget to display the images
img_label = Label(root, font=("Arial", 24))
img_label.pack(pady=10)

lines = util.load_int_lists('input.txt')
for x, y, vx, vy in lines:
    robots.append((x + y * 1j, vx + vy * 1j))

# Start the animation
update_frame()

# Start the Tkinter event loop
root.mainloop()
