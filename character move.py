from pico2d import *


class Character():
    def __init__(self):
        self.x,self.y=200,120
        self.jumpnum=0
        self.dir=0
        self.flag=0
        self.image =load_image('character1.png')

    def clickflag(self,flag):
        self.flag=flag
    def xclick(self,dir):
        self.dir=dir

    def update(self):
        self.y+=(self.dir * 20)
        if self.y >= 200:
            self.dir = -1
            self.jumpnum=1
        elif self.y <=120 and self.jumpnum==1:
            self.jumpnum=0
            if self.flag==0:
                self.dir = 0
            elif self.flag==1:
                self.dir = 1
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
        if event.type == SDL_KEYDOWN and event.key == SDLK_x:
            character.xclick(1)
            character.clickflag(1)
            event.type = SDL_KEYUP
        elif event.type == SDL_KEYUP and event.key == SDLK_x:
            character.clickflag(0)

start = True

open_canvas()

character= Character()


while start:

    handle_events()

    character.update()

    clear_canvas()
    character.draw()
    update_canvas()

    delay(0.02)



close_canvas()

