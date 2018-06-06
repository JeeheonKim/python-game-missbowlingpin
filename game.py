import pygame
import os

LEFT=-1
RIGHT=1
FRONT=0



#graphics
def bouncing_image(direction,screen,location):
    direction='front'
    if direction==LEFT:
        direction='left'
    elif direction==RIGHT:
        direction='right'

    character=pygame.image.load(os.path.join('assets',direction+'-deflated.png'))
    character_surface=pygame.Surface((137,203))
    pygame.transform.scale(character,(137,203),character_surface)
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    character=pygame.image.load(os.path.join('assets',direction+'-round.png'))
    character_surface=pygame.Surface((137,209))
    pygame.transform.scale(character,(137,209),character_surface)
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    character=pygame.image.load(os.path.join('assets',direction+'-deflated.png'))
    character_surface=pygame.Surface((137,203))
    pygame.transform.scale(character,(137,203),character_surface)
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    character=pygame.image.load(os.path.join('assets',direction+'-half.png'))
    character_surface=pygame.Surface((137,192))
    pygame.transform.scale(character,(137,192),character_surface)
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(1000)
    character=pygame.image.load(os.path.join('assets',direction+'-deflated.png'))
    character_surface=pygame.Surface((137,203))
    pygame.transform.scale(character,(137,203),character_surface)
    screen.blit(character,location)
    pygame.display.flip()



#initializing the game

pygame.init()

done=False
clock=pygame.time.Clock()

screen=pygame.display.set_mode((500,400))
screen.fill((255,255,255))
drawing_surface=pygame.Surface((450,350))
drawing_surface.fill((245,245,220))


#draw_grid() # this is just for test


screen.blit(drawing_surface, (50,50))
pygame.display.flip()

bouncing_image(FRONT,screen,(0,0))

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    else:
        bouncing_image(FRONT)


pygame.quit()
sys.exit()
