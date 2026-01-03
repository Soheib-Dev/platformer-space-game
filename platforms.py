import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,move_x,move_y):
        super().__init__()
        self.image = pygame.image.load("images/platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = move_x
        self.move_y = move_y
        self.move_direction = 2
        self.move_counter = 2


    def update(self,player2,screen,all_sprites):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction* self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 100:

            self.move_direction *= -1
            self.move_counter = 0
    

