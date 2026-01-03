import pygame
from human import *
from tile import *
from enemy import *
from weapons import *
from health import *
from Buttons import *
from BLOOD import *
from Lava import *
from platforms import *
from ammo import *
from Rocket import *
import random


pygame.init()  


screen_width = 1100
screen = pygame.display.set_mode((screen_width,700))
pygame.display.set_caption("return to earth")
TILE_SIZE = 140

image_animation1 = pygame.image.load("images/player_walk_1.png")
image_animation2 = pygame.image.load("images/player_walk_2.png")
image_jump = pygame.image.load("images/jump.png")

planet_images = []
bg_images = []
bg_image = []

img = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(img,(1100,700))
bg_images.append(bg)


img = pygame.image.load("images/earth.png")
earth = pygame.transform.scale(img,(250,250))
bg_image.append(earth)

img1 = pygame.image.load("images/mars.png")
mars = pygame.transform.scale(img1,(100,100)) 
bg_image.append(mars)

img4 = pygame.image.load("images/planet4.png")
planet3 = pygame.transform.scale(img4,(50,50))
planet_images.append(planet3)

img13 = pygame.image.load("images/planet2.png")
planet2 = pygame.transform.scale(img13,(150,150)) 
planet_images.append(planet2)

img12 = pygame.image.load("images/planet5.png")
planet4 = pygame.transform.scale(img12,(150,150)) 
planet_images.append(planet4)

finish = False

bg_width = bg_images[0].get_width()
planets1_width = bg_image[1].get_width()
planets2_width = planet_images[0].get_width()

stone = pygame.image.load("images/stone.png")

music = pygame.mixer.Sound("images/music.wav")
music.set_volume(0.1)
music.play(loops=-1)

resume_img = pygame.image.load("images/button_resume.png")
resume = Button(304,300,resume_img,1)

quit_img = pygame.image.load("images/button_quit.png")
quit = Button(608,300,quit_img,1)

start_img = pygame.image.load("images/start_btn.png")
start = Button(304,300,start_img,0.75)

restart_img = pygame.image.load("images/restart_btn.png")
restart = Button(304,300,restart_img,1.5)

transform = pygame.image.load("images/fire ball.png")
volda = pygame.transform.scale(transform,(45,45))

intro = pygame.image.load("images/intro.jpg")

img44 = pygame.image.load("images/poused.jpg")
poused = pygame.transform.scale(img44,(1100,700))

img55 = pygame.image.load("images/end.jpg")
end = pygame.transform.scale(img55,(1100,700))

img66 = pygame.image.load("images/dead_image.png")
dead_img = pygame.transform.scale(img66,(150,150))


fps = 60
hide_frames = 0 

game_map = [
            "111000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "111000001000000000000000000000000000000000050000(00020900000000*000000000000000!0",
            "1110600003000000000001111.     111     11111111111,  ,.  1111111111,.     1111110",
            "111069100220002020401000000000000000001000000000000000000000000000000000000000000",
            "11111111111111111111818188888.111111111111188888888888888888888888888888888888888"]

all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
enime = pygame.sprite.Group()
weapons = pygame.sprite.Group()
enime_middle = pygame.sprite.Group()
enime_big = pygame.sprite.Group()
midcates = pygame.sprite.Group()
lavas = pygame.sprite.Group()
platforms_x = pygame.sprite.Group()
ammos = pygame.sprite.Group()
rockets = pygame.sprite.Group()
players = pygame.sprite.Group()
riffles = pygame.sprite.Group()

clock = pygame.time.Clock()

tile_width = stone.get_width()
tile_height = stone.get_height()

random_planets = random.randint(0,100)




for idx_row,row in enumerate(game_map):
     for idx_col,col in enumerate(row):
          if col == "1":
               tile_x = idx_col * tile_width
               tile_y = idx_row * tile_height
               tile = Tile(tile_x,tile_y,stone)
               all_sprites.add(tile)
               tiles.add(tile)
          if col == "2":
              small_enime = SMALL_Enemy(idx_col * 146 ,idx_row*175)
              all_sprites.add(small_enime)
              enime.add(small_enime)
          if col == "3":
              player_x = screen_width //2
              player_y = idx_row*  167
              player = Player(player_x,player_y,image_animation1,image_jump,image_animation1,image_animation2,1)
              all_sprites.add(player)      
              players.add(player)
          if col == "4":
              weapon_x = idx_col * 146
              weapon_y = idx_row * 146
              weapon = Weapon(weapon_x,weapon_y)
              all_sprites.add(weapon)
              weapons.add(weapon)
          if col == "5": 
              middle_enemy = MIDDLE_Enemy(idx_col*146,idx_row*167)                    
              all_sprites.add(middle_enemy)
              enime_middle.add(middle_enemy)
          if col == "6": 
              midcate = Medcate(idx_col*146,idx_row*167)                    
              all_sprites.add(midcate) 
              midcates.add(midcate)
          if col == "8":
              lava = Lava(idx_col* 142,idx_row*140)
              all_sprites.add(lava)
              lavas.add(lava)
          if col == "9":
              ammo = Ammo(idx_col* 146,idx_row*167)
              all_sprites.add(ammo)
              ammos.add(ammo)
          if col == ".":
               platform_x = Platform(idx_col* 146,idx_row*146,1,0)
               all_sprites.add(platform_x)
               platforms_x.add(platform_x)
          if col == ",":
               platform_x = Platform(idx_col* 146,idx_row*146,0,1)
               all_sprites.add(platform_x)
               platforms_x.add(platform_x)
          if col == "*": 
              big_enemy = Big_Enemy(idx_col*146,idx_row*180)                    
              all_sprites.add(big_enemy)
              enime_big.add(big_enemy)
          if col == "!": 
              roocket = rocket(idx_col*140,idx_row*105)                    
              all_sprites.add(roocket)
              rockets.add(roocket)
          if col == "(":
              weapon_x = idx_col * 146
              weapon_y = idx_row * 146
              weapon2 = Weapon2(weapon_x,weapon_y)
              all_sprites.add(weapon2)
              riffles.add(weapon2)

              
              
font = pygame.font.Font("images/Old School Adventures.ttf",32)

def text_font(font,text,text_col,x,y):
    text_font = font.render(text,True,text_col)
    screen.blit(text_font,(x,y))

gravity = 0.5 
bullets = []
game_started = True
game_poused = False
game_over = False
lava = False



run = True
while run:
        clock.tick(fps)
        screen.blit(intro,(0,0))

       



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if finish == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_poused = True
                        game_started = False
                    

        if game_started == False:
            for x in range(8):
                speed = 1
                for i  in bg_images:
                    screen.blit(i,((bg_width*x)- player.scroll * speed,0))
                    speed += 0.5
                for i  in bg_image:
                    screen.blit(i,((2000*x)- player.scroll * speed,0))
                    speed += 0.5
                for i  in planet_images:
                    screen.blit(i,((bg_width*x + 1000)- player.scroll * speed  ,random_planets))
                    speed += 0.5

                


            if player.shootloop > 0:
                player.shootloop += 1
            if player.shootloop > 3:
                player.shootloop = 0
        
            collisions_x = pygame.sprite.spritecollide(player, tiles,False)
            for tile in collisions_x:
                if player.velocity_x > 0:
                    for sprite in all_sprites:
                        sprite.rect.x += 5
                    player.rect.right = tile.rect.left
                    player.velocity_x = 0
                    player.scroll -= 1
                elif player.velocity_x < 0:
                    for sprite in all_sprites:
                        sprite.rect.x -= 5 
                    
                    player.rect.left = tile.rect.right
                    player.velocity_x = 0
                    player.scroll += 1
                    

            
            player.rect.y += player.velocity_y
            player.velocity_y += gravity

            collisions_y = pygame.sprite.spritecollide(player, tiles, False)
            for tile in collisions_y:
                if player.velocity_y > 0:
                    player.rect.bottom  = tile.rect.top 
                    player.velocity_y = 0
                    player.jump = False
                elif player.velocity_y < 0:
                    player.rect.top = tile.rect.bottom
                    player.velocity_y = 0

            collisions_enemy_y = pygame.sprite.spritecollide(player,enime,False)   
            for enmie in collisions_enemy_y:
                if player.velocity_y > 0:
                    collisions_enemy = pygame.sprite.spritecollide(player,enime,True)
                if not player.velocity_y > 0:
                    player.health -= 10
                    if player.health == 0:
                        game_over = True



        
            if pygame.sprite.spritecollide(player,enime,False) and hide_frames > 10:
               
                hide_frames = 0


            
            if pygame.sprite.spritecollide(player,weapons,False):
                player.rifflerr = False
                player.handgun = True
                if player.handgun:
                    if player.right:
                        weapon.rect.x = player.rect.x 
                        weapon.rect.y = player.rect.y + 15
                        weapon.right = True
                        weapon.left = False
                    if player.left:
                        weapon.left = True
                        weapon.right = False
                        weapon.rect.x = player.rect.x 
                        weapon.rect.y = player.rect.y + 15
            

            if pygame.sprite.spritecollide(player,riffles,False):
                player.handgun = False
                player.rifflerr = True
                if player.rifflerr:
                    if player.right:
                        weapon2.rect.x = player.rect.x 
                        weapon2.rect.y = player.rect.y + 15
                        weapon2.right = True
                        weapon2.left = False
                    if player.left:
                        weapon2.left = True
                        weapon2.right = False
                        weapon2.rect.x = player.rect.x 
                        weapon2.rect.y = player.rect.y + 15            



                
                

            collisions_enemy_with_tile_x = pygame.sprite.spritecollide(middle_enemy,tiles,False)
            for tile in collisions_enemy_with_tile_x:
                if middle_enemy.velocity_x > 0:
                    middle_enemy.rect.right = tile.rect.left
                    middle_enemy.velocity_x = 0
                elif middle_enemy.velocity_x < 0:
                    middle_enemy.rect.left = tile.rect.right
                    middle_enemy.velocity_x = 0

            collisions_enemy_with_tile_y = pygame.sprite.spritecollide(middle_enemy,tiles,False)
            for tile in collisions_enemy_with_tile_y:
                if middle_enemy.velocity_y > 0:
                    middle_enemy.rect.bottom = tile.rect.top
                    middle_enemy.velocity_y = 0
                elif middle_enemy.velocity_y < 0:
                    middle_enemy.rect.top = tile.rect.bottom
                    middle_enemy.velocity_y = 0

            hide_frames += 1

            collisions_enemy_with_tile_y = pygame.sprite.spritecollide(big_enemy,tiles,False)
            for tile in collisions_enemy_with_tile_y:
                if big_enemy.velocity_y > 0:
                    big_enemy.rect.bottom = tile.rect.top
                    big_enemy.velocity_y = 0
                elif big_enemy.velocity_y < 0:
                    big_enemy.rect.top = tile.rect.bottom
                    big_enemy.velocity_y = 0



            if pygame.Rect.colliderect(player.rect,middle_enemy.rectangle):
                middle_enemy.shock = True
            if not pygame.Rect.colliderect(player.rect,middle_enemy.rectangle):
                middle_enemy.shock = False

            if pygame.Rect.colliderect(player.rect,big_enemy.rectangle):
                big_enemy.shock = True
            if not pygame.Rect.colliderect(player.rect,big_enemy.rectangle):
                big_enemy.shock = False

            if pygame.sprite.spritecollide(player,rockets,False):
                finish = True
    
            
            for bullet in player.bullets:
                bullet.draw(screen)
                if pygame.sprite.spritecollide(bullet,tiles,False):
                    player.bullets.remove(bullet)


                collision_bullet_enemy_1 = pygame.sprite.spritecollide(bullet,enime_middle,False)
                for bullets in collision_bullet_enemy_1:
                    
                    blood = Blood(middle_enemy.rect.x,middle_enemy.rect.y)

                    middle_enemy.hit()
                    hide_frames = 0
                    player.bullets.remove(bullet)
                    
                    if middle_enemy.health_x == 0:
                        blood.enemy_death = True 
                        if blood.enemy_death:
                            if pygame.sprite.spritecollide(bullet,enime_middle,True):
                                blood.draw(screen,middle_enemy)
                                blood.move()

                if pygame.sprite.spritecollide(bullet,enime_big,False) and hide_frames > 50:
                    blood = Blood(middle_enemy.rect.x,middle_enemy.rect.y)
                    big_enemy.hit()
                    hide_frames = 0
                    player.bullets.remove(bullet)
                    if big_enemy.health_x == 0:
                        
                        blood.enemy_death = True 
                        if blood.enemy_death:
                            if pygame.sprite.spritecollide(bullet,enime_big,True):
                                blood.draw(screen,middle_enemy)
                                blood.move()

                        
            for bullet in big_enemy.bullets:
                bullet.draw(screen)
                if pygame.sprite.spritecollide(bullet,tiles,False):
                    big_enemy.bullets.remove(bullet)
                if pygame.sprite.spritecollide(bullet,players,False):
                    big_enemy.bullets.remove(bullet)
                    player.health -= 5
                    if player.health == 0:
                        game_over = True
                        player.is_alive = False




                        
            if pygame.sprite.spritecollide(player,midcates,False):
                pygame.sprite.spritecollide(player,midcates,True)
                player.health += 25

            if pygame.sprite.spritecollide(player,lavas,False):
                player.health -= 50
                if player.health <= 0:
                    game_over = True
                    player.is_alive = False


            if pygame.sprite.spritecollide(player,enime_middle,False) and hide_frames > 5:    
                player.health -= 10
                hide_frames = 0
                if player.health == 0:
                    game_over = True
                    player.is_alive = False
            
    

            if pygame.sprite.spritecollide(player,ammos,False):
                player.ammo += 5
                pygame.sprite.spritecollide(player,ammos,True)

                    
            collisions_y_plat = pygame.sprite.spritecollide(player, platforms_x, False)
            for platform in collisions_y_plat:
                if player.velocity_y > 0:
                    player.rect.bottom = platform.rect.top 
                    player.rect.x += platform.move_direction
                    player.velocity_y = 0
                    player.jump = False                        
                elif player.velocity_y < 0:
                    player.rect.top = platform.rect.bottom 
                    player.velocity_y = 0


                
            all_sprites.draw(screen)
            text_font(font,f"X{player.ammo}",(255,255,255),950,50)
            screen.blit(volda,(900,50))
            weapon2.move(screen,player)
            weapon.move(screen,player)
            player.draw(screen,all_sprites,bullets,players)
            platform_x.update(player,screen,all_sprites)
            enime_middle.update(player,screen,all_sprites)
            enime_big.update(player,screen,all_sprites)
            all_sprites.update(player,screen,all_sprites)

        if finish:
            screen.blit(end,(0,0))
            text_font(font,"Good Job",(255,255,255),550,250)
            text_font(font,"You Return To Earth",(255,255,255),550,450)
            if quit.draw(screen):
                pygame.quit() 

        if game_poused == True:
            screen.blit(poused,(0,0))
            if resume.draw(screen):
                game_started = False
                game_poused = False

            if quit.draw(screen):
                pygame.quit()

        if game_started == True:
            if start.draw(screen):
                game_started = False

            if quit.draw(screen):
                pygame.quit()


        if game_over == True:
            screen.fill((0,0,0))
            screen.blit(dead_img,(200,250))
            text_font(font,"You Die",(255,255,255),400,250)
            if quit.draw(screen):
                pygame.quit()

    
        pygame.display.update()

