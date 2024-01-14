import pygame
from random import choice
rooms = [{'id': 1, 'npc': [], 'platforms': [], 'start_type': 1, 'exit_type': 1}, {'id': 2, 'npc': [], 'platforms': [], 'start_type': 2, 'exit_type': 2},
         {'id': 3, 'npc': [], 'platforms': [], 'start_type': 1, 'exit_type': 2}, {'id': 4, 'npc': [], 'platforms': [], 'start_type': 2, 'exit_type': 3},
         {'id': 5, 'npc': [], 'platforms': [], 'start_type': 1, 'exit_type': 3}, {'id': 6, 'npc': [], 'platforms': [], 'start_type': 2, 'exit_type': 4}, 
         {'id': 7, 'npc': [], 'platforms': [], 'start_type': 1, 'exit_type': 4}, {'id': 8, 'npc': [], 'platforms': [], 'start_type': 2, 'exit_type': 1},
         {'id': 9, 'npc': [], 'platforms': [], 'start_type': 3, 'exit_type': 1}, {'id': 10, 'npc': [], 'platforms': [], 'start_type': 4, 'exit_type': 1},
         {'id': 11, 'npc': [], 'platforms': [], 'start_type': 3, 'exit_type': 2}, {'id': 12, 'npc': [], 'platforms': [], 'start_type': 4, 'exit_type': 2},
         {'id': 13, 'npc': [], 'platforms': [], 'start_type': 3, 'exit_type': 3}, {'id': 14, 'npc': [], 'platforms': [], 'start_type': 4, 'exit_type': 3}, 
         {'id': 15, 'npc': [], 'platforms': [], 'start_type': 3, 'exit_type': 4}, {'id': 16, 'npc': [], 'platforms': [], 'start_type': 4, 'exit_type': 4}] # Варианты комнат

class Level:
    def __init__(self, room_count=5):
        self.curr_level = 0
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
        screen.fill(0, 0, 0)
        curr_platforms = self.rooms[self.curr_level]['platforms']
        curr_npcs = self.rooms[self.curr_level]['npc']
        for platform in curr_platforms:
            pygame.draw.rect(screen, pygame.Color('blue'), platform)
        for npc in curr_npcs:
            npc.render()

    def next_level(self):
        self.curr_level += 1
        

    