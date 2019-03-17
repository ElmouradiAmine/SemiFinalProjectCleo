import pygame

from menuScreen import * 
from settings import *
from playnowScreen import *


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

menuScreen = MenuScreen(screen)
menuScreen.run()

    
pygame.quit()
quit()




        
        
        




