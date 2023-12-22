import pygame as pg


class Katana:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprire = sprite
        self.incline = 45

    def render(self, x, y):
        self.sprire.rect.x = x
        self.sprire.rect.y = y
        pg.transform.rotate(self.sprire.image, self.incline)

    def actived(self):
        self.incline = 135
        pg.time.wait(100)
        self.incline = 45
