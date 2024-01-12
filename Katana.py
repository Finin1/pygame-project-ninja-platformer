import pygame as pg
from os import path


class Katana:  # класс катаны
    def __init__(self, sprite):  # тут класс получает нужный спрайт
        self.sprite = sprite
        self.sprite.mask = pg.mask.from_surface(sprite.image)
        self.center_pos = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))
        self.facing = 1
        self.original_image = sprite.image
        self.def_img = pg.transform.rotate(pg.transform.flip(self.sprite.image, True, True), -90)

        self.attack_img = pg.transform.scale(pg.image.load(path.join('data\images\katana_attack.png')), (155, 30))

        self.sprite.rect = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))
        self.attack = False
        self.attackCount = 20
        self.can_defend = True

    def render(self, x, y, face):  # тут происходит рендер катаны
        self.sprite.rect.x = x
        self.sprite.rect.y = y

        if face != self.facing:
            self.sprite.image = pg.transform.flip(self.sprite.image, True, False)
            self.facing *= -1

        self.defend()

        if self.attack:
            if self.sprite.image != self.attack_img:
                self.sprite.image = self.attack_img
            self.actived()

        self.sprite.rect = self.sprite.image.get_rect(center=(self.sprite.rect.x, self.sprite.rect.y))

        if self.facing == -1:
            self.sprite.image = pg.transform.flip(self.sprite.image, True, False)

    def actived(self):  # этот метод отвечает за удар меча
        if self.attackCount >= -20:
            neg = 1
            if self.attackCount < 0:
                neg = -1
            self.sprite.rect.x -= self.attackCount * 5 * neg * self.facing - 50 * self.facing
            self.attackCount -= 1
        else:
            self.attackCount = 20
            self.sprite.image = self.original_image
            self.attack = False

    def defend(self):
        if not self.attack and self.can_defend:
            self.sprite.image = self.def_img

        if not self.can_defend:
            self.can_defend = True
            self.sprite.image = self.original_image
