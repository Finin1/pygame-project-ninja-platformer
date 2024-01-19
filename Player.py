import pygame as pg
from Bullet import Bullet
from Entity import Entity
from Katana import Katana


class Player(Entity):  # Класс Игрока

    def __init__(self, screen, win, health, katana_sprite, face, speed: list, mass, pos=[5, 500], size=[50, 100]):
        # инициализация класса
        super().__init__(health, pos, size, speed, mass)
        self.screen = screen
        self.win_size = win
        self.body = None
        self.isJump = False
        self.jumpCount = 20
        self.bullets = []
        self.is_lunge = False
        self.lungeCount = 0
        self.facing = 1
        self.katana = Katana(katana_sprite)
        self.interface = face
        self.mouse = pg.mouse.get_pressed()

    def render(self, objects):  # Отрисовка персонажа и пуль
        super().render(self, objects)

        for bullet in self.bullets:
            if 0 < bullet.rect.x < self.win_size[0]:
                bullet.render()
            else:
                self.bullets.pop(self.bullets.index(bullet))
                bullet.finish_work()

    def move(self, x=10):  # Движение персонажа
        if not self.mouse[2]:
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

        self.katana.render(self.pos_x + 30 + (self.width // 2 * self.facing),
                           self.pos_y + (self.height // 2) + self.speed_y,
                           self.facing)

        self.lunge()

    def shot(self, shuriken, group):  # выстрел персонажа
        if self.interface.total_shurikens > 0:
            self.bullets.append(
                Bullet(self.pos_x, self.pos_y + (self.height // 2) // 2, shuriken, pg.transform.rotate(shuriken, 45),
                       self.facing, group))

            self.interface.total_shurikens -= 1

    def lunge(self):  # Одна из механик игры, выпад
        if self.is_lunge:
            if self.lungeCount < 5:
                self.pos_x += 50 * self.facing
                self.lungeCount += 1
            else:
                self.is_lunge = False
                self.lungeCount = 0

    def attack(self):  # основная атака персонажа
        self.katana.actived()

    def super_attack(self, img1, img2, group):  # супер атака персонажа
        if self.interface.can_super_attack:
            self.bullets.append(
                Bullet(self.pos_x, self.pos_y + (self.height // 2) // 2, img1, img2, self.facing, group))
            self.interface.can_super_attack = False

# if __name__ == '__main__':  # Демонстрация работы класса
#     pg.init()
#     win_size = (1000, 900)
#     sc = pg.display.set_mode(win_size)
#     run = True
#     clock = pg.time.Clock()
#
#     platforms = [pg.Rect(0, 590, 100, 100), pg.Rect(150, 550, 5000, 100), pg.Rect(600, 200, 100, 500),
#                  pg.Rect(700, 200, 100, 200), pg.Rect(600, 300, 100, 100), pg.Rect(700, 200, 100, 100)]
#
#     all_sprites = pg.sprite.Group()
#     shuriken = pg.transform.scale(load_image('shuriken.png'), (30, 30))
#     sprite = pg.sprite.Sprite()
#     sprite.image = pg.transform.scale(load_image("katana_start_pos.png"), (150, 150))
#     sprite.rect = sprite.image.get_rect()
#     all_sprites.add(sprite)
#
#     super_attack_image_1 = load_image('super_attack_1.png')
#     super_attack_image_2 = load_image('super_attack_2.png')
#
#     game_interface = Interface(shuriken, 10, sc, super_attack_image_1)
#
#     pauseMenu = PauseMenu(win_size)
#     menu_image = pg.transform.scale(load_image('main_menu.jpg'), win_size)
#
#     player = Player(sc, win_size, 50, sprite, [1, 0], 10)
#     jump = False
#     while run:
#         for event in pg.event.get():
#             if event.type == pg.QUIT or game_interface.hp <= 0:
#                 run = False
#
#             elif event.type == pg.KEYDOWN:
#                 if event.key == pg.K_SPACE and not jump:
#                     jump = True
#                     player.check_gravity(platforms, True)
#                     jump = False
#                 elif event.key == pg.K_f:
#                     player.shot()
#                 elif event.key == pg.K_LSHIFT:
#                     player.is_lunge = True
#                 elif event.key == pg.K_e:  # тут можно испытать hp_bar
#                     game_interface.damage += 1
#                 elif event.key == pg.K_q:
#                     player.super_attack()
#                 elif event.key == pg.K_ESCAPE:
#                     pauseMenu.is_pause = not pauseMenu.is_pause
#
#         if pauseMenu.is_pause:
#             mouse = pg.mouse.get_pressed()
#             if mouse[0]:
#                 player.katana.attack = True
#             if mouse[2]:
#                 player.katana.can_defend = True
#             else:
#                 player.katana.can_defend = False
#
#             sc.fill((0, 0, 0))
#             for platform in platforms:
#                 pg.draw.rect(sc, pg.Color('blue'), platform)
#
#             player.move()
#             game_interface.render()
#             player.lunge()
#             player.render(platforms)
#             all_sprites.draw(sc)
#         else:
#             sc.blit(menu_image, (0, 0))
#             pauseMenu.render()
#
#         pg.display.flip()
#         clock.tick(30)
