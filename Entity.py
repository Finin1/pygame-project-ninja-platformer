import pygame
import typing


class Entity():
    def __init__(self, health, pos: list, size: typing.Tuple, v: list, mass):
        self.v = v
        self.pos = pos
        self.MAX_HEALTH = health
        self.cur_health = health
        self.MASS = mass
        self.size = size # tuple(hight, width)

    def render(self, screen): # куча проверок. Физика, состояние здоровья, скорость
        test_entity.position = (test_entity.position[0] + test_entity.speed[0] / fps, test_entity.position[1] + test_entity.speed[1] / fps)
        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(screen, pygame.Color('White'), rect=rect)
    
    @property
    def speed(self):
        return self.v

    @speed.setter
    def speed(self, v):
        self.v = v
    
    @property
    def health(self):
        return self.cur_health
    
    @health.setter
    def health(self, new_health):
        self.cur_health = new_health

    @property
    def position(self):
        return self.pos
    
    @position.setter
    def position(self, coords):
        self.pos = coords
    

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    test_entity = Entity(10, [0, 0], (50, 50), [0, 0], 1)
    print(test_entity.speed)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                test_entity.speed[0] += 10
                test_entity.speed[1] += 10
        screen.fill((0, 0, 0))
        test_entity.render(screen)
        clock.tick(fps)
        pygame.display.flip()
        
    pygame.quit()
