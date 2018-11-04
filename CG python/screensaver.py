import pygame
import random

# Define some colors
WHITE=(255,255,255)
BLACK=(0,0,0)
Orange=(255,165,0)
DarkOrange=(255,200,0)
Coral=(255,127,80)
LightCoral=(240,128,208)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
UN = (94,23,12)
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

rect=[Orange,DarkOrange,Coral,LightCoral,GREEN,UN,RED,WHITE]

#Starting postion
rect_x=684.0
rect_y=384.0

#change postion
rect_change_x=5
rect_change_y=5

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # --- Drawing code

    for i in range(10000):
        pygame.display.flip()
        #pygame.draw.circle(screen,BLACK,[684,384],100)
        pygame.draw.rect(screen,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),[rect_x,rect_y,1,1])

        rect_x+=rect_change_x
        rect_y+=rect_change_y
        if rect_x>1367 or rect_x<0:
            rect_change_x=rect_change_x*-1
        elif rect_y>767 or rect_y<0:
            rect_change_y=rect_change_y*-1

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(60)

# Close the window and quit.

pygame.quit()
