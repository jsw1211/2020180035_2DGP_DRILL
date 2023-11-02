# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework
import random

# state event check
# ( state event type, event value )

# time_out = lambda e : e[0] == 'TIME_OUT'




# Boy Run Speed
# fill here
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

bird_image_x = 918 / 5
bird_image_y = 506 / 3

class Run:

    @staticmethod
    def enter(bird, e):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if bird.dir == 1 and bird.x > 1600 - 50:
            bird.dir = -1
        elif bird.dir == -1 and bird.x < 50:
            bird.dir = 1


    @staticmethod
    def draw(bird):
        if bird.frame//5 == 0:
            bird_image_h = 2
        elif bird.frame//5 == 1:
            bird_image_h = 1
        elif bird.frame//5 == 2:
            bird_image_h = 0
        if bird.dir == 1:
            bird.image.clip_composite_draw(int(bird_image_x * (int(bird.frame) % 5)), int(bird_image_y * bird_image_h), int(bird_image_x), int(bird_image_y), 0, '', bird.x, bird.y, 100, 100)
        elif bird.dir == -1:
            bird.image.clip_composite_draw(int(bird_image_x * (int(bird.frame) % 5)), int(bird_image_y * bird_image_h), int(bird_image_x), int(bird_image_y), 0, 'h', bird.x, bird.y, 100, 100)


class StateMachine:
    def __init__(self, bird):
        self.bird = bird
        self.cur_state = Run


    def start(self):
        self.cur_state.enter(self.bird, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.bird)

    def draw(self):
        self.cur_state.draw(self.bird)


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 400
        self.frame = random.randint(0,5)
        self.action = 3
        self.face_dir = 1
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()


    def draw(self):
        self.state_machine.draw()
