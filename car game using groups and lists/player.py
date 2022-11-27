import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image and rect
        self.image0 = pygame.image.load('graphics/car_left.png').convert_alpha()
        self.image1 = pygame.image.load('graphics/car_regular.png').convert_alpha()
        self.image2 = pygame.image.load('graphics/car_right.png').convert_alpha()
        self.image = self.image1
        
        self.rect = self.image.get_rect(center = (245,600))

        # some random attributes
        self.screen = pygame.display.get_surface()
        self.speed = 20

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.screen.blit(self.image2,self.rect)
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.screen.blit(self.image0,self.rect)
        else: self.screen.blit(self.image1,self.rect)
            
        self.wall_collisions()

    def wall_collisions(self):
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.screen.blit(self.image1,self.rect)
        if self.rect.left < 0:
            self.rect.left = 0
            self.screen.blit(self.image1,self.rect)


    def update(self):
        self.input()
        
