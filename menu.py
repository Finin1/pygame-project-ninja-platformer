import pygame
from settings import fon, clock, fps
from button import Button


def main_menu(screen):  # главное меню
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(fon, (0, 0))

        game_button = Button(125, 50, (145, 30, 66))  # кнопка играть
        game_button.draw(100, 125, 'Играть')
        if game_button.action:
            return 'game'  # начинаем игру

        stat_button = Button(200, 50, (145, 30, 66))  # кнопка статистики
        stat_button.draw(0, 0, 'Статистика')
        if stat_button.action:
            return 'stat'  # открываем статистику

        exit_button = Button(125, 50, (145, 30, 66))  # кнопка выхода
        exit_button.draw(0, 462, 'Выход')
        if exit_button.action:
            return 'exit'  # выход из игры

        profile_button = Button(165, 50, (145, 30, 66))  # кнопка просмотра профиля
        profile_button.draw(859, 0, 'Профиль')
        if profile_button.action:
            return 'profile'  # reg/login

        pygame.display.flip()
        clock.tick(fps)


def stat(screen):  # просмотр статистики
    print('stat')
    return


def profile(screen):  # профиль игрока
    print('profile')
    return
