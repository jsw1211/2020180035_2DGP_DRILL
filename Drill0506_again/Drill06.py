from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    global arrow
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    arrow = load_image('hand_arrow.png')


def handle_events():
  
    global running
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def reset_world():
    global running, cx, cy, frame
    global t
    global action
    global mx, my
    global points

    mx, my = 0, 0
    running = True
    x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3

    points = [(100, 900), (1200, 800), (500, 100)]
    #set_new_target_arrow()


def set_new_target_arrow():
    global sx, sy, hx, hy, t
    global action
    global frame
    sx, sy = cx, cy
    #hx, hy = 50, 50
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT) # 끝점
    t = 0.0
    action = 1 if sx < hx else 0
    frame = 0

def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for p in points:
        arrow.draw(p[0], p[1])
    arrow.draw(mx, my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()
    
    
def update_world():
    global frame
    global cx, cy
    global t

    frame = (frame + 1) % 8

    #if t <= 1.0:
    #    cx = (1-t)*sx + t*hx # cx는 시작 x와 끝x를 1-t:t의 비율로 섞은 위치
    #    cy = (1-t)*sy + t*hy
    #    t += 0.001
    #else:
    #    cx, cy = hx, hy # 캐릭터 위치를 목적지 위치와 강제로 정확히 일치 시킨다.
    #    set_new_target_arrow()

    
open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()


while running:
    render_world()  # 월드의 현재 내용을 그린다.
    update_world()  # 사용자 입력을 받아들인다.
    handle_events()  # 월드 안의 객체들의 상호작용을 계산하고 그 결과를 update한다.


close_canvas()