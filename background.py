__author__ = 'SooJeong'

import random

from pico2d import *

global dir

class Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('background.png')
        self.speed = 0.1
        self.left = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self):
        self.left = (self.left + self.speed) % self.image.w



class Grass:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 10.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    global grass_num

    def __init__(self, w, h):
        self.grass_num = 0
        self.image = load_image('grass.png')
        self.speed = 1.5
        self.left = 0
        self.dir = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self):
        self.left = (self.left + self.speed) % self.image.w
        # if self.screen_width == 0:
        #     self.grass_num += 1
        # if self.grass_num % 10 == 0:
        #     self.speed += 0.001



class UpObject:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 10.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    # global grass_num
    # SCROLL_SPEED_PPS = 1

    def __init__(self):
        self.x, self.y = 800, 400
        self.image = load_image('up_object_1.png')
        self.speed = 1.5
        self.left = 0
        # self.screen_width = w
        # self.screen_height = h

    def draw(self):
        # x = int(self.left)
        # w = min(self.image.w - x, self.screen_width)
        # self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        # self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)
        self.image.clip_draw(0, 0, 150, 400, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 75, self.y - 250, self.x + 75, self.y + 200

    def update(self):
        self.x = (self.x - self.speed)
        if self.x < -150:
            self.x = 800