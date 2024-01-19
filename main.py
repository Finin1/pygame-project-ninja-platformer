import pygame
from settings import screen, font_type
from load_images import load_image
from menu import main_menu, stat, profile
from Katana import Katana
from Player import Player
from Level import Level
from Interface import Interface
from pause_menu import PauseMenu
from json import load

pygame.init()

next = main_menu()
while True:  # ожидание действия
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
    win_size = 1600, 900
    sc = pygame.display.set_mode(win_size)
    run = True
    clock = pygame.time.Clock()
    
    level = Level(2)
    
    platforms = [pygame.Rect(0, 590, 100, 100), pygame.Rect(150, 550, 5000, 100)]

    all_sprites = pygame.sprite.Group()
    shuriken = pygame.transform.scale(load_image('shuriken.png'), (30, 30))
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("katana_start_pos.png"), (150, 150))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    super_attack_image_1 = load_image('super_attack_1.png')
    super_attack_image_2 = load_image('super_attack_2.png')

    game_interface = Interface(shuriken, 10, sc, super_attack_image_1)
    katana = Katana(sprite)
    mouse = pygame.mouse.get_pressed()

    # crate_rooms(all_sprites)
    level = Level(2)

    pauseMenu = PauseMenu(win_size)
    main_image = pygame.transform.scale(load_image('main_menu.jpg'), win_size)
    with open('data/settings.json', 'r', encoding='utf-8') as file:
        fps = load(file)["fps"]

    player = Player(sc, win_size, 50, sprite, game_interface,  [1, 0], 10)
    jump = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or game_interface.hp <= 0:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jump:
                    jump = True
                    player.check_gravity(platforms, True)
                    jump = False
                elif event.key == pygame.K_f:
                    player.shot(shuriken, all_sprites)
                elif event.key == pygame.K_LSHIFT:
                    player.is_lunge = True
                elif event.key == pygame.K_e:  # тут можно испытать hp_bar
                    game_interface.damage += 1
                elif event.key == pygame.K_q:
                    player.super_attack(super_attack_image_1, super_attack_image_2, all_sprites)
                elif event.key == pygame.K_ESCAPE:
                    pauseMenu.is_pause = not pauseMenu.is_pause

        if pauseMenu.is_pause:
            if player.mouse[0]:
                player.katana.attack = True
            if player.mouse[2]:
                player.katana.can_defend = True
            else:
                player.katana.can_defend = False

            if player.pos_x + player.width >= win_size[0]:
                if level.next_level():
                    running = False
                player.pos_x = 0
            elif player.pos_y + player.height >= win_size[1]:
                player.pos_x = 0
                player.pos_y = 500
                game_interface.damage += 1

            level.render_room(sc)
            player.move()
            game_interface.render()
            player.render(level.get_platforms())
            all_sprites.draw(sc)
        else:
            sc.blit(main_image, (0, 0))
            pauseMenu.render()

        pygame.display.flip()
        clock.tick(fps)
