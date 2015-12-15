__author__ = 'SooJeong'

from pico2d import *

import game_framework


from main_state import Boy
from background import Background
from background import Grass
from life import Life


name = "scroll_state"

boy = None
background = None
grass = None
life = None

def create_world():
    global boy, background, grass, life
    boy = Boy()
    background = Background(800, 600)
    grass = Grass(800, 100)
    life = Life()


def destroy_world():
    global boy, background, grass, life
    del(boy)
    del(background)
    del(grass)
    del(life)

def enter():
    open_canvas(800, 600)
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass

def resume():
    pass


def handle_events(frame_time): #frame_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def update():
    boy.update()
    background.update()
    grass.update()
    life.update()



def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    boy.draw()
    life.draw()
    update_canvas()
