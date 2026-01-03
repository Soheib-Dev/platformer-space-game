import pygame 
import random
from weapons import *

class SMALL_Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/alien.gif")
        self.rect =  self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 2
        self.move_counter = 0
        self.velocity_x = 0

    def update(self,player2,screen,all_sprites):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter = 0
    
        
class MIDDLE_Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images_right = []
        self.index = 0
        self.counter = 0
        for num in range(1,8):
            image_right = pygame.image.load(f"images/R{num}E.png")
            self.images_right.append(image_right)

        self.image = self.images_right[self.index]
        self.rect =  self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.rectangle = (self.rect.x + 20,self.rect.y,28,60)
        self.hitbox = (self.rect.x + 20,self.rect.y,28,60)
        self.shock = False
        self.move_counter = 0
        self.left = False
        self.velocity_y = 0
        self.gravity = 1
        self.velocity_x = 0
        self.right = False
        self.visible = False
        self.health_x = 100
    
    
    def update(self,player,screen,all_sprites):
        walk_cooldown = 20

        if self.visible == False:
            self.counter += 1
            if self.shock == False:
                self.right = True
                self.left = False
                self.rect.x += self.speed
                self.move_counter += 1
                if abs(self.move_counter) > 50:
                    self.speed *= -1
                    self.move_counter = 0
                    self.left = True
                    self.right = False
            
            if self.shock == True: 
                if self.rect.x < player.rect.x:
                    self.rect.x += self.speed
                if self.rect.x > player.rect.x:
                    self.rect.x -= self.speed
                        

        self.rect.y += self.velocity_y
        self.velocity_y += self.gravity
        self.rectangle = (self.rect.x - 300,self.rect.y - 325,600,400)  
        self.hitbox = (self.rect.x + 20,self.rect.y,28,60)  
        self.health = (self.rect.x,self.rect.y - 10, self.health_x, 10)
        pygame.draw.rect(screen,(255,0,0),(self.rect.x,self.rect.y - 10, 100, 10))
        pygame.draw.rect(screen,(0,255,0),self.health)

        
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 2
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]

    def hit(self): 
        self.health_x -= 50


class Big_Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images_right = []
        self.index = 0
        self.counter = 0
        for num in range(1,2):
            image_right = pygame.image.load(f"images/enime_{num}.png")
            big_enemy = pygame.transform.scale(image_right,(140,140))
            self.images_right.append(big_enemy)
        self.image = self.images_right[self.index]
        self.rect =  self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.rectangle = (self.rect.x + 20,self.rect.y,56,120)
        self.hitbox = (self.rect.x + 20,self.rect.y,28,60)
        self.shock = False
        self.move_counter = 0
        self.left = False
        self.velocity_y = 0
        self.gravity = 1
        self.velocity_x = 0
        self.right = False
        self.visible = False
        self.health_x = 100
        self.bullets = []
        self.cooldown_count = 0
    
    
    def update(self,player,screen,all_sprites):
        walk_cooldown = 10


        if self.visible == False:
            self.counter += 1
            if self.shock == False:
                self.right = True
                self.left = False
                self.rect.x += self.speed
                self.move_counter += 1
                if abs(self.move_counter) > 50:
                    self.speed *= -1
                    self.move_counter = 0
                    self.left = True
                    self.right = False
            
            if self.shock == True:
                global bullet
                if self.cooldown_count == 0:
                    if self.rect.x < player.rect.x:
                        self.right = True
                        self.left = False
                        if self.right:
                            bullet = Bullet(self.rect.x,self.rect.y + 70,self.direction())
                    if self.rect.x > player.rect.x:
                        self.left = True
                        self.right = False
                        if self.left:
                            bullet = Bullet(self.rect.x,self.rect.y + 70,self.direction())
                    self.cooldown_count = 45

                    if self.health_x <= 0:
                        self.bullets.remove(bullet)                
                    self.bullets.append(bullet)
            for bullet in self.bullets:
                bullet.move()
                if bullet.off_screen():
                    self.bullets.remove(bullet)

        if self.cooldown_count > 0:
            self.cooldown_count -= 1

        self.rect.y += self.velocity_y
        self.velocity_y += self.gravity
        self.rectangle = (self.rect.x - 600,self.rect.y - 675,1200,800)  
        self.hitbox = (self.rect.x + 20,self.rect.y,28,60)  
        self.health = (self.rect.x,self.rect.y - 10, self.health_x, 10)
        pygame.draw.rect(screen,(255,0,0),(self.rect.x,self.rect.y - 10, 100, 10))
        pygame.draw.rect(screen,(0,255,0),self.health)
        pygame.draw.rect(screen,(0,255,0),self.rectangle,1)        
        
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 2
            if self.index >= len(self.images_right):
                self.index = 0
            self.image = self.images_right[self.index]

    def hit(self): 
        self.health_x -= 20

    def direction(self):
        if self.left:
            return -1
        if self.right:
            return 1
            

