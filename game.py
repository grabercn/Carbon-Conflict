"""
game.py - Manages the main game loop, rendering, and basic UI.
"""

import pygame
import pygame_menu
from pygame_menu import themes
from settings import *
from player import Player
from map import load_map
from factions import factions

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Carbon Conflict")
        self.clock = pygame.time.Clock()

        # Initialize player and map data after the main menu
        self.turn_count = 1
        self.map_data = load_map("default.txt")
        self.player = None
        self.faction = factions["Green Order"]  # Example starting faction

        # Run the main menu here (pauses execution)
        self.main_menu()

    def main_menu(self):
        def start_the_game():
            # Initialize player after starting the game
            self.player = self.find_player()
            print("Starting the game...")
            self.run()  # Start the main game loop when the game starts
            self.running = True  # Start the game loop after pressing Play

        def quit_game():
            pygame.quit()
            quit()

        menu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
        #menu.add.text_input('Name: ', default='username', maxchar=20)
        menu.add.button('Play', start_the_game)
        menu.add.button('Quit', quit_game)

        # Pause execution and run the main menu event loop
        menu.mainloop(self.screen)


    def find_player(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == PLAYER:
                    return Player(x, y)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(0, -1, self.map_data)
        elif keys[pygame.K_DOWN]:
            self.player.move(0, 1, self.map_data)
        elif keys[pygame.K_LEFT]:
            self.player.move(-1, 0, self.map_data)
        elif keys[pygame.K_RIGHT]:
            self.player.move(1, 0, self.map_data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.end_turn()

    def end_turn(self):
        self.turn_count += 1
        print(f"Turn {self.turn_count} starts!")

    def draw_map(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                color = WHITE if tile == EMPTY else BLACK
                pygame.draw.rect(self.screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw_ui(self):
        font = pygame.font.SysFont(None, 24)
        turn_text = font.render(f"Turn: {self.turn_count}", True, WHITE)
        faction_text = font.render(f"Faction: {self.faction.name}", True, self.faction.color)
        self.screen.blit(turn_text, (10, 10))
        self.screen.blit(faction_text, (10, 30))

    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(GREEN)
            self.draw_map()
            self.player.draw(self.screen)
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(FPS)
