import pygame as pg


# import Entity


class Player:
    def __init__(self, x=500, y=500):
        self.pos_x = x
        self.pos_y = y
        self.body = None
        self.isJump = False
        self.jumpCount = 20

    def render(self):
        pg.draw.rect(sc, pg.Color('white'), (self.pos_x, self.pos_y, 50, 100))

    def move(self, x=10, y=1):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.pos_x -= x
        elif keys[pg.K_d]:
            self.pos_x += x

    def jump(self):
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


if __name__ == '__main__':
    pg.init()
    sc = pg.display.set_mode((1000, 900))
    run = True
    player = Player()
    clock = pg.time.Clock()
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    print('ss')
                    player.isJump = True

        sc.fill((0, 0, 0))
        player.jump()
        player.move()
        player.render()
        pg.display.flip()
        clock.tick(30)
