import pygame as pg
from Player import Player
import Bullet


class Weapon:
    def __init__(self, obj, damage=1):  # x, y, width, height
        # self.pos_x = x
        # self.pos_y = y
        # self.width = width
        # self.height = height
        self.damage = damage
        self.hitbox = pg.Rect(obj.x, obj.y, obj.width, obj.height)

    def check_collision(self, obj):
        wal = self.hitbox.collidelistall(obj)
        if len(wal) > 0:
            print('y')


if __name__ == '__main__':  # демонстрация работы класса
    pg.init()
    win_size = (1000, 900)
    sc = pg.display.set_mode(win_size)
    run = True
    player = Player(sc, win_size)
    clock = pg.time.Clock()
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
        pg.display.flip()
        clock.tick(30)
