from pico2d import *

class Background():
    def __init__(self):
        self.image = load_image('brack board.png')
    def draw(self):
        self.image.draw(400, 300)

class Map():
    def __init__(self):
        self.y=80
        self.x=20
        self.imagestat=0
        self.image =load_image('rect obstacle.png')
    def placenum(self,place):
        self.x=self.x*(place*2+1)

    def update(self):
        self.x-=1;

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


start = True

open_canvas()

background= Background()
mapping= [Map() for i in range(20)]

for i in range(20):
    mapping[i].placenum(i)

while start:

    handle_events()
    for map in mapping:
        map.update()

    clear_canvas()
    background.draw()
    for map in mapping:
        map.draw()
    update_canvas()

    delay(0.1)



close_canvas()
