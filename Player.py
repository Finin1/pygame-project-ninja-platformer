import pygame as pg
from Bullet import Bullet
from os import path
from sys import exit

from Entity import Entity
from Katana import Katana
from interface import Interface


class Player(Entity):  # Класс Игрока
    def __init__(self, screen, win, health, speed: list, mass, pos=[500, 500], size=[50, 100]):  # инициализация класса
        super().__init__(health, pos, size, speed, mass)
        self.screen = screen
        self.win_size = win
        self.body = None
        self.isJump = False
        self.jumpCount = 20
        self.bullets = []
        self.facing = 1

    def render(self, objects):  # Отрисовка персонажа и пуль
        super().render(self, objects)

        for bullet in self.bullets:
            if 0 < bullet.rect.x < self.win_size[0]:
                bullet.render()
            else:
                self.bullets.pop(self.bullets.index(bullet))
                bullet.finish_work()

    def move(self, x=10):  # Движение персонажа
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.is_collided['right'] = False
            self.is_collided['left'] = False
            self.speed_x = 1
            self.pos_x -= x * self.speed_x
            self.facing = -1
        elif keys[pg.K_d]:
            self.is_collided['right'] = False
            self.is_collided['left'] = False
            self.speed_x = 1
            self.pos_x += x * self.speed_x
            self.facing = 1

        katana.render(self.pos_x + 30 + (self.width // 2 * self.facing), self.pos_y + (self.height // 2) + self.speed_y,
                      self.facing)

    # def jump(self):  # прыжок персонажа
    #     if self.isJump:
    #         if self.jumpCount >= -20:
    #             neg = 1
    #             if self.jumpCount < 0:
    #                 neg = -1
    #             self.pos_y -= self.jumpCount ** 2 * 0.1 * neg
    #             self.jumpCount -= 1
    #         else:
    #             self.isJump = False
    #             self.jumpCount = 20

    def shot(self):  # выстрел персонажа
        self.bullets.append(
            Bullet(self.pos_x, self.pos_y + (self.height // 2) // 2, shuriken, self.facing,
                   all_sprites))

    def lunge(self, x=300):  # Одна из механик игры, выпад
        self.pos_x += x * self.facing

    def attack(self):
        katana.actived()


def load_image(name):
    fullname = path.join('data\images', name)
    # Если файл не существует, то выходим
    if not path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit()
    img = pg.image.load(fullname)
    return img


if __name__ == '__main__':  # Демонстрация работы класса
    pg.init()
    win_size = (1000, 900)
    sc = pg.display.set_mode(win_size)
    run = True
    player = Player(sc, win_size, 50, [1, 0], 10)
    clock = pg.time.Clock()

    game_interface = Interface(10, sc)

    platforms = [pg.Rect(0, 590, 100, 100), pg.Rect(150, 550, 5000, 100)]

    all_sprites = pg.sprite.Group()
    shuriken = pg.transform.scale(load_image('shuriken.png'), (30, 30))
    sprite = pg.sprite.Sprite()
    sprite.image = pg.transform.scale(load_image("katana_start_pos.png"), (150, 150))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    katana = Katana(sprite)

    jump = False
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT or game_interface.hp <= 0:
                run = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not jump:
                    jump = True
                    player.check_gravity(platforms, True)
                    jump = False
                elif event.key == pg.K_f:
                    player.shot()
                    print(len(player.bullets))
                elif event.key == pg.K_LSHIFT:
                    player.lunge()
                elif event.key == pg.K_e:
                    katana.attack = True
                    game_interface.hp -= 1

        sc.fill((0, 0, 0))
        for platform in platforms:
            pg.draw.rect(sc, pg.Color('blue'), platform)

        player.move()
        game_interface.render()
        player.render(platforms)
        all_sprites.draw(sc)
        pg.display.flip()
        clock.tick(30)
