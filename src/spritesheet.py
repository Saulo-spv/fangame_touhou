import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = filename.replace('png', 'json')
    
        with open(self.meta_data) as file:
            self.data = json.load(file)
        
        file.close()
    
    def get_sprite(self, x, y, width, height, colorkey=(0,0,0)):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey(colorkey)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite
    
    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, width, height = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x, y, width, height)
        return image