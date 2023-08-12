import pygame
from settings import *
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH / 2, HEIGHT / 2

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -5

        if keystate[pygame.K_s]:
            self.speedy = 5

        if keystate[pygame.K_a]:
            self.speedx = -5

        if keystate[pygame.K_d]:
            self.speedx = 5
            
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


