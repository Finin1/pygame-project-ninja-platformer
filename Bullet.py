import pygame as pg


class Bullet(pg.sprite.Sprite):  # класс, создающий пули

    def __init__(self, x, y, image, facing, *group):  # получает положение по оси х и у, радиус, цвет, и сторону полёта
        super().__init__(*group)
        self.start_image = image
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 50 * facing

    def render(self):  # тут объект рендерится
        self.rect.x += self.vel
        if self.image == self.start_image:
            self.image = pg.transform.rotate(self.image, 45)
        else:
            self.image = self.start_image

    def finish_work(self):  # удаление спрайта
        self.kill()
