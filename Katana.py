import pygame as pg
import math


class Katana:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite.mask = pg.mask.from_surface(sprite.image)
        self.center_pos = self.sprite.image.get_rect(center=(self.y, self.y))
        self.incline = -45
        self.for_rotate = False
        self.facing = 1
        self.sprite.image = pg.transform.rotate(self.sprite.image, int(self.incline))
        self.sprite.rect = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))

    def render(self, x, y, face):
        self.sprite.rect.x = x
        self.sprite.rect.y = y

        if self.for_rotate:
            self.sprite.image = pg.transform.flip(self.sprite.image, False, True)
            self.for_rotate = False

        self.sprite.rect = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))
        if face != self.facing:
            self.sprite.image = pg.transform.flip(self.sprite.image, True, False)
            self.facing *= -1

    def actived(self):
        self.for_rotate = True
