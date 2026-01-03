import pygame
from weapons import *


pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image,image_jump,animation1,animation2,scale):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.image_jump = pygame.transform.scale(image_jump,(int(width * scale), int(height * scale)))
        self.rect.topleft = (x,y)
        self.animation = []
        self.animation.append(animation1)
        self.animation.append(animation2)
        self.index = 0
        self.images = self.animation[int(self.index)]
        self.jump = False
        self.jump_height = -15
        self.left = False
        self.right = False
        self.stand = False
        self.player_vel = 5
        self.velocity_y = 0
        self.velocity_x = 0
        self.handgun = False
        self.shootloop = 0
        self.health = 400
        self.audio_jump = pygame.mixer.Sound("images/audio_jump.mp3")
        self.audio_jump.set_volume(0.2)
        self.bullets = []
        self.cooldown_count = 0
        self.game_over = 0
        self.scroll = 0
        self.ammo = 495     
        self.rifflerr = False
        self.is_switching =  False
        self.is_alive = True

    
    def draw(self,surface,all_sprites,bullets,players):
        if self.is_alive:
            self.move(surface,all_sprites,bullets,players)        

    def move(self,surface,all_sprites,bullets,players):
        
        self.images = self.animation[int(self.index)]
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                self.left = True
                self.right = False
                self.stand = False
                for sprite in all_sprites:
                    sprite.rect.x += 5
                self.velocity_x = -self.player_vel
                self.scroll -= 1
                
        elif keys[pygame.K_RIGHT] and self.scroll < 3000:
                    self.right = True
                    self.left = False
                    self.stand = False
                    
                        
                    for sprite in all_sprites:
                        sprite.rect.x -= 5
                    self.velocity_x = self.player_vel
                    self.scroll += 1
                    


        else:
                self.velocity_x = 0
                self.index = 0

        if keys[pygame.K_UP] and self.jump is False:
                    self.jump = True
                    self.stand = False
                    self.velocity_y = self.jump_height
                    self.audio_jump.play()


        self.cooldown()

        if self.handgun:
                if keys[pygame.K_SPACE] and self.cooldown_count == 0:
                    if self.ammo == 0:
                         self.ammo = 0
                    else:
                        self.ammo -= 1
                        if self.right:
                            bullet = Bullet(self.rect.x+ 75,self.rect.y + 40,self.direction())
                        if self.left:
                            bullet = Bullet(self.rect.x-25,self.rect.y + 45,self.direction())
                        self.bullets.append(bullet)
                        self.cooldown_count = 20
                for bullet in self.bullets:
                    bullet.move()
                    if bullet.off_screen():
                        self.bullets.remove(bullet)

        elif self.rifflerr:
                if keys[pygame.K_SPACE] and self.cooldown_count == 0:
                    if self.ammo == 0:
                         self.ammo = 0
                    else:
                        self.ammo -= 1
                        if self.right:
                            bullet = Bullet(self.rect.x+ 75,self.rect.y + 40,self.direction())
                        if self.left:
                            bullet = Bullet(self.rect.x-25,self.rect.y + 45,self.direction())
                        self.bullets.append(bullet)
                        self.cooldown_count = 40
                for bullet in self.bullets:
                    bullet.move()
                    if bullet.off_screen():
                        self.bullets.remove(bullet)


        self.rect.x += self.velocity_x

        if not self.stand:
            if self.jump:
                if self.left:
                    self.image_jump_left = pygame.transform.flip(self.image_jump,True,False)
                    surface.blit(self.image_jump_left,(self.rect.x,self.rect.y))
                else:
                    surface.blit(self.image_jump,(self.rect.x,self.rect.y))
                    
            elif self.left:
                self.index += 0.1
                self.images = pygame.transform.flip(self.images,True,False)
                surface.blit(self.images,(self.rect.x,self.rect.y))
                if self.index > len(self.animation):
                    self.index = 0
                

            elif self.right:
                self.index += 0.1
                surface.blit(self.images,(self.rect.x,self.rect.y))
                if self.index > len(self.animation):
                     self.index = 0
                
                    

            
            else:
                if self.right:
                    surface.blit(self.images,(self.rect.x,self.rect.y))
                else:
                    self.images = pygame.transform.flip(self.images,True,False)
                    surface.blit(self.images,(self.rect.x,self.rect.y))

            
            
        pygame.draw.rect(surface,(255,0,0),(25,50,400,25))
        pygame.draw.rect(surface,(0,255,0),(25,50,self.health,25))

            
    

    def direction(self):
        if self.left:
            return -1
        if self.right:
            return 1
        
    def cooldown(self):
        if self.cooldown_count >= 50:
            self.cooldown_count = 0
        if self.cooldown_count > 0:
            self.cooldown_count += 1

