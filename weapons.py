import pygame

class Bullet:
    def __init__(self,x,y,direction):
        self.img = pygame.image.load("images/fire ball.png")
        self.image = pygame.transform.scale(self.img,(14,14))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.direction = direction

    def draw(self,win):
        win.blit(self.image,(self.rect.x,self.rect.y))
        
    def move(self):
        if self.direction == 1:
            self.rect.x += 5
        if self.direction == -1:
            self.rect.x -= 5

    def off_screen(self):
        return not(self.rect.x >= 0 and self.rect.x <= 1100)

class Weapon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.index = 0       
        image = pygame.image.load("images/bullet1.png")
        self.image = pygame.transform.scale(image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False

    def move(self,surface,player):
        self.rect.y += 1
        if self.rect.y > 500:
            self.rect.y -= 1
            self.rect.y += 0

        if player.handgun == False:
            if self.right: 
                surface.blit(self.image,(self.rect.x,self.rect.y))

            elif self.left:
                self.images = pygame.transform.flip(self.image,True,False)
                surface.blit(self.images,(self.rect.x,self.rect.y))

        elif player.handgun:
            if self.right: 
                surface.blit(self.image,(self.rect.x+50,self.rect.y))

            elif self.left:
                self.images = pygame.transform.flip(self.image,True,False)
                surface.blit(self.images,(self.rect.x- 55,self.rect.y))

class Weapon2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.index = 0       
        image = pygame.image.load("images/riffle.png")
        self.image = pygame.transform.scale(image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False

    def move(self,surface,player):

            
        if player.rifflerr == False:
            if self.right: 
                surface.blit(self.image,(self.rect.x,self.rect.y))

            elif self.left:
                self.images = pygame.transform.flip(self.image,True,False)
                surface.blit(self.images,(self.rect.x,self.rect.y))
        if player.rifflerr:
            if self.right: 
                surface.blit(self.image,(self.rect.x+50,self.rect.y))

            elif self.left:
                self.images = pygame.transform.flip(self.image,True,False)
                surface.blit(self.images,(self.rect.x- 55,self.rect.y))
                


                


              
      
