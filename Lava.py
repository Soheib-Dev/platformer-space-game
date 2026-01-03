import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load("images/lava1.png")
        self.image = pygame.transform.scale(image,(145,140))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
