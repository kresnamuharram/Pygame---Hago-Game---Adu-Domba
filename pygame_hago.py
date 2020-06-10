import pygame, sys, random as rand
pygame.init()
pygame.font.init()
pygame.font.get_fonts()
clock = pygame.time.Clock()

########################################
#function on main
########################################
def stage_field():
    pygame.draw.rect(screen, (0,240,0), jalur0, 0)
    pygame.draw.rect(screen, black, jalur0, 1)
    pygame.draw.rect(screen, (0,240,0), jalur1, 0)
    pygame.draw.rect(screen, black, jalur1, 1)
    pygame.draw.rect(screen, (0,240,0), jalur2, 0)
    pygame.draw.rect(screen, black, jalur2, 1)
    pygame.draw.rect(screen, (0,240,0), jalur3, 0)
    pygame.draw.rect(screen, black, jalur3, 1)
    pygame.draw.rect(screen, (0,240,0), jalur4, 0)
    pygame.draw.rect(screen, black, jalur4, 1)
def circle_guide():
    pygame.draw.circle(screen,white,(850,200),40)
    screen.blit(pion,(830,160))
    pygame.draw.circle(screen,white,(850,300),40)
    screen.blit(peluncur,(830,260))
    pygame.draw.circle(screen,white,(850,400),40)
    screen.blit(king,(830,360))
    text_pion = font.render("1",1,black)
    text_peluncur = font.render("2",1,black)
    text_king = font.render("3",1,black)
    screen.blit(text_pion,(850,240))
    screen.blit(text_peluncur,(850,340))
    screen.blit(text_king,(850,440))
#draw view
def draw_view():
    stage_field()    
    circle_guide()
    for player in jalur0_array:
        player.draw(screen)
    for player in jalur1_array:
        player.draw(screen)
    for player in jalur2_array:
        player.draw(screen)
    for player in jalur3_array:
        player.draw(screen)
    for player in jalur3_array:
        player.draw(screen)
    for player in jalur4_array:
        player.draw(screen)
    
    #draw enemy
    for enemy in jalur0_array_enemy:
        enemy.draw(screen)
    for enemy in jalur1_array_enemy:
        enemy.draw(screen)
    for enemy in jalur2_array_enemy:
        enemy.draw(screen)
    for enemy in jalur3_array_enemy:
        enemy.draw(screen)
    for enemy in jalur4_array_enemy:
        enemy.draw(screen)
    
    #from random for display which turn now
    if player_random == 0:
        screen.blit(pion,(100,100))
    if player_random == 1:
        screen.blit(peluncur,(100,100))
    if player_random == 2:
        screen.blit(king,(100,100))
    #draw last
    Kresna.draw(screen)
    Lala.draw(screen)
    pygame.display.update()

########################################
#Funcion each path with array
########################################
#player func array
def player_array0():
    global jalur0_trek,variabel0_jalur1_pemain

    for player in jalur0_array:
        if player.y <= 90:
            jalur0_array.remove(player)
            jalur0_trek = False
        if player.y > 490:
            jalur0_array.remove(player)

    if len(jalur0_array) > 0:
        jalur0_trek = True

    if jalur0_trek:
        for player in jalur0_array:
            print(player.speed," speed player ")
            for player_new in jalur0_array:
                if player_new.rect[1]==player.rect[1]:
                    continue
                elif 0> player_new.rect[1]-player.rect[1] > (-70):
                    if not player.player_collide_player:
                        player_new.power += player.power
                        player.speed = player_new.power
                        player.player_collide_player = True
                        if player.speed >4:
                            player.speed = 4
            if len(jalur0_array_enemy) == 0:
                player.y -= player.speed
            else: 
                for enemy in jalur0_array_enemy:
                    if player.rect[1]-enemy.rect[1] <=70:
                        if player.power-enemy.power > 0:
                            player.speed = player.power-enemy.power
                            player.y -= player.speed
                        elif player.power-enemy.power < 0:
                            player.speed = enemy.power-player.power
                            player.y += player.speed
                        elif player.power-enemy.power == 0:
                            player.speed = 0
                            player.y -= player.speed
                    else:
                        player.y -= player.speed
def player_array1():
    global jalur1_trek

    for player in jalur1_array:
        if player.y <= 90:
            jalur1_array.remove(player)
            jalur1_trek = False

    if len(jalur1_array) > 0:
        jalur1_trek = True
        
    if jalur1_trek:
        for player in jalur1_array:
            player.y -= 4  
def player_array2():
    global jalur2_trek

    for player in jalur2_array:
        if player.y <= 90:
            jalur2_array.remove(player)
            jalur2_trek = False

    if len(jalur2_array) > 0:
        jalur2_trek = True
        
    if jalur2_trek:
        for player in jalur2_array:
            player.y -= 4 
def player_array3():
    global jalur3_trek

    for player in jalur3_array:
        if player.y <= 90:
            jalur3_array.remove(player)
            jalur3_trek = False

    if len(jalur3_array) > 0:
        jalur3_trek = True
        
    if jalur3_trek:
        for player in jalur3_array:
            player.y -= 4  
def player_array4():
    global jalur4_trek

    for player in jalur4_array:
        if player.y <= 90:
            jalur4_array.remove(player)
            jalur4_trek = False

    if len(jalur4_array) > 0:
        jalur4_trek = True
        
    if jalur4_trek:
        for player in jalur4_array:
            player.y -= 4  
#enemy func array
def enemy_array0():
    global jalur0_trek_enemy
    for enemy in jalur0_array_enemy:
        if enemy.y >= 490:
            jalur0_array_enemy.remove(enemy)
            jalur0_trek_enemy = False
    if len(jalur0_array_enemy) > 0:
        jalur0_trek_enemy = True       
    if jalur0_trek_enemy:
        for enemy in jalur0_array_enemy:
            for enemy_new in jalur0_array_enemy:
                if enemy_new.rect[1]==enemy.rect[1]:
                    continue
                elif 0 > enemy_new.rect[1]-enemy.rect[1] > (-70):
                    if not enemy.enemy_collide_enemy:
                        enemy_new.power += enemy.power
                        enemy.speed =enemy_new.power
                        enemy.enemy_collide_enemy = True
                        if enemy.speed > 4:
                            enemy.speed = 4
            if len(jalur0_array) == 0:
                enemy.y += 4
            else: 
                for player in jalur0_array:
                    if player.rect[1]-enemy.rect[1] <=70:
                        if player.power-enemy.power > 0:
                            enemy.speed = player.power-enemy.power
                            enemy.y -= enemy.speed
                            print(enemy.speed, " player kuat")
                        elif player.power-enemy.power < 0:
                            enemy.speed = enemy.power-player.power
                            enemy.y += enemy.speed
                        elif player.power-enemy.power == 0:
                            enemy.speed = 0
                            enemy.y += enemy.speed
                        
                    else:
                        enemy.y += 4
def enemy_array1():
    global jalur1_trek_enemy
    for enemy in jalur1_array_enemy:
        if enemy.y >= 490:
            jalur1_array_enemy.remove(enemy)
            jalur1_trek_enemy = False
    if len(jalur1_array_enemy) > 0:
        jalur1_trek_enemy = True       
    if jalur1_trek_enemy:
        for enemy in jalur1_array_enemy:
            enemy.y += 4 
def enemy_array2():
    global jalur2_trek_enemy
    for enemy in jalur2_array_enemy:
        if enemy.y >= 490:
            jalur2_array_enemy.remove(enemy)
            jalur2_trek_enemy = False
    if len(jalur2_array_enemy) > 0:
        jalur2_trek_enemy = True       
    if jalur2_trek_enemy:
        for enemy in jalur2_array_enemy:
            enemy.y += 4
def enemy_array3():
    global jalur3_trek_enemy
    for enemy in jalur3_array_enemy:
        if enemy.y >= 490:
            jalur3_array_enemy.remove(enemy)
            jalur3_trek_enemy = False
    if len(jalur3_array_enemy) > 0:
        jalur3_trek_enemy = True       
    if jalur3_trek_enemy:
        for enemy in jalur3_array_enemy:
            enemy.y += 1  
def enemy_array4():
    global jalur4_trek_enemy
    for enemy in jalur4_array_enemy:
        if enemy.y >= 490:
            jalur4_array_enemy.remove(enemy)
            jalur4_trek_enemy = False
    if len(jalur4_array_enemy) > 0:
        jalur4_trek_enemy = True       
    if jalur4_trek_enemy:
        for enemy in jalur4_array_enemy:
            enemy.y += 4  

#########################################
#Classes
#########################################
#class Player
class Player:
    count_keys = 0
    health_bar_red = [300,490,500,90]
    health_bar_green = [300,490,500,90]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,screen):
        health_bar_red = [300,490,500,90]
        health_bar_green = [300,490,500,90]
        pygame.draw.rect(screen, (255,0,0), health_bar_red, 0)
        pygame.draw.rect(screen, (0,240,0), health_bar_green, 0)
        pygame.draw.rect(screen, black, health_bar_green, 1)
        health_bar_status = font.render("health bar status",1,black)
        screen.blit(health_bar_status,(health_bar_green[0]+health_bar_green[2]/2-health_bar_status.get_width()/2,health_bar_green[1]+health_bar_green[3]/2-health_bar_status.get_height()/2))
class Player_pion(Player):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 1
        self.attack = 4
        self.rect = [self.x,self.y+10,self.width,self.height-10]
        self.player_collide_player = False
        self.speed = 4
    def draw(self,screen):
        screen.blit(pion,(self.x,self.y))
        self.rect = [self.x,self.y+10,self.width,self.height-10]
class Player_peluncur(Player):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 2
        self.attack = 2
        self.rect = [self.x,self.y+10,self.width,self.height-10]
        self.player_collide_player = False
        self.speed = 4
    def draw(self,screen):
        screen.blit(peluncur,(self.x,self.y))
        self.rect = [self.x,self.y+10,self.width,self.height-10]
class Player_king(Player):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 4
        self.attack = 1
        self.rect = [self.x,self.y,self.width,self.height]
        self.player_collide_player = False
        self.speed = 4
    def draw(self,screen):
        screen.blit(king,(self.x,self.y))
        self.rect = [self.x,self.y,self.width,self.height]
#class Enemy
class Enemy:
    count_keys = 0
    health_bar_red = [300,490,500,90]
    health_bar_green = [300,490,500,90]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self,screen):
        health_bar_red = [300,0,500,90]
        health_bar_green = [300,0,500,90]
        pygame.draw.rect(screen, (255,0,0), health_bar_red, 0)
        pygame.draw.rect(screen, (0,240,0), health_bar_green, 0)
        pygame.draw.rect(screen, black, health_bar_green, 1)
        health_bar_status = font.render("health bar status",1,black)
        screen.blit(health_bar_status,(health_bar_green[0]+health_bar_green[2]/2-health_bar_status.get_width()/2,health_bar_green[1]+health_bar_green[3]/2-health_bar_status.get_height()/2))
class Enemy_pion(Enemy):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 1
        self.attack = 4
        self.rect = [self.x,self.y+10,self.width,self.height-10]
        self.speed = 4
        self.enemy_collide_enemy = False
    def draw(self,screen):
        screen.blit(pion,(self.x,self.y))
        self.rect = [self.x,self.y+10,self.width,self.height-10]
        self.speed = 4
class Enemy_peluncur(Enemy):   
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 2
        self.attack = 2
        self.rect = [self.x,self.y+10,self.width,self.height-10]
        self.speed = 4
        self.enemy_collide_enemy = False
    def draw(self,screen):
        screen.blit(peluncur,(self.x,self.y))
        self.rect = [self.x,self.y+10,self.width,self.height-10]
class Enemy_king(Enemy):
    def __init__ (self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.power = 4
        self.attack = 1
        self.rect = [self.x,self.y,self.width,self.height]
        self.speed = 4
        self.enemy_collide_enemy = False
    def draw(self,screen):
        screen.blit(king,(self.x,self.y))
        self.rect = [self.x,self.y,self.width,self.height]


########################################
#Variable
########################################
#screen
screen_width = 900
screen_height = 580
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("coba2")
#load
pion = pygame.image.load('Pion.png')
king = pygame.image.load('Raja.png')
peluncur = pygame.image.load('Peluncur.png')
#color
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
font = pygame.font.SysFont('freesansbold.tff', 32)
#layout
jalur0 = [300,90,100,400]
jalur1 = [400,90,100,400]
jalur2 = [500,90,100,400]
jalur3 = [600,90,100,400]
jalur4 = [700,90,100,400]
penampil_player = 64
penampil_enemy = 64
######################################### array ########################################
#array pemain
jalur0_array = []
jalur1_array = []
jalur2_array = []
jalur3_array = []
jalur4_array = []
jalur0_trek  = False
jalur1_trek = False
jalur2_trek = False
jalur3_trek = False
jalur4_trek = False
#variabel 0 untuk looping pada array pemain
variabel0_jalur1_pemain = 0
variabel0_jalur2_pemain = 0
variabel0_jalur3_pemain = 0
variabel0_jalur4_pemain = 0
variabel0_jalur5_pemain = 0
#array enemy
jalur0_array_enemy = []
jalur1_array_enemy = []
jalur2_array_enemy = []
jalur3_array_enemy = []
jalur4_array_enemy = []
jalur0_trek_enemy  = False
jalur1_trek_enemy = False
jalur2_trek_enemy = False
jalur3_trek_enemy = False
jalur4_trek_enemy = False
#variabel 0 untuk looping pada array enemy
variabel0_jalur1_enemy = 0
variabel0_jalur2_enemy = 0
variabel0_jalur3_enemy = 0
variabel0_jalur4_enemy = 0
variabel0_jalur5_enemy = 0


#variable
enemy_count = 0
time_waiting = 0
player_random = rand.randrange(0,3)
enemy_random = rand.randrange(0,5)
enemy_random_pion = rand.randrange(0,3)
Kresna = Player(0,0,0,0)
Lala = Enemy(0,0,0,0)

#main loop
while True:
    #variable di main loop
    keys = pygame.key.get_pressed()
    screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#comp act
    enemy_count += 1
    if enemy_count == 10 or enemy_count == 40:
        if enemy_random == 0:
            if len(jalur0_array_enemy) >= 0:
                if enemy_random_pion == 0:
                    jalur0_array_enemy.append(Enemy_pion(jalur0[0],26,64,64))
                if enemy_random_pion == 1:
                    jalur0_array_enemy.append(Enemy_peluncur(jalur0[0],26,64,64))
                if enemy_random_pion == 2:
                    jalur0_array_enemy.append(Enemy_king(jalur0[0],26,64,64))
        if enemy_random == 1:
            if len(jalur1_array_enemy) >= 0:
                if enemy_random_pion == 0:
                    jalur1_array_enemy.append(Enemy_pion(jalur1[0],26,64,64))
                if enemy_random_pion == 1:
                    jalur1_array_enemy.append(Enemy_peluncur(jalur1[0],26,64,64))
                if enemy_random_pion == 2:
                    jalur1_array_enemy.append(Enemy_king(jalur1[0],26,64,64))
        if enemy_random == 2:
            if len(jalur2_array_enemy) >= 0:
                if enemy_random_pion == 0:
                    jalur2_array_enemy.append(Enemy_pion(jalur2[0],26,64,64))
                if enemy_random_pion == 1:
                    jalur2_array_enemy.append(Enemy_peluncur(jalur2[0],26,64,64))
                if enemy_random_pion == 2:
                    jalur2_array_enemy.append(Enemy_king(jalur2[0],26,64,64))
        if enemy_random == 3:
            if len(jalur3_array_enemy) >= 0:
                if enemy_random_pion == 0:
                    jalur3_array_enemy.append(Enemy_pion(jalur3[0],26,64,64))
                if enemy_random_pion == 1:
                    jalur3_array_enemy.append(Enemy_peluncur(jalur3[0],26,64,64))
                if enemy_random_pion == 2:
                    jalur3_array_enemy.append(Enemy_king(jalur3[0],26,64,64))
        if enemy_random == 4:
            if len(jalur4_array_enemy) >= 0:
                if enemy_random_pion == 0:
                    jalur4_array_enemy.append(Enemy_pion(jalur4[0],26,64,64))
                if enemy_random_pion == 1:
                    jalur4_array_enemy.append(Enemy_peluncur(jalur4[0],26,64,64))
                if enemy_random_pion == 2:
                    jalur4_array_enemy.append(Enemy_king(jalur4[0],26,64,64))
    if enemy_count == 41 or enemy_count == 10:
        enemy_count = 11
        enemy_random = rand.randrange(0,5)
        enemy_random_pion = rand.randrange(0,3)
    enemy_array0()
    enemy_array1()
    enemy_array2()
    enemy_array3()
    enemy_array4()

#key to act
    if keys[pygame.K_0] and Player.count_keys == 0:
        time_waiting = pygame.time.get_ticks()
        jalur0_trek = True
        if player_random == 0:
            jalur0_array.append(Player_pion(jalur0[0], 490, 64, 64))
        elif player_random == 1:
            jalur0_array.append(Player_peluncur(jalur0[0], 490, 64, 64))
        elif player_random == 2:
            jalur0_array.append(Player_king(jalur0[0], 490, 64, 64))
        Player.count_keys += 1
    if keys[pygame.K_1] and Player.count_keys == 0:
        time_waiting = pygame.time.get_ticks()
        jalur1_trek = True
        if player_random == 0:
            jalur1_array.append(Player_pion(jalur1[0], 490, 64, 64))
        elif player_random == 1:
            jalur1_array.append(Player_peluncur(jalur1[0], 490, 64, 64))
        elif player_random == 2:
            jalur1_array.append(Player_king(jalur1[0], 490, 64, 64))
        Player.count_keys += 1
    if keys[pygame.K_2] and Player.count_keys == 0:
        time_waiting = pygame.time.get_ticks()
        jalur2_trek = True
        if player_random == 0:
            jalur2_array.append(Player_pion(jalur2[0], 490, 64, 64))
        elif player_random == 1:
            jalur2_array.append(Player_peluncur(jalur2[0], 490, 64, 64))
        elif player_random == 2:
            jalur2_array.append(Player_king(jalur2[0], 490, 64, 64))
        Player.count_keys += 1
    if keys[pygame.K_3] and Player.count_keys == 0:
        time_waiting = pygame.time.get_ticks()
        jalur3_trek = True
        if player_random == 0:
            jalur3_array.append(Player_pion(jalur3[0], 490, 64, 64))
        elif player_random == 1:
            jalur3_array.append(Player_peluncur(jalur3[0], 490, 64, 64))
        elif player_random == 2:
            jalur3_array.append(Player_king(jalur3[0], 490, 64, 64))
        Player.count_keys += 1
    if keys[pygame.K_4] and Player.count_keys == 0:
        time_waiting = pygame.time.get_ticks()
        jalur4_trek = True
        if player_random == 0:
            jalur4_array.append(Player_pion(jalur4[0], 490, 64, 64))
        elif player_random == 1:
            jalur4_array.append(Player_peluncur(jalur4[0], 490, 64, 64))
        elif player_random == 2:
            jalur4_array.append(Player_king(jalur4[0], 490, 64, 64))
        Player.count_keys += 1
    player_array0() 
    player_array1() 
    player_array2() 
    player_array3() 
    player_array4() 

#start game
    if Player.count_keys:
        waiting_progress = pygame.time.get_ticks()
        if waiting_progress - time_waiting <= 1000:
            detik1 = font.render("3", 1, black)   
            screen.blit(detik1,(0,0))
        elif waiting_progress - time_waiting <= 2000:
            detik2 = font.render("2" ,1, black) 
            screen.blit(detik2,(00,00))  
        elif waiting_progress - time_waiting <= 3000:
            detik3 = font.render("1",1 , black) 
            screen.blit(detik3,(00,00))  
        Player.count_keys += 1
        if Player.count_keys >= 30:
            Player.count_keys = 0
            player_random = rand.randrange(0,3)

#logic game

#view
    draw_view()
    pygame.display.update()

    clock.tick(10)
