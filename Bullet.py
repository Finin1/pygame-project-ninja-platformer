import pygame as pg
# from weapon import Weapon


class Bullet(pg.sprite.Sprite):  # класс, создающий пули

    def __init__(self, x, y, image, image2, facing, *group):  # получает положение по оси х и у, радиус, цвет, и сторону полёта
        super().__init__(*group)
        self.start_image = image
        self.second_image = pg.transform.scale(image2, (50, 45))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 50 * facing
        self.facing = facing

    def render(self):  # тут объект рендерится
        self.rect.x += self.vel
        if self.image == self.start_image:
            self.image = self.second_image
        else:
            self.image = self.start_image

        if self.facing == -1:
            self.image = pg.transform.flip(self.image, True, True)

    def finish_work(self):  # удаление спрайта
        self.kill()
