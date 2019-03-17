import pygame
from shapes import *
from colors import * 

pygame.init()

screen = pygame.display.set_mode((800,600))


running = True
editText = EditText()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        editText.events(event)

    screen.fill(BLACK)
    editText.draw(screen)
    pygame.display.update()
    


pygame.quit()
quit()
