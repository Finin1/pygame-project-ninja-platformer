import pygame
from settings import screen, clock, fps
from load_images import load_image
from menu import main_menu, stat, profile
from Entity import Entity
from Player import Player

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
    win_size = (1000, 900)
    sc = pygame.display.set_mode(win_size)
    run = True
    player = Player(sc, win_size, 50, [1, 0], 10)
    clock = pygame.time.Clock()

    platforms = [pygame.Rect(0, 500, 100, 100), pygame.Rect(0, 550, 5000, 100)]

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("katana_start_pos.png"), (150, 150))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)

    player.load_sprites(sprite=sprite)
    katana = player.get_katana()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump(platforms)
                elif event.key == pygame.K_f:
                    player.shot()                 
                elif event.key == pygame.K_LSHIFT:
                    player.lunge()
                elif event.key == pygame.K_e:
                    katana.attack = True

        sc.fill((0, 0, 0))
        for platform in platforms:
            pygame.draw.rect(sc, pygame.Color('blue'), platform)

        player.move()
        player.render(platforms)
        all_sprites.draw(sc)
        pygame.display.flip()
        clock.tick(30)
