import json
import pygame
from button import Button
from save_stats import save_stat
from load_images import load_image
from settings import clock, fps, font_type, name_file_stat


def main_menu():  # главное меню
    size = width, height = 1024, 512
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image('main_menu.jpg'), (width, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(fon, (0, 0))

        game_button = Button(125, 50, (145, 30, 66))  # кнопка играть
        game_button.draw(screen, 100, 125, 'Играть')
        if game_button.action:
            return 'game'  # начинаем игру

        stat_button = Button(200, 50, (145, 30, 66))  # кнопка статистики
        stat_button.draw(screen, 0, 0, 'Статистика')
        if stat_button.action:
            return 'stat'  # открываем статистику

        exit_button = Button(125, 50, (145, 30, 66))  # кнопка выхода
        exit_button.draw(screen, 0, 462, 'Выход')
        if exit_button.action:
            return 'exit'  # выход из игры

        pygame.display.flip()
        clock.tick(fps)


def stat():  # просмотр статистики
    size = width, height = 1200, 675
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image('stat_menu.png'), (width, height))

    save_stat("stat_opens")

    with open(name_file_stat, mode='r') as stat_file:
        data = json.load(stat_file)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(fon, (0, 0))

        text = font_type.render(f'Запусков программы: {data["starts"]}', True, (255, 0, 0))  # создание
        screen.blit(text, (20, 20))  # отображение текста

        text = font_type.render(f'Запусков игры: {data["game_starts"]}', True, (255, 0, 0))
        screen.blit(text, (20, 50))

        text = font_type.render(f'Просмотров статистики: {data["stat_opens"]}', True, (255, 0, 0))
        screen.blit(text, (20, 80))

        exit_button = Button(125, 50, (145, 30, 66))  # кнопка выхода
        exit_button.draw(screen, 0, 625, 'Выход')
        if exit_button.action:
            return  # выход в главное меню

        pygame.display.flip()
        clock.tick(fps)
