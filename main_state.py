__author__ = 'SooJeong'

from pico2d import *
import game_framework

from background import Grass
from background import Background
from boy import Boy
from life import Life
from life import Dead
from background import UpObject

name = "main_state"

running = None
boy = None
grass = None
background = None
life = None
dead = None
upobject = None


def create_world():
    global boy, grass, background, life, dead, upobject

    boy = Boy()
    grass = Grass(800, 100)
    background = Background(800, 600)
    life = Life()
    dead = Dead()
    upobject = UpObject()


def destroy_world():
    global boy, grass, background, life, dead, upobject

    del(boy)
    del(grass)
    del(background)
    del(life)
    del(dead)
    del(upobject)



def enter():
    open_canvas()
    hide_cursor()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update():
    boy.update()
    grass.update()
    background.update()
    upobject.update()
    life.update()
    dead.update()

    if collide(boy, upobject):
        print("collision")

def draw():
    clear_canvas()
    background.draw()
    upobject.draw()
    dead.draw()
    life.draw()
    grass.draw()
    boy.draw()
    boy.draw_bb()
    upobject.draw_bb()

    update_canvas()

