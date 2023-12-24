import pygame as pg


class Bullet:  # класс, создающий пули
    def __init__(self, x, y, radius, color, facing):  # получает положение по оси х и у, радиус, цвет, и сторону полёта
        self.x = x
        self.y = y
        self.radius = radius
        self.width = radius * 2
        self.height = radius * 2
        self.color = color
        self.facing = facing
        self.vel = 50 * facing

    def render(self, sc):  # тут объект рендерится
        pg.draw.circle(sc, self.color, (self.x, self.y), self.radius)
