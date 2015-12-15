__author__ = 'SooJeong'

import random

from pico2d import *


class Boy:
    image = None

    RUN, JUMP, SLIDE = 0, 1, 2


    def __init__(self):
        self.x, self.y = 100, 130
        self.state = self.run
        self.frame = random.randint(0, 7)
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state == self.RUN:
                self.state = self.JUMP

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def run(self):
        self.run_frames += 1

    def slide(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 50

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.JUMP:
            if self.y == 130:
                while self.y == 230:
                    self.y += 20
            if self.y == 230:
                while self.y == 130:
                    self.y -= 20


    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RUN, self.SLIDE):
                self.state = self.JUMP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RUN, self.JUMP):
                self.state = self.SLIDE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.JUMP, self.SLIDE):
                self.state = self.RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.JUMP, self.SLIDE):
                self.state = self.RUN



