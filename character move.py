from pico2d import *
open_canvas()

character = load_image('movecharcter1.png')

x = 800
frame =0;

while(x>0):
    clear_canvas()
    character.clip_draw(frame*72, 0, 72, 58,x,100)
    update_canvas()
    frame=(frame+1)%3
    x-=10
    delay(0.1)
    get_events()



close_canvas()

