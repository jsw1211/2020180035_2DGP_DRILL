from pico2d import load_image


class Grass:
    def __init__(self, y1 = 30):
        self.image = load_image('grass.png')
        self.y =y1

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
