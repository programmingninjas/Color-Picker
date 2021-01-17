from colorthief import ColorThief
from turtle import *
import numpy as np
import matplotlib.pyplot as plt

color_thief = ColorThief('image path') #Enter image path

# get the dominant color

dominant_color = color_thief.get_color(quality=1)

screen = Screen()

colormode(255)

screen.bgcolor(dominant_color)

# build a color palette

colors = color_thief.get_palette(color_count=6)

palette = np.array(colors)[np.newaxis, :, :]

plt.imshow(palette)
plt.axis('off')
plt.show()


