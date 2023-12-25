import pygame
import typing


class Entity():
    def __init__(self, health, pos: list, size: list, v: list, mass):
        self.speed_x = v[0] # list(v_x, v_y)
        self.speed_y = v[1]
        self.pos_x = pos[0]
        self.pos_y = pos[1] # list(x, y)
        self.MAX_HEALTH = health
        self.health = health
        self.MASS = mass
        self.width = size[0]
        self.height = size[1] # list(width, height)
        self.in_air = False
        self.is_alive = True
        self.is_collided = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.accel = 1

    def render(self, screen, objects): # Отрисовка, куча проверок. Физика, состояние здоровья, скорости
        # Заготовка для проверки жива ли сущность
        if self.health <= 0:
            self.is_alive = False

        self.gravity_rect = pygame.Rect(self.pos_x, self.pos_y + self.height, self.width, 1)
        
        # pygame.draw.rect(self.screen, pygame.Color('Red'), self.test_rect) # Отрисовка для тестов

        self.check_gravity(objects)
        self.check_collision(objects)
  
        pygame.draw.rect(self.screen, pygame.Color('white'), (self.pos_x, self.pos_y, self.width, self.height))
    
    def check_collision(self, objects):
        collided_platforms = self.get_hitbox().collidelistall(objects)
        if collided_platforms:
            for collided_index in collided_platforms:
                platform = objects[collided_index]
                right_side = self.pos_x + self.width
                left_side = self.pos_x
                top_side = self.pos_y
                bottom_side = self.pos_y + self.height
                
                if platform.top <= bottom_side and platform.top >= top_side and self.is_collided['bottom'] == False: # Нижная коллизия
                    modifier = abs(bottom_side - platform.top)
                    self.pos_y -= modifier 
                    self.is_collided['bottom'] = True 
                elif platform.bottom >= top_side and platform.bottom <= bottom_side and self.is_collided['top'] == False: # Верхняя коллизия
                    modifier = abs(top_side - platform.bottom)
                    self.pos_y += modifier
                    self.speed_y = 0
                    self.is_collided['top'] = True
                elif platform.right >= left_side and platform.right <= right_side and self.is_collided['left'] == False: # Левая коллизия
                    modifier = abs(left_side - platform.right)
                    self.pos_x += modifier
                    self.speed_x = 0
                    self.is_collided['left'] = True
                elif platform.left <= right_side and platform.left >= left_side and self.is_collided['right'] == False: # Правая коллизия
                    modifier = abs(right_side - platform.left)
                    self.pos_x -= modifier 
                    self.speed_x = 0
                    self.is_collided['right'] = True

                # Обнуление скоростей, если есть столкновение
                if self.is_collided['top']:
                    self.speed_y = 0
                if self.is_collided['bottom']:
                    self.speed_y = 0
                if self.is_collided['right']:
                    self.speed_x = 0
                if self.is_collided['left']:
                    self.speed_x = 0

    def get_hitbox(self):
        hitbox = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        return hitbox
    
    def check_gravity(self, objects, jump=False): # Проверка гравитации 
        # Проверка прыжок ли это
        if jump and self.speed_y == 0:
            self.speed_y = -20
            self.pos_y += -2
        else:
            for platform in objects:
                big_rect = (self.gravity_rect.left, self.gravity_rect.top - 2000, self.gravity_rect.width, self.gravity_rect.height + 4000)
                if platform.colliderect(big_rect): # Выбор платформы над которой сущность
                    if platform.colliderect(self.gravity_rect): # Проверка стоит ли прямоугольник над платформой
                        self.speed_y = 0
                        self.pos_y = platform.top - self.height
                    else:
                        self.speed_y += self.accel
                        self.pos_y += self.speed_y
