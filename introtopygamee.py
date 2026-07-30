import pygame
import sys

# Initalize Pygame
pygame.init()

# Screen dimension
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Example")

#Clock for FPS
clock = pygame.time.Clock()
EPS = 60

# Color definitions
WHITE = (255, 255, 255)
BLACK =(0,0,0)

# Sprite class
class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect




    




def update(self, keys):
        # Simple movement with W, A, S, and D keys
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_d]:
             self.rect.x += 5
        if keys[pygame.K_w]:
             self.rect.x -= 5
        if keys[pygame.K_s]:
             self.react.x += 5





















































