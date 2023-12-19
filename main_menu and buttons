import pygame
pygame.init()
font_type = pygame.font.SysFont('arial', 36) # добавление шрифта


class Button: # кнопка
    def __init__(self, width, height, color): # параметры
        self.width = width
        self.height = height
        self.color = color

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos() # мышка
        click = pygame.mouse.get_pressed() # отслеживание клика
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.height)) # рисование кнопки
        if x < mouse[0] < x + self.width: # проверка клика на кнопку
            if y < mouse[1] < y + self.height:
                if click[0] == 1:
                    if action is not None:
                        action()
        text = font_type.render(message, True, (0, 0, 0)) # создание
        screen.blit(text, (x + 5, y + 5)) # отображение текста кнопки


def main(screen): # функция главного меню
    screen.fill((60, 240, 231))

    game_button = Button(125, 50, (2, 217, 16)) # кнопка играть
    game_button.draw(188, 100, 'Играть')

    stat_button = Button(201, 50, (2, 217, 16)) # кнопка статистики
    stat_button.draw(150, 200, 'Статистика')

    exit_button = Button(125, 50, (2, 217, 16)) # кнопка выхода
    exit_button.draw(188, 300, 'Выход', exit)


pygame.display.set_caption('Менюшки') # создание pygame окна
size = width, height = 501, 501
screen = pygame.display.set_mode(size)


running = True # флаг работы программы
main_menu = True # флаг главного меню
while running: # основной цикл
    for event in pygame.event.get(): # получение действия пользователя
        if event.type == pygame.QUIT: # проверка на закрытие окна
            running = False
    if main_menu:
        main(screen) # отображение главного меню
    pygame.display.flip() # отрисовка кадра
