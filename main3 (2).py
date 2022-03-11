import pygame
import os
import time
import random
pygame.font.init()
#Fenstergröße
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Attack")

#Hintergrund
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","bg_02_h.png")),(WIDTH, HEIGHT))

#Gegnerische Raumschiffe Grün
BlauesRaumschiff1 = pygame.image.load(os.path.join("assets","PNG","Enemies","enemyBlue1.png"))
GruenesRaumschiff2 = pygame.image.load(os.path.join("assets","PNG","Enemies","enemyGreen2.png"))
RotesRaumschiff3 = pygame.image.load(os.path.join("assets","PNG","Enemies","enemyRed3.png"))

#Raumschiff des Spielers
SpielerRaumschiff = pygame.image.load(os.path.join("assets","PNG","playerShip3_orange.png"))

#Schusspartikel
RoterLaser = pygame.image.load(os.path.join("assets","PNG","Lasers","laserRed04.png"))
BlauerLaser = pygame.image.load(os.path.join("assets","PNG","Lasers","laserBlue04.png"))
GruenerLaser = pygame.image.load(os.path.join("assets","PNG","Lasers","laserGreen12.png"))

class Laser:
    def _init_(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    def move(self, vel):
        selfy += vel
    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    def collision(self,obj):
        return collide(self, obj)
    


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.RoterLaser,(self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter >0: 
            self.cool_down_counter += 1

    def shoot (self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = SpielerRaumschiff
        self.laser_img = RoterLaser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    COLOR_MAP = {
                "red": (RotesRaumschiff3, RoterLaser),
                "green": (GruenesRaumschiff2, GruenerLaser),
                "blue": (BlauesRaumschiff1, BlauerLaser)
                }
    def __init__ (self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y += vel

def collide (obj1,obj2):
    offset_x = obj2.x - obj1.x
    offset_y = onj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x, offset_y)) != None

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans",30)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 4

    player = Player(350, 500)


    clock = pygame.time.Clock()

    lost= False

    def redraw_window():
            WIN.blit(BG,(0,0))
            #draw text
            lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
            level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

            WIN.blit(lives_label, (10,10))
            WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

            for enemy in enemies:
                enemy.draw(WIN)

            player.draw(WIN)
            

            pygame.display.update()
    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Bewegung durch WASD und Spieler kann nicht aus dem Bild verschwinden
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

        redraw_window()

    main()
