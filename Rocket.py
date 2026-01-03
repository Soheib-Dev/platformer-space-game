import pygame

class rocket(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/rocket.png")
        self.rocket = pygame.transform.scale(self.image,(140,140))
        self.rect = self.rocket.get_rect()
        self.rect.topleft = (x,y)
