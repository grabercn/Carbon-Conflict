"""
player.py - Defines the player character and movement logic.
"""

import pygame
from settings import TILE_SIZE, BLUE, WALL

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, map_data):
        new_x = self.x + dx
        new_y = self.y + dy

        if map_data[new_y][new_x] != WALL:
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
