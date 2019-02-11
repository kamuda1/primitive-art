from PIL import Image, ImageDraw
import PIL
from IPython.display import display
import numpy as np
from PIL import ImageFilter
from numpy import cos, sin


def make_triangle(im, height_mag, width_mag, color=250):
    [x, y] = [np.random.uniform(im.size[0]),
              np.random.uniform(im.size[1])]
    height = np.random.uniform(-height_mag, height_mag)
    width = np.random.uniform(-width_mag, width_mag)

    draw = ImageDraw.Draw(im)
    draw.polygon(((x, y),
                  (x, y+height),
                  (x+width, y),
                  (x, y)),
                 fill=color)

    return


def make_squares(im, height_mag, width_mag, color=250):
    [x, y] = [np.random.uniform(im.size[0]),
              np.random.uniform(im.size[1])]
    height = np.random.uniform(-height_mag, height_mag)
    width = np.random.uniform(-width_mag, width_mag)

    draw = ImageDraw.Draw(im)
    draw.polygon(((x, y),
                  (x, y+height),
                  (x+width, y+height),
                  (x+width, y),
                  (x, y)),
                 fill=color)

    return
