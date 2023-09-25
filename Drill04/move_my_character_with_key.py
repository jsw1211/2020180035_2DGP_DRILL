from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events():
    global running, dir_x, dir_y
    global x, y
    global motion

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                motion = 0               
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                motion = 1
            elif event.key == SDLK_UP:
                dir_y += 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1
            elif event.key == SDLK_z:
                motion = 4
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                motion = 0
            elif event.key == SDLK_LEFT:
                dir_x += 1
                motion = 1
            elif event.key == SDLK_UP:
                dir_y -= 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1
            elif event.key == SDLK_z:
                motion = 4

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
dir_x = 0
dir_y = 0
motion = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if motion == 0:
        character.clip_draw(frame * 118, 390, 110, 160, x, y, 200, 200)
    elif motion == 1:
        character.clip_composite_draw(frame * 118, 390, 110, 160, 0, 'h',x, y, 200, 200)
    elif motion == 2:
        character.clip_draw(frame * 118, 390, 110, 160, x, y, 200, 200)
    elif motion == 3:
        character.clip_draw(frame * 118, 390, 110, 160, x, y, 200, 200)
    elif motion == 4:
        character.clip_draw(580, 50, 250, 100, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    if motion != 4:
        x += dir_x * 5
        y += dir_y * 5
    delay(0.05)

close_canvas()

