import game_framework
import time
from pico2d import *


class Land:
    def __init__(self):
        self.image = load_image('test land.png')

    def draw(self):
        self.image.draw(400, 40)

class Character():
    global mapping
    image_state=[0,1,2]
    image=None
    def __init__(self):
        self.x=200
        self.y=120
        self.height=0
        self.base_y=120
        self.jump=0
        #점프키
        self.dir=0
        #점프키 고정확인
        self.flag=0
        if Character.image == None:
            Character.image_state=0
            self.image =load_image('character1.png')

    def clickflag(self,flag):
        self.flag=flag
    def xclick(self,dir):
        self.dir=dir
    def update(self):
        # if self.height < 90 and self.jump==0:
        #     self.y+=(self.dir)
        #     self.height+=self.dir
        #     if self.height>89:
        #         self.jump=1
        # elif self.height>0 and self.jump==1:
        #     self.jump=1
        #     self.dir=-3
        #     self.y+=(self.dir)
        #     self.height+=self.dir
        # elif self.y<=self.base_y:
        #     self.jump=0
        #     self.height=0
        #     self.y=self.base_y
        #     if self.flag==0:
        #         self.dir = 0
        #     elif self.flag==1:
        #         self.dir = 3
        self.y+=(self.dir)
        if self.y >= 210:
            self.dir =-3
            self.jump=1
        elif self.y <=120 and self.jump==1:
            self.jump=0
            self.y=120
            if self.flag==0:
                self.dir = 0
            elif self.flag==1:
                self.dir = 3
        if character.image_state==1:
            self.image =load_image('character2.png')
    def draw(self):
         self.image.clip_draw(0, 0, 40, 40,self.x,self.y)

class Obstacle():
    global character
    rect = None
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
        if character.x+20>self.x-20 and character.x-20>=self.x-40 and character.x-20<self.x+20 and character.x+20<=self.x+40:
            if character.y-20<self.y+20:
                character.image_state=1


def stage1():
    global timer,chtime,num,mapping

    mapping=[Obstacle() for i in range(26)]

    #장애물생성
    mapping[0].placenum(800,1)
    mapping[1].placenum(1200,1)
    mapping[2].placenum(1600,1)
    mapping[3].placenum(1600,2)
    mapping[4].placenum(2400,1)
    mapping[5].placenum(2400,2)
    mapping[6].placenum(3000,1)
    mapping[7].placenum(3040,1)
    mapping[8].placenum(3600,1)
    mapping[9].placenum(4000,1)
    mapping[10].placenum(4000,2)
    mapping[11].placenum(4600,1)
    mapping[12].placenum(4640,1)
    mapping[13].placenum(5000,1)
    mapping[14].placenum(5000,2)
    mapping[16].placenum(5400,1)
    mapping[17].placenum(5440,1)
    mapping[18].placenum(5740,1)
    mapping[19].placenum(5780,1)
    mapping[20].placenum(6000,1)
    mapping[21].placenum(6000,2)
    mapping[22].placenum(6400,1)
    mapping[23].placenum(6800,1)
    mapping[24].placenum(7200,1)
    mapping[25].placenum(7200,2)


def handle_events():
    global start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type ==SDL_KEYDOWN and event.key==SDLK_ESCAPE :
            start=False
        if event.type == SDL_KEYDOWN and event.key == SDLK_x and character.y<=120:
            character.xclick(3)
            character.clickflag(1)
            event.type = SDL_KEYUP
        elif event.type == SDL_KEYUP and event.key == SDLK_x:
            character.clickflag(0)

character = None
mapping=[]
land=None
timer=0

def enter():
    global character,land,mapping,start_time
    stage1()
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
    for Obstacle in mapping:
        Obstacle.update()
    #점점 빨라짐
    if timer>=1000:
        delay(0.003)
    elif timer>=500:
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
