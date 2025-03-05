# resourcemanager.py
import pygame

class ResourceManager:
    def __init__(self):
        self.tiles = {}
        self.sprites = {}
        self.backgrounds = {}

    def load_tile(self, tile_name, image_path):
        """ Load an individual tile from an image """
        tile_image = pygame.image.load(image_path).convert_alpha()
        self.tiles[tile_name] = tile_image

    def load_sprite(self, sprite_name, image_path, tile_width, tile_height):
        """ Load a sprite sheet and extract tiles of specified width and height """
        sprite_sheet = pygame.image.load(image_path).convert_alpha()
        self.sprites[sprite_name] = {
            'sheet': sprite_sheet,
            'tile_width': tile_width,
            'tile_height': tile_height
        }

    def load_background(self, background_name, image_path):
        """ Load a background image """
        background = pygame.image.load(image_path).convert_alpha()
        self.backgrounds[background_name] = background

    def get_tile(self, tile_name):
        """ Return the tile image for a given tile name """
        return self.tiles.get(tile_name)

    def get_sprite(self, sprite_name, frame_x, frame_y):
        """ Return a specific frame from the sprite sheet based on its x and y grid position """
        sprite_info = self.sprites.get(sprite_name)
        if not sprite_info:
            return None
        
        sheet = sprite_info['sheet']
        tile_width = sprite_info['tile_width']
        tile_height = sprite_info['tile_height']
        
        # Calculate the position of the frame in the sprite sheet
        frame_rect = pygame.Rect(frame_x * tile_width, frame_y * tile_height, tile_width, tile_height)
        return sheet.subsurface(frame_rect)

    def get_background(self, background_name):
        """ Return the background image for a given name """
        return self.backgrounds.get(background_name)
