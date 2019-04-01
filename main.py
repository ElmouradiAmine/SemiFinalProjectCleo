import pygame

from settings import *
from screens import *
from sys import *

if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)
    pygame.mixer.music.load('./Music/egyptMusic.mp3')
    pygame.mixer.music.play()

    menuScreen = MenuScreen(screen)
    menuScreen.run()
    pygame.quit()
    quit()




        
        
        




