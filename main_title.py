import game_framework
import characterstage

from pico2d import *
name = "TestTitle"
image = None

def enter():
    global image
    open_canvas(800, 600)
    image = load_image('test title.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(characterstage)


def pause(): pass
def resume(): pass
