import game_framework
from pico2d import *


class Land:
    def __init__(self):
        self.image = load_image('test land.png')

    def draw(self):
        self.image.draw(400, 40)

class Character():
    def __init__(self):
        self.x,self.y=200,120
        # self.jumpHeight= 20
        self.jumpnum=0
        self.dir=0
        self.flag=0
        self.image =load_image('character1.png')

    def clickflag(self,flag):
        self.flag=flag
    def xclick(self,dir):
        self.dir=dir

    def update(self):
        if self.dir!=0:
             self.dir-=1
        self.y+=(self.dir*0.1)
        if self.y >= 210:
            self.dir =-1
            self.dir-=1
            self.jumpnum=1
        elif self.y <=120 and self.jumpnum==1:
            self.jumpnum=0
            self.y=120
            if self.flag==0:
                self.dir = 0
            elif self.flag==1:
                self.dir = 50
    def draw(self):
        self.image.clip_draw(0, 0, 40, 40,self.x,self.y)

class Obstacle():

    def __init__(self):
        self.y=0
        self.x=0
        self.imagestat=0
        self.image =load_image('rect obstacle.png')
    def placenum(self,placex,placey):
        self.x=placex
        self.y=placey

    def update(self):
        self.x-=5;

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40,self.x,self.y)


def handle_events():

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            start=False
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_x and character.y<=120:
            character.xclick(50)
            character.clickflag(1)
            event.type = SDL_KEYUP
        elif event.type == SDL_KEYUP and event.key == SDLK_x:
            character.clickflag(0)

def stage1():
    global timer
    i=0
    if timer%8==0:
        mapping[i].placenum(800,120)


start = True
character = None
mapping=None
land=None
timer=0

def enter():
    global character,mapping,land
    open_canvas()
    character= Character()
    mapping= [Obstacle() for i in range(15)]
    stage1()
    land=Land()

def exit():
    global character,land
    del(character)
    del(land)
    close_canvas()

def update():
    global timer
    character.update()
    for Obstacle in mapping:
        Obstacle.update()
    delay(0.01)
    timer+=1

def draw():
    clear_canvas()
    character.draw()
    land.draw()
    for Obstacle in mapping:
        Obstacle.draw()
    update_canvas()