import pygame
from load_images import load_image

pygame.init()


pygame.display.set_caption('Ninja: "Hurricane Chronicles"')
size = width, height = 1024, 512
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font_type = pygame.font.SysFont('arial', 36)  # шрифт
fps = 60

fon = pygame.transform.scale(load_image('main_menu.jpg'), (width, height))
