import pygame

pygame.init()


pygame.display.set_caption('Ninja: "Hurricane Chronicles"')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 900))
font_type = pygame.font.SysFont('arial', 36)  # шрифт
fps = 60
name_file_stat = 'data/stat.json'
