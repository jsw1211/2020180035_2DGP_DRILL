from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    global arrow_x, arrow_y
    global arrow_cx, arrow_cy
    global t
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            arrow_x, arrow_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            t = 0
            i = 0
            arrow_cx, arrow_cy = arrow_x, arrow_y
    pass

def character_move():
    global i
    if (i == 100):
        return
    global arrow_x, arrow_y
    global c_x, c_y
    global x, y
    global frame
    global arrow_cx, arrow_cy
    global t
    if (i == 0):
        c_x, c_y = x, y
    t = i / 100
    x = (1 - t) * c_x + t * arrow_cx
    y = (1 - t) * c_y + t * arrow_cy
    i += 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_x, arrow_y = x, y
arrow_cx, arrow_cy = arrow_x, arrow_y
frame = 0
t = 0
i = 100
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character_move()
    if (i != 100):
        arrow.draw(arrow_cx, arrow_cy)
    arrow.draw(arrow_x, arrow_y)
    if (x < arrow_cx):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    frame = (frame + 1) % 8
    delay(0.01)
    update_canvas()

    handle_events()

close_canvas()



