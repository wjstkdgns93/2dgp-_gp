from pico2d import *


class Character:
    def __init__(self):
        self.x,self.y=200,120
        self.image =load_image('character1.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0, 0, 40, 40,self.x,self.y)

def handle_events():

    global start

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            start = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            start = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            pass

start = True
jump=0
jumpcount=0
count=0

open_canvas()

character= Character()


while(start):

    handle_events()

    character.update()

    clear_canvas()
    character.draw()
    update_canvas()

    delay(0.2)



close_canvas()

