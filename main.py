from settings import pygame, screen, clock, fps
from menu import main_menu, stat, profile

pygame.init()

while True:  # ожидание действия
    next = main_menu(screen)
    if next == 'exit':
        exit()
    elif next == 'stat':
        stat(screen)
    elif next == 'profile':
        profile(screen)
    else:
        break

running = True
while running:  # основной игровой процесс
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print('Игровой процесс')
    pygame.display.flip()
    clock.tick(fps)
