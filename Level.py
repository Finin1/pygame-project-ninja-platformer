import pygame
from random import choice
from load_images import load_image
rooms = [{'id': 1, 'npc': [], 'platforms': [pygame.Rect(0, 800, 1600, 100), pygame.Rect(0, 900, 1600, 1)], 'start_type': 1, 'exit_type': 1},
         {'id': 2, 'npc': [], 'platforms': [pygame.Rect(0, 800, 450, 100), pygame.Rect(0, 900, 1600, 1), pygame.Rect(575, 650, 500, 50), pygame.Rect(1200, 500, 500, 600)], 'start_type': 1, 'exit_type': 2}, 
         {'id': 3, 'npc': [], 'platforms': [pygame.Rect(1200, 800, 450, 100), pygame.Rect(0, 900, 1600, 1), pygame.Rect(575, 650, 500, 50), pygame.Rect(0, 500, 500, 600)], 'start_type': 2, 'exit_type': 1}
         ] # Варианты комнат

class Level:
    def __init__(self, room_count=5):
        self.curr_level = 0
        self.last_level = room_count
        self.rooms = []
        self.rooms.append(choice(rooms))
        for i in range(room_count): # Выбор случайного набора комнат для уровня (с входом и выходом на одном ярусе)
            roll = True
            while roll:
                next_room = choice(rooms)
                if self.rooms[i]['exit_type'] == next_room['start_type']:
                    roll = False
                    self.rooms.append(next_room)

    def render_room(self, screen):
        screen.fill((117, 187, 253))
        all_platforms = pygame.sprite.Group()
        sun = load_image('sun.jpg')
        sun = pygame.transform.scale(sun, (300, 175))
        sun_texture = pygame.sprite.Sprite(all_platforms)
        sun_texture.image = sun
        sun_texture.rect = sun.get_rect()
        all_platforms.add(sun_texture)
        sun_texture.rect.x = 1250
        sun_texture.rect.y = 100
        curr_platforms = self.rooms[self.curr_level]['platforms']
        curr_npcs = self.rooms[self.curr_level]['npc']

        for platform in curr_platforms:
            texture = load_image('dirt.png')
            texture = pygame.transform.scale(texture, (platform.width, platform.height))
            platform_texture = pygame.sprite.Sprite(all_platforms)
            platform_texture.image = texture
            platform_texture.rect = platform
            all_platforms.add(platform_texture)
            platform_texture.rect.x = platform.topleft[0]
            platform_texture.rect.y = platform.topleft[1]
            
        for npc in curr_npcs:
            npc.render()
        all_platforms.draw(screen)

    def get_platforms(self):
        return self.rooms[self.curr_level]['platforms']
    
    def next_level(self):
        if self.curr_level != self.last_level: # Проверка не является ли уровень последним
            self.curr_level += 1
        else:
            return True
        

    