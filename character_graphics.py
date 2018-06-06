import pygame, os

pygame.image.load("")
LEFT=-1
RIGHT=1
FRONT=0
def bouncing_image(direction):
    if direction==LEFT:
        pygame.image.load(os.path.join('assets','front-deflated'))
        pygame.time.delay(10)
        pygame.image.load(os.path.join('assets','front-rount'))
        pygame.time.delay(100)
        pygame.image.load(os.path.join('assets','front-deflated'))
        pygame.time.delay(10)
        pygame.image.load(os.path.join('assets','front-half'))
        pygame.time.delay(10)
        pygame.image.load(os.path.join('assets','front-deflated'))
    elif direction==RIGHT:

    elif direction==FRONT:
        
