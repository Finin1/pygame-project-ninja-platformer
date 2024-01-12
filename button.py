import pygame
from settings import screen, font_type


class Button:  # кнопка
    def __init__(self, width, height, color):  # параметры
        self.width = width
        self.height = height
        self.color = color
        self.action = False

    def draw(self, x, y, message):
        mouse = pygame.mouse.get_pos()  # мышка
        click = pygame.mouse.get_pressed()  # отслеживание клика
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))  # рисование кнопки
        if x < mouse[0] < x + self.width:  # проверка клика на кнопку
            if y < mouse[1] < y + self.height:
                if click[0] == 1:
                    pygame.time.delay(300)
                    self.action = True
        text = font_type.render(message, True, (255, 255, 255))  # создание
        screen.blit(text, (x + 5, y + 5))  # отображение текста кнопки