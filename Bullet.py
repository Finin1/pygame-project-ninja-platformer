import pygame as pg
# from weapon import Weapon


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = radius * 2
        self.height = radius * 2
        self.color = color
        self.facing = facing
        self.vel = 50 * facing

    def render(self, sc):
        pg.draw.circle(sc, self.color, (self.x, self.y), self.radius)
