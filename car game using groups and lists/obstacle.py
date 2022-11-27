import pygame
from random import randint, choice
import math

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,game_state,player):
        super().__init__()
        self.game_state = game_state
        self.player = player
        self.start_pos = pygame.math.Vector2(choice([50,250,430]),randint(-250,-50))
        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.start_pos))
        
        self.speed = 10
        self.screen = pygame.display.get_surface()

    def move(self):
        self.new_pos = pygame.math.Vector2(choice([50,250,430]),randint(-250,-50))
        self.rect.y += self.speed
        if self.speed >= 16:
            self.speed = 16

    def destroy():
        if self.rect.y > 650:
            self.kill()
        
    def update(self):
        self.move()
        
