import pygame
import time
import random

pygame.init()

display_width = 1368
display_height = 768

mjlist=[]
mjspinlist=[]

#List for the images names
for i in range(1,26):
    a='mj'+str(i)
    mjlist.append(a)

for i in range(26,55):
    a='mj'+str(i)
    mjspinlist.append(a)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MJ')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

w1=0
w2=0
x = 0
y = 200
xchange = 5

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    mjImg = pygame.image.load(mjlist[w1])
    mjspinImg = pygame.image.load(mjspinlist[w2])

    #Display for the Changing Bacground Color
    gameDisplay.fill((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))

    pygame.display.flip()

    if(xchange==5):
        gameDisplay.blit(mjImg,(x,y))

    elif(xchange==-5):
        gameDisplay.blit(mjImg,(x,y))

    pygame.display.flip()
    x+=xchange
    w1+=1

    #Spinning part of MJ
    if(x>=1000 or x<0):
        xchange=0
        gameDisplay.blit(mjspinImg,(1000,y))
        pygame.display.flip()
        w2+=1
        if(w2>28):
            w2=0
            x=0
            time.sleep(1)

    if(x==0):
        xchange=5

    if(w1>24):
        w1=0
        pygame.display.flip()

    else:
        pass
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
quit()
