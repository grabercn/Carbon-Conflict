"""
main.py - Entry point for Carbon Conflict
Initializes pygame and starts the game loop.
"""

import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
