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

    character=pygame.image.load(os.path.join('assets'+os.sep+'images',direction+'-2.png')).convert()
    character.set_colorkey((34,177,76))
    character_surface=pygame.Surface((150,150))
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    pygame.Rect((0,0),(137,210))
    
    character=pygame.image.load(os.path.join('assets'+os.sep+'images',direction+'-1.png')).convert()
    character.set_colorkey((34,177,76))
    character_surface=pygame.Surface((150,150))
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    
    character=pygame.image.load(os.path.join('assets'+os.sep+'images',direction+'-2.png')).convert()
    character.set_colorkey((34,177,76))
    character_surface=pygame.Surface((150,150))
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(100)
    
    character=pygame.image.load(os.path.join('assets'+os.sep+'images',direction+'-3.png')).convert()
    character.set_colorkey((34,177,76))
    character_surface=pygame.Surface((150,150))
    screen.blit(character,location)
    pygame.display.flip()
    pygame.time.delay(1000)
    
    character=pygame.image.load(os.path.join('assets'+os.sep+'images',direction+'-2.png')).convert()
    character.set_colorkey((34,177,76))
    character_surface=pygame.Surface((150,150))
    screen.blit(character,location)
    pygame.display.flip()



#initializing the game

pygame.init()

done=False
clock=pygame.time.Clock()

screen=pygame.display.set_mode((1080,620))
drawing_surface=pygame.image.load(os.path.join('assets'+os.sep+'backgrounds','image1.png')).convert()
screen.blit(drawing_surface, (0,0))
pygame.display.flip()

bouncing_image(FRONT,screen,(0,0))

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    else:
        bouncing_image(FRONT,screen,(0,0))


pygame.quit()
sys.exit()
