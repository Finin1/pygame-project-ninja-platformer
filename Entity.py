import pygame
import typing


class Entity():
    def __init__(self, health, pos: list, size: typing.Tuple, v: list, mass):
        self.speed = v
        self.position = pos
        self.MAX_HEALTH = health
        self.health = health
        self.MASS = mass
        self.size = size # tuple(width, hight)
        self.in_air = True
        self.is_alive = True
        self.is_collided = {'top': False, 'bottom': False, 'right': False, 'left': False}

    def render(self, screen, objects): # куча проверок. Физика, состояние здоровья, скорость
        if self.health <= 0:
            self.is_alive = False
        # Гравитация
        # if self.in_air:
        #     # self.speed[1] += 10
        # else:
        #     self.speed[1] = 0

        self.check_collision(objects)

        self.position = [self.position[0] + self.speed[0] / fps, self.position[1] + self.speed[1] / fps]
        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(screen, pygame.Color('White'), rect=rect)
    
    def check_collision(self, objects):
        collided_platforms = self.get_hitbox().collidelistall(objects)
        if collided_platforms:
            for collided_index in collided_platforms:
                platform = platforms[collided_index]
                right_side = self.position[0] + self.size[0]
                left_side = self.position[0]
                top_side = self.position[1]
                bottom_side = self.position[1] + self.size[1]
                
                if platform.top <= bottom_side and platform.top >= top_side and self.is_collided['bottom'] == False:
                    modifier = abs(bottom_side - platform.top)
                    self.position[1] -= modifier 
                    # self.in_air = False
                    self.is_collided['bottom'] = not self.is_collided['bottom'] 
                elif platform.bottom >= top_side and platform.bottom <= bottom_side and self.is_collided['top'] == False:
                    modifier = abs(top_side - platform.bottom)
                    self.position[1] += modifier
                    self.speed[1] = 0
                    self.is_collided['top'] = not(self.is_collided['top'])
                elif platform.right >= left_side and platform.right <= right_side and self.is_collided['left'] == False:
                    modifier = abs(left_side - platform.right)
                    self.position[0] += modifier
                    self.speed[0] = 0
                    self.is_collided['left'] = not(self.is_collided['left'])
                elif platform.left <= right_side and platform.left >= left_side and self.is_collided['right'] == False:
                    modifier = abs(right_side - platform.left)
                    self.position[0] -= modifier 
                    self.speed[0] = 0
                    self.is_collided['right'] = not(self.is_collided['right'])

                if self.is_collided['top'] == 1:
                    self.speed[1] = 0
                if self.is_collided['bottom'] == 1:
                    self.speed[1] = 0
                if self.is_collided['right'] == 1:
                    self.speed[0] = 0
                if self.is_collided['left'] == 1:
                    self.speed[0] = 0

    def get_hitbox(self):
        hitbox = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        return hitbox
    

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    test_entity = Entity(10, [50, 0], (50, 50), [0, 0], 1)
    platforms = [pygame.Rect(0, 495, 500, 5), pygame.Rect(300, 440, 300, 100)]
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                test_entity.speed[1] += 100
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                test_entity.speed[0] += 100
        screen.fill((0, 0, 0))
        hitboxes = []

        for platform in platforms:
            pygame.draw.rect(screen, pygame.Color('blue'), platform)
        test_entity.render(screen, platforms)

        clock.tick(fps)
        pygame.display.flip()
        
    pygame.quit()
