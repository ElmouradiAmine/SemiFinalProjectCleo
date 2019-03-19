import pygame

from settings import *
from screens import *


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

menuScreen = MenuScreen(screen)
menuScreen.run()

    
pygame.quit()
quit()




        
        
        




