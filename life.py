__author__ = 'SooJeong'

import random

from pico2d import *


class Life:

    def __init__(self):
        self.x, self.y = 99, 559
        self.image = load_image('life_1.png')

    def draw(self):
        self.image.clip_draw(0, 0, 150, 75, self.x, self.y)

    def update(self):
        pass



class Dead:
    image = None

    def __init__(self):
        self.x, self.y = 150, 75
        if Dead.image == None:
            Dead.image = load_image('life_2.png')

    def draw(self):
        self.image.draw(100, 560)

    def update(self):
        pass