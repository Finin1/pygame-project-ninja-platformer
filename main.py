import pygame
from settings import screen, clock, fps, size
from load_images import load_image
from menu import main_menu, stat, profile
from Entity import Entity
from Player import Player
from Interface import Interface

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
    pygame.init()
    win_size = size
    sc = pygame.display.set_mode(win_size)
    run = True
    player = Player(sc, win_size, 50, [1, 0], 10)
    clock = pygame.time.Clock()

    platforms = [pygame.Rect(0, 590, 100, 100), pygame.Rect(150, 550, 5000, 100)]

    all_sprites = pygame.sprite.Group()
    shuriken = pygame.transform.scale(load_image('shuriken.png'), (30, 30))
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("katana_start_pos.png"), (150, 150))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    game_interface = Interface(shuriken, 10, sc)
    player.load_sprites(sprite)
    katana = player.get_katana()

    jump = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or game_interface.hp <= 0:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jump:
                    player.jump(platforms)
                elif event.key == pygame.K_f:
                    player.shot(game_interface, shuriken, all_sprites)
                elif event.key == pygame.K_LSHIFT:
                    player.lunge()
                elif event.key == pygame.K_e:  # тут можно испытать hp_bar
                    game_interface.damage += 1

        player.mouse = pygame.mouse.get_pressed()
        if player.mouse[0]:
            katana.attack = True
        if player.mouse[2]:
            katana.can_defend = True
        else:
            katana.can_defend = False

        sc.fill((0, 0, 0))
        for platform in platforms:
            pygame.draw.rect(sc, pygame.Color('blue'), platform)

        player.move()
        game_interface.render()
        player.render(platforms)
        all_sprites.draw(sc)
        pygame.display.flip()
        clock.tick(30)