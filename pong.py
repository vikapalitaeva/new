#создай игру "Лабиринт"!
from pygame import *
from random import*
FPS = 60
clock = time.Clock()
display.set_caption('Пинг понг')
window = display.set_mode((700,500))

kartinka = transform.scale(image.load('phon.jpg'), (700,500))

keys_pressed = key.get_pressed()
x1,x2,y1,y2 = 15,15,30,30 
#speed = 3
class Gamesprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def update(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_d]: 
            self.rect.x += self.speed 
        if keys_pressed[K_a]: 
            self.rect.x -= self.speed
    
class Ball(Gamesprite):
    def update(self):
        global lost
        self.rect.y += randint(1,3)
        if  self.rect.y >=  500:
            self.rect.y = 0
            lost +=1
            self.rect.x = randint(0,700)
    
          
  
finish = False
rocket1 = Player('rocket1.png',90,430,8 ,70,65)
rocket1 = Player('rocket2.png',85,425,7 ,65,60)
ball = Ball('ball.png',30,70,380,7 ,30)
font = font.Font(None,45)


game = True
while game:
    clock.tick(FPS)
    window.blit(kartinka,(0,0))
    if e.type == QUIT:
        quit()
    elif  e.type == KEYDOWN:
        if e.key == K_SPACE:
            pass
               

    '''if kills >=10:
        finish = True
    if lost >=3:
        finish = True
    if finish == True:
        if lost >=3:
            Lose = font.render('LOSE',True,(255,255,255))
            window.blit(Lose, (300, 300))
        if kills >=10:
            Win = font.render('WIN',True,(255,255,255))
            window.blit(Win, (300, 300))
    else:
        window.blit(kartinka,(0,0))



        win = font.render('Счёт:'+ str(kills),True,(255,255,255))
        lose = font.render(
        'Пропущено:' + str(lost),True,(255,255,255))'''
    rocket1.update()
    rocket1.reset()
    rocket2.update()
    rocket2.reset()
    ball.update()
    ball.reset()
    window.blit(win,(20,0))
    window.blit(lose,(20,30))
    display.update()

