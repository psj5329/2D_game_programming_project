__author__ = 'SooJeong'


import random
from background import Grass
from background import Background
from pico2d import *

running = None
boy = None
grass = None
background = None
life = None


class Life:
    image = None

    def __init__(self):
        self.x, self.y = 80, 560
        if Life.image == None:
            Life.image = load_image('life_1.png')

    def draw(self):
        self.image.clip_draw(100, 100, 100, 100, self.x, self.y)

class Dead:
    image = None

    def __init__(self):
        self.x, self.y = 50, 75
        if Dead.image == None:
            Dead.image = load_image('life_2.png')

    def draw(self):
        self.image.draw(81, 561)




class Boy:
    image = None

    RUN, JUMP = 0, 1



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

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.JUMP:
            if self.y == 130:
                while self.y == 230:
                    self.y += 20
            if self.y == 230:
                while self.y == 130:
                    self.y -= 20





def handle_events():
    global running
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # else:
        #     boy.handle_event(event)




def main():

    open_canvas()

    global running

    boy = Boy()
    grass = Grass(800, 100)
    background = Background(800, 600)
    life = Life()
    dead = Dead()

    running = True
    while running:
        handle_events()

        boy.update()

        clear_canvas()
        background.draw()
        grass.draw()
        dead.draw()
        life.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()