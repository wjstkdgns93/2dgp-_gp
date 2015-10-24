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
        self.maxhight=90
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
    global obsnum,timer
    global character,mapping

    rect=None
    def __init__(self):
        self.y=-100
        self.x=-100
        self.imagestat=0
        if Obstacle.rect==None:
            self.image =load_image('rect obstacle.png')


    def placenum(self,placex,placey):
        self.x=placex
        self.y=80+(placey*40)

    def update(self):
        self.x-=5

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40,self.x,self.y)
        #임시 충돌체크(장애물제거)
        if character.x+20>=self.x-20 and character.x-20<=self.x+20:
            if character.y-20<self.y+20:
                 for i in range(15):
                    mapping.pop(i)


def stage1():
    global timer,mapping

    if timer%10==0:
        for i in range(15):
            mapping.append(Obstacle())
    #지나간 맵 제거
    if(len(mapping)>270):
        for i in range(15):
            mapping.pop(i)

    #시간별 장애물생성
    if timer==100:
        mapping[len(mapping)-14].placenum(800,1)
    if timer==200:
        mapping[len(mapping)-14].placenum(800,1)
    if timer==300:
        mapping[len(mapping)-14].placenum(800,1)
    if timer==400:
        mapping[len(mapping)-14].placenum(800,1)
    if timer==500:
        mapping[len(mapping)-14].placenum(800,1)
    if timer==650:
        mapping[len(mapping)-14].placenum(800,1)
        mapping[len(mapping)-13].placenum(800,2)
    if timer==800:
        mapping[len(mapping)-14].placenum(800,1)
        mapping[len(mapping)-13].placenum(800,2)


def handle_events():
    global start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type ==SDL_KEYDOWN and event.key==SDLK_ESCAPE :
            start=False
        if event.type == SDL_KEYDOWN and event.key == SDLK_x and character.y<=120:
            character.xclick(50)
            character.clickflag(1)
            event.type = SDL_KEYUP
        elif event.type == SDL_KEYUP and event.key == SDLK_x:
            character.clickflag(0)

character = None
mapping=[]
land=None
timer=0

def enter():
    global character,land,mapping
    character= Character()
    land=Land()

def exit():
    global character,land
    del(character)
    del(land)
    close_canvas()

def update():
    global timer
    character.update()
    stage1()
    for Obstacle in mapping:
        Obstacle.update()
    #점점 빨라짐
    if timer>=600:
        delay(0.005)
    elif timer>=300:
         delay(0.007)
    else:
        delay(0.01)
    timer+=1

def draw():
    clear_canvas()
    character.draw()
    land.draw()
    for Obstacle in mapping:
        Obstacle.draw()
    update_canvas()
