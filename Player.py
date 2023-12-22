import pygame as pg
from Bullet import Bullet
from os import path
from sys import exit
from Katana import Katana
# import Entity


class Player:  # класс Игрока
    def __init__(self, screen, win, x=500, y=500):  # инициализация класса
        self.pos_x = x
        self.pos_y = y
        self.width = 50
        self.height = 100
        self.screen = screen
        self.win_size = win
        self.body = None
        self.isJump = False
        self.jumpCount = 20
        self.bullets = []
        self.facing = 1
        self.speed = 1

    def render(self):  # отрисовка персонажа и пуль
        pg.draw.rect(self.screen, pg.Color('white'), (self.pos_x, self.pos_y, self.width, self.height))

        for bullet in self.bullets:
            if 0 < bullet.x < self.win_size[0]:
                bullet.x += bullet.vel
                bullet.render(self.screen)
            else:
                self.bullets.pop(self.bullets.index(bullet))

    def move(self, x=10):  # движение персонажа
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.pos_x -= x * self.speed
            self.facing = -1
        elif keys[pg.K_d]:
            self.pos_x += x * self.speed
            self.facing = 1

        katana.render(self.pos_x + 30 + (self.width // 2 * self.facing), self.pos_y + (self.height // 2))

    def jump(self):  # прыжок персонажа
        if self.isJump:
            if self.jumpCount >= -20:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.pos_y -= self.jumpCount ** 2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 20

    def shot(self):  # выстрел персонажа
        self.bullets.append(Bullet(self.pos_x, self.pos_y + (self.height // 2), 10, (255, 0, 0), self.facing))

    def lunge(self, x=300):  # одна из механик игры, выпад
        self.pos_x += x * self.facing

    def attack(self):
        pass


def load_image(name):
    fullname = path.join('data\images', name)
    # если файл не существует, то выходим
    if not path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit()
    img = pg.image.load(fullname)
    return img


if __name__ == '__main__':  # демонстрация работы класса
    pg.init()
    win_size = (1000, 900)
    sc = pg.display.set_mode(win_size)
    run = True
    player = Player(sc, win_size)
    clock = pg.time.Clock()

    all_sprites = pg.sprite.Group()
    sprite = pg.sprite.Sprite()
    sprite.image = pg.transform.scale(load_image("katana.png"), (100, 121))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    katana = Katana(player.pos_x, player.pos_y, sprite)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.isJump = True
                elif event.key == pg.K_f:
                    player.shot()
                elif event.key == pg.K_LSHIFT:
                    player.lunge()

        sc.fill((0, 0, 0))
        player.jump()
        player.move()
        player.render()
        all_sprites.draw(sc)
        pg.display.flip()
        clock.tick(30)
