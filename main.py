__author__ = 'SooJeong'


import random
from pico2d import *

running = None

class Grass:
    global grass_num

    def __init__(self):
        self.x = 400
        self.s = 1
        self.map = 0
        self.image = load_image('grass.png')

    def draw(self):
        self.image.clip_draw(0, 0, 800, 100, self.x, 50)

        if self.x == 0:
            self.x = 800
            self.map += 1
            if self.map % 2 == 0:
                self.s += 1
            self.x -= 10 * self.s
        elif self.x > 0:
            self.x -= 10 * self.s


class Life:
    def __init__(self):
        pass



class Boy:
    image = None

    run, slide = 0, 1

    def run(self):
        self.run_frames += 1

    def slide(self):
        pass


    def __init__(self):
        self.x, self.y = 100, 130
        self.state = self.run
        self.frame = random.randint(0, 7)
        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            pass# if self.

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8





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
    boy = Boy()
    grass = Grass()

    global running
    running = True
    while running:
        handle_events()

        boy.update()

        clear_canvas()
        grass.draw()
        boy.draw()
        update_canvas()

        delay(0.05)

    close_canvas()


if __name__ == '__main__':
    main()