import pygame
import random

# Define some colors
WHITE=(255,255,255)
BLACK=(0,0,0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (1366,768)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SCREENSAVER")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
fl=0
lp=0
k=0
j=0
j1=1
j2=1
g=1
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    l=95
    m=0
    # --- Drawing code

    #FOR SKY

    p=0
    r=60
    t=1
    for i in range(10):
        pii=((225-k)/j1,(64-t)/j1,r)
        poo=pygame.draw.rect(screen,pii,[0,p,1376,50])
        p+=50
        r-=5
        t-=5

        if(225-k<20 or 64-t-g<20):
            j1=20


    #CODE FOR SUN
    print(pii)
    if(pii==(3.0, 5.4, 15)):
        pygame.draw.circle(screen,(220,220,220),[684,0+lp],l)
    else:
        for i in range(7):
            pygame.draw.circle(screen,(255,165,m),[684,450+lp],l)
            l-=5
            m+=10

    #CODE FOR BOAT

    pygame.draw.polygon(screen, (15,15,15), [[1+fl,470],[30+fl,490],[60+fl,470]],0)
    pygame.draw.polygon(screen, (15,15,15), [[20+fl,470],[30+fl,460],[40+fl,470]],0)
    fl+=100
    if(fl>1376 or fl<0):
        fl=0.5*-1
        lp+=7
        k+=5
        j+=1
        g+=2
    #CODE FOR SEA

    n=1
    o=767
    for i in range(30):
        pygame.draw.rect(screen,(122-n,112-n,160-n),[0,o,1376,10])
        o-=10
        n+=3

    #CODE FOR REFLECTION
    '''
    c=0
    d=0
    e=0
    #f=0
    #g=0
    #h=0
    for i in range(40):
    #pygame.draw.rect(screen,(200,50+c,0+d),[515+e,477+f,311-g-h,20])
        pygame.draw.ellipse(screen,(200,50+c,0+d),[510,476.5,350,50-e+0.3],0)
        c+=2
        d+=2
        e+=1
        #f+=1
        #g+=1
        #h+=1
    '''
    #CODE REFLECTION
    '''
    col=5
    a1=5
    for i in range(10):
        pygame.draw.polygon(screen,(255-col,127-col,80-col+15),[[540+a1,477],[620,768],[740,768],[820-a1,477]],0)
        col+=10
        a1+=5
    '''
    # --- Go ahead and update the screen with what we've drawn.

    #Getting the position of the cursor
    '''
    pos=pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]
    print("X:",x," Y:",y,"\n")'''
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(60)

# Close the window and quit.

pygame.quit()
