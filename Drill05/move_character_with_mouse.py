from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
arrow_x = 0
arrow_y = 0
hide_cursor()

def random_arrow():
    global arrow_x
    global arrow_y
    arrow_x = random.randint(0, TUK_WIDTH)
    arrow_y = random.randint(0, TUK_HEIGHT)
    arrow.draw(arrow_x, arrow_y)

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    random_arrow()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




