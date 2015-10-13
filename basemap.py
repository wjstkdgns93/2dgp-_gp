from pico2d import *

# class Background():
#     def __init__(self):
#         self.image = load_image('brack board.png')
#     def draw(self):
#         self.image.draw(400, 300)

class Map():
    image = None

    def __init__(self,place,place2):
        self.y=80+(place2*40)
        self.x=20*(place*2+1)
        self.imagestat=0
        if Map.image == None:
            Map.image =load_image('rect obstacle.png')

    def update(self):
        self.x-=4

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

def stage1():  #시간별 장애물생성
    global timer
    if timer == 30:
        mapping.append(Map(19,1))


start = True

open_canvas()
mapping= [Map(i,0) for i in range(19)]

timer=0
mapstate=0
# background= Background()


while start:

    handle_events()

    if timer % 10 == 0:
        del(mapping[0])
        mapping.append(Map(19,0))
        mapstate+=1

    stage1()


    timer+=1

    for map in mapping:
        map.update()

    clear_canvas()
    # background.draw()
    for map in mapping:
        map.draw()
    update_canvas()

    delay(0.05)


close_canvas()
