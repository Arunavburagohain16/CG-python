import pygame
import time
import random

pygame.init()

display_width = 1368
display_height = 768

mjlist=[]
mjspinlist=[]
#mjlist=['mj1.png','mj2.png','mj3.png','mj4.png','mj5.png','mj6.png','mj7.png','mj8.png','mj9.png','mj10.png']
#mjrevlist=['mj1-ConvertImage.png','mj2-ConvertImage.png','mj3-ConvertImage.png','mj4-ConvertImage.png','mj5-ConvertImage.png','mj6-ConvertImage.png','mj7-ConvertImage.png','mj8-ConvertImage.png','mj9-ConvertImage.png','mj10-ConvertImage.png']
for i in range(1,26):
    a='mj'+str(i)
    mjlist.append(a)
#print(mjlist)
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
y = 200#500
xchange = 5

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    mjImg = pygame.image.load(mjlist[w1])
    mjspinImg = pygame.image.load(mjspinlist[w2])
    #mjImgrev = pygame.image.load(mjrevlist[w1])
    #stageImg=pygame.image.load("stage.jpg")
    gameDisplay.fill((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    #gameDisplay.fill(black)
    #gameDisplay.blit(stageImg,(0,0))
    pygame.display.flip()
    #pygame.draw.circle(gameDisplay,white,[x+130,y+50],200)

    if(xchange==5):
        gameDisplay.blit(mjImg,(x,y))

    elif(xchange==-5):
        gameDisplay.blit(mjImg,(x,y))

    pygame.display.flip()
    x+=xchange
    w1+=1

    if(x>=1000 or x<0):
        xchange=0
        gameDisplay.blit(mjspinImg,(1000,y))
        pygame.display.flip()
        w2+=1
        if(w2>28):
            w2=0
            x=0
            time.sleep(1)
            #xchange=xchange*-1

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
