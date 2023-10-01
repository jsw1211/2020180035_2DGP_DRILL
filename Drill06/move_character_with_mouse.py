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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            arrow_x, arrow_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            arrow.draw(arrow_x, arrow_y)
    pass

def character_move():
    global arrow_x, arrow_y
    global c_x, c_y
    global x, y
    global frame
    c_x, c_y = x, y
    for i in range(0, 100+1, 1):
        t = i / 100
        x = (1 - t) * c_x + t * arrow_x
        y = (1 - t) * c_x + t * arrow_y
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        arrow.draw(arrow_x, arrow_y)
        if (x < arrow_x):
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
        
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
arrow_x, arrow_y = x, y
frame = 0
hide_cursor()

while running:
    character_move()

    handle_events()

close_canvas()




