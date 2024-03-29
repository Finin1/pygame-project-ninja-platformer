import pygame as pg


class Interface:  # класс, который рисует интерфейс игрока
    def __init__(self, image, start_hp, screen):
        self.start_hp = start_hp
        self.hp = start_hp
        self.sc = screen

        self.damage = 0
        self.time = 100

        self.green_line = 200
        self.red_line = 200
        self.yellow_line = 0
        self.line_width = 30

        self.shuriken_image = image
        self.total_shurikens = 5

    def render(self):  # тут рендерится интерфейс игрока
        self.hp_bar()
        self.shuriken_lot()

    def hp_bar(self):  # здесь рисуется полоска здоровья 
        n = round(self.red_line * (self.hp / self.start_hp))
        pg.draw.rect(self.sc, (255, 0, 0), (20, 20, self.red_line, self.line_width))
        pg.draw.rect(self.sc, (0, 255, 0), (20, 20, n, self.line_width))
        if self.damage and self.time:
            pg.draw.rect(self.sc, (255, 255, 0),
                         (round(self.red_line * ((self.hp - self.damage + 1) / self.start_hp)), 20,
                          round((self.red_line / self.start_hp) * self.damage),
                          self.line_width))
            self.time -= 1

        if not self.time:  # по окончанию времени существования жёлтой линии
            self.hp -= self.damage
            self.damage = 0
            self.time = 100

        font = pg.font.Font(None, 40)
        text = font.render(f"{self.hp - self.damage}HP", 1, (255, 255, 255))
        self.sc.blit(text, (30, 23))

    def shuriken_lot(self):  # тут рисуется лот с сюрикеном и кол-вом сюрикенов 
        pg.draw.rect(self.sc, (112, 65, 15), (20, 75, 50, 50), 5)
        self.sc.blit(self.shuriken_image, (30, 85))
        font = pg.font.Font(None, 25)
        text = font.render(f"{self.total_shurikens}", 1, (255, 255, 255))
        self.sc.blit(text, (55, 105))
