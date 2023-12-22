import pygame as pg
import math


class Katana:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite.mask = pg.mask.from_surface(sprite.image)
        self.center_pos = self.sprite.image.get_rect(center=(self.y, self.y))
        self.incline = 105

    def render(self, x, y):
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        pg.transform.rotate(self.sprite.image, int(self.incline))
        self.sprite.rect = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))

    def actived(self):
        self.incline = 135
        pg.time.wait(100)
        self.incline = 45
