import random
import time
from pygame import *

class GameSprite1(sprite.Sprite):
    def __init__(self, player_image, player_x1, player_y1, player_speed1,x,y,a):
        super().__init__()
        self.mod = a
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed1 = player_speed1
        self.rect = self.image.get_rect()
        self.rect.x = player_x1
        self.rect.y = player_y1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite1):
    def move_sprite1(self):
        if self.mod == 1:
            key_pressed = key.get_pressed()
            if key_pressed[K_s] and self.rect.y < 800:
                self.rect.y += self.speed1
            if key_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed1
        if self.mod == 2:
            key_pressed = key.get_pressed()
            if key_pressed[K_DOWN] and self.rect.y < 800:
                self.rect.y += self.speed1
            if key_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed1

window = display.set_mode((1400,1000))
display.set_caption("Пинг Понг")
background = transform.scale(image.load("background.jpg"), (1400,1000))
player1_sprite = Player_1('pngwing.com (1).png',0,0,3,50,200,1)
player2_sprite = Player_1('pngwing.com (1).png',1350,0,3,50,200,2)



game = True

while game == True:
    window.blit(background,(0,0))
    player1_sprite.reset()
    player1_sprite.move_sprite1()
    player2_sprite.reset()
    player2_sprite.move_sprite1()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
