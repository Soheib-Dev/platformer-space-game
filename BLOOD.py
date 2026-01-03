import pygame

class Blood(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images_right = []
        self.index = 0
        self.counter = 0
        for num in range(1,3):
            image_right = pygame.image.load(f"images/blood pop{num}.png")
            self.images_right.append(image_right)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.enemy_death = False


    def move(self):
        walk_cooldown = 20
        self.counter += 1
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 0.1
            if self.index >= len(self.images_right):
                self.enemy_death = True
            self.image = self.images_right[int(self.index)]

    def draw(self,surface,enemy):
        surface.blit(self.image,(enemy.rect.x,enemy.rect.y))

