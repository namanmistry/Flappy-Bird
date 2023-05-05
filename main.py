import pygame
import random
from pygame import mixer        
import math
pygame.init()
#loading all the images at once

ICON=pygame.image.load('flappy-bird-icon-10.jpg')
BG=pygame.image.load('game-background-png-5.png')
BASE=pygame.image.load('base.png')
PLAYER=[]
BG1=pygame.image.load('game-background-hd-images-14569.jpeg')
for i in range(3):
    PLAYER.append(pygame.image.load('bird'+str(i)+'.png'))
PIPE=pygame.image.load('pipe.png')
PIPEROTATE=pygame.transform.rotate(PIPE,180)
NUMBERIMG=[]
NUMBERIMGRESIZE=[]
SCORE=0


for i in range(11):
    NUMBERIMG.append(pygame.image.load(str(i)+'-Number-PNG.png'))
for i in NUMBERIMG:
    NUMBERIMGRESIZE.append(pygame.transform.scale(i,(32,32)))

#making main window
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('                                                                                                         FLAPPY BIRD')
pygame.display.set_icon(ICON)

#music
CONTROL=True
mixer.music.load('Retro-Frantic_V001_Looping.mp3')
if CONTROL==True:
    mixer.music.play(-1)



#defining constants for pipe
pipeupx=[]
pipeupy=[]
pipeupx_change=1
DISTANCE_BETWEEN_PIPE=[]

for i in range(4):
    pipeupx.append(0)
    
for i in range(3):
    pipeupx[i]=pipeupx[i-1]+random.randint(250,400)
    pipeupy.append(random.randint(-230,-150))
    DISTANCE_BETWEEN_PIPE.append(random.randint(410,550))

#defining constants for player
PLAYERX=100
PLAYERY=300
PLAYERY_CHANGE=1
count=0

#defining constants for base image
BASEX=0
BASEX_CHANGE=0.5

#defining constant for number image
NUMBERS=[]
SCOREIMG=[]

#defining constants for game over
gameover1=pygame.font.Font('freesansbold.ttf',90)





#defining a function to display background image
def background():
    if count>60000:
        screen.blit(BG1,(0,0))
    else:
        screen.blit(BG,(0,0))

def pipe(x,y,d):
    
    screen.blit(PIPEROTATE,(x,y))
    screen.blit(PIPE,(x,y+d))

def player(x,y):
    global over
    
    if count%5==0 and over==False:
        screen.blit(PLAYER[1],(x,y))
    if count%10==0 and over==False:
        screen.blit(PLAYER[2],(x,y))
    else:
        screen.blit(PLAYER[0],(x,y))
def base(x):
    screen.blit(BASE,(x,520))
    screen.blit(BASE,(x+336,520))
    screen.blit(BASE,(x+672,520))

def score(s):
    global NUMBERS
    counter=0
    if s<10:
        for i in range(11):
            if i==s:
                screen.blit(NUMBERIMGRESIZE[i],(10,10))
    
    else:
        string=str(s)
        NUMBERS.clear()
        for i in string:
            NUMBERS.append(int(i))
        for n in range(len(NUMBERS)):
            screen.blit(NUMBERIMGRESIZE[NUMBERS[n]],(10+counter*32,10))
            counter+=1
def gameover(y1,x2,y2,d):
    
    
    if y1<=y2+320+10  and x2==100:
        
        return True
    elif y1>=y2+d-10 and  x2==100:
        
        return True
    else:
        return False
def game_over_blit():
    msg=gameover1.render("Game Over",True,(255,255,255))
    screen.blit(msg,(170,250))
#making main while loop
over=False
while CONTROL:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            CONTROL=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                PLAYERY_CHANGE-=3
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                PLAYERY_CHANGE=0.5
                sound=mixer.Sound('SFX_Jump_16.wav')
                sound.play()
        
    background()
    
    
    for i in range(3):
        
        pipe(pipeupx[i],pipeupy[i],DISTANCE_BETWEEN_PIPE[i])
        pipeupx[i]-=pipeupx_change   
        
        if pipeupx[i]<-52:
            pipeupx[i]=852
            DISTANCE_BETWEEN_PIPE[i]=random.randint(410,500)
    PLAYERY+=PLAYERY_CHANGE
    player(PLAYERX,PLAYERY)
    BASEX-=BASEX_CHANGE
    base(BASEX)
    if BASEX<-208:
        BASEX=0
    for i in range(3):
        if pipeupx[i]==100:
            SCORE+=1
            score_up_sound=mixer.Sound('SFX_Jump_01.wav')
            score_up_sound.play()
        elif pipeupx_change==0:
            SCORE=0
        over=gameover(PLAYERY,pipeupx[i],pipeupy[i],DISTANCE_BETWEEN_PIPE[i])
        if over==True:
            game_over_blit()
            mixer.music.pause()
            PLAYERX=100
            PLAYERY=300
            PLAYERY_CHANGE=0
            pipeupx_change=0
            BASEX_CHANGE=0
            gameover1_sound=mixer.Sound('SFX_Jump_47.wav')
            gameover1_sound.play()
            pygame.mixer.pause()
    score(SCORE)
    count+=1
    
        
            
    pygame.display.update()
