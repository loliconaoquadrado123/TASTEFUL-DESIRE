import pygame
from pygame.locals import *
import random
import os
import sys
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)
SIZE=(640,600)
screen = pygame.display.set_mode(SIZE)
rect=Rect(200,500,32,32)
fontsList = pygame.font.get_fonts()
print (fontsList)
speed=1000
pygame.init() 
a=True
playerSpeed=10

def drawScore():
    TEXTCOLOUR = (200, 100, 0)
    fontObj = pygame.font.SysFont("arialblack", 50)
    textSufaceObj = fontObj.render(str(pygame.time.get_ticks()), True, TEXTCOLOUR, None)
    screen.blit(textSufaceObj, (50, 50))
def restart():
    #os.startfile(sys.argv[0])
    #sys.exit()
    os.startfile(__file__)
    sys.exit()
def lose():
    global a
    while a:
        BACKGROUND = (255, 255, 255)
        TEXTCOLOUR = (200, 100, 0)
        fontObj = pygame.font.SysFont("arialblack", 50)
        textSufaceObj = fontObj.render('you lose!', True, TEXTCOLOUR, None)
        screen.fill(BACKGROUND)
        screen.blit(textSufaceObj, (100, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_e:
                    a=False
                    restart()
            if event.type == QUIT:
                pygame.quit()
                
    
       
upperbound=-100
objs=[]

def barrier():
    
    holepos=random.randrange(0,640)
    objs.append(Rect(0,upperbound,holepos,50))
    objs.append(Rect(holepos+100,upperbound,640-holepos-100,50))
barrier()
#level

pygame.time.set_timer(pygame.USEREVENT, speed)
clock = pygame.time.Clock()
#loguca
running=True
while running:
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rect=rect.move(-playerSpeed,0)
    if keys[pygame.K_RIGHT]:
        rect=rect.move(playerSpeed,0)
    if keys[pygame.K_UP]:
        rect=rect.move(0,-playerSpeed)
    if keys[pygame.K_DOWN]:
        rect=rect.move(0,playerSpeed)
        
    for i in range(len(objs)):

        collide = pygame.Rect.colliderect(rect, objs[i])
        if collide:
            lose()
            a=True
            
    screen.fill(GRAY)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type==USEREVENT:
            objs=[]
            barrier()
            
    for i in range(len(objs)):
        
        pygame.draw.rect(screen,RED,objs[i],0)  
        objs[i]=objs[i].move(0,10)
        if objs[-1].top==600:
            objs.pop()
    drawScore()
    pygame.draw.rect(screen,GREEN,rect,0)
    pygame.display.update()
    clock.tick(60)
    speed=speed-1
    
pygame.quit()