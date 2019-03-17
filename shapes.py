import pygame
from settings import *
from colors import *

class Button:
    def __init__(self,text):
        self.x = 0
        self.y = 0
        self.width = 150
        self.height = 50
        self.surface = pygame.Surface((self.width,self.height))
        self.surface.fill(RED)
        self.text = Text(text)
        self.isSelected = False

    def draw(self,screen):
        if (self.isSelected):
            pygame.draw.rect(screen, RED, [self.x,self.y, self.width, self.height])
        else:
            pygame.draw.rect(screen, BLUE, [self.x,self.y, self.width, self.height])

        self.text.draw(screen,self.x+self.width/2,self.y+self.height/2)

    def events(self,event,mouse_x,mouse_y):
        if (pygame.mouse.get_rel()!=(0,0)): 
            if(self.checkMouseIn(mouse_x,mouse_y)):
                self.isSelected = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("passed")
                        return True
            else:
                self.isSelected = False
        return False

    def checkMouseIn(self,mouse_x,mouse_y):
        if ( mouse_x > self.x and mouse_x < self.x + self.width ):
            if ( mouse_y > self.y and mouse_y < self.y + self.height ):
                self.isSelected = True
                return True
        return False
            

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def setCoord(self,x,y,mode = DRAW_FROM_TOPLEFT):
        if (mode == DRAW_FROM_CENTER):
            self.x = x - self.width/2
            self.y = y + self.height/2
        else:
            self.x = x
            self.y = y
        


class EditText:
    def __init__(self,hide=0):
        self.hide = hide
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 50
        self.textString = ""
        self.textDisplayed = ""
        self.isSelected = False
        self.maxChar = 10
        self.padding = 0

    def addPadding(self,padding):
        self.padding = padding
        

    def setCoord(self,x,y):
        self.x  = x-self.width/2
        self.y = y+self.height/2

    def checkMouseIn(self,mouse_x,mouse_y):
        if ( mouse_x > self.x and mouse_x < self.x + self.width ):
            if ( mouse_y > self.y and mouse_y < self.y + self.height ):
                return True
        return False

    def draw(self,screen):
        if (self.hide == 0):
            self.textDisplayed = self.textString
        else:
            self.textDisplayed = ""
            for i in range(len(self.textString)):
                self.textDisplayed += "*"
        self.text = Text(self.textDisplayed,46 if self.hide == 1 else 36)
        pygame.draw.rect(screen, GREEN, [self.x, self.y , self.width , self.height ] ,2)
        self.text.draw(screen,self.x+10,self.y+self.height/2+self.padding,1)
        if self.isSelected:
            pygame.draw.rect(screen, RED, [self.text.textrect.right , self.text.textrect.centery-(self.height-10)/2-self.padding, 2 , self.height-10 ])
            
    def events(self,event):
        capslock = pygame.key.get_mods() & pygame.KMOD_CAPS
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ( self.checkMouseIn(mouse_x,mouse_y)):
                self.isSelected = True
        if event.type == pygame.KEYDOWN and self.isSelected:
            if len(self.textString)< self.maxChar:
                if event.key == pygame.K_q:
                    self.textString += "a" if (not capslock ) else "A"
                elif event.key == pygame.K_w:
                    self.textString += "z"
                elif event.key == pygame.K_e:
                    self.textString += "e"
                elif event.key == pygame.K_r:
                    self.textString += "r"
                elif event.key == pygame.K_t:
                    self.textString += "t"
                elif event.key == pygame.K_y:
                    self.textString += "y"                
                elif event.key == pygame.K_u:
                    self.textString += "u"
                elif event.key == pygame.K_i:
                    self.textString += "i"        
                elif event.key == pygame.K_o:
                    self.textString += "o"
                elif event.key == pygame.K_p:
                    self.textString += "p"
                elif event.key == pygame.K_a:
                    self.textString += "q"
                elif event.key == pygame.K_s:
                    self.textString += "s"
                elif event.key == pygame.K_d:
                    self.textString += "d"                
                elif event.key == pygame.K_f:
                    self.textString += "f"
                elif event.key == pygame.K_g:
                    self.textString += "g"
                elif event.key == pygame.K_h:
                    self.textString += "h"
                elif event.key == pygame.K_j:
                    self.textString += "j"
                elif event.key == pygame.K_k:
                    self.textString += "k"
                elif event.key == pygame.K_l:
                    self.textString += "l"
                elif event.key == pygame.K_SEMICOLON: 
                    self.textString += "m"                
                elif event.key == pygame.K_z:
                    self.textString += "w"
                elif event.key == pygame.K_x:
                    self.textString += "x" 
                elif event.key == pygame.K_c:
                    self.textString += "c"
                elif event.key == pygame.K_v:
                    self.textString += "v"
                elif event.key == pygame.K_b:
                    self.textString += "b"
                elif event.key == pygame.K_n:
                    self.textString += "n"
            if event.key == pygame.K_BACKSPACE:
                print("pressed")
                if (len(self.textString)>0):        
                    self.textString = self.textString[:-1]
                print(self.textString)

class Text:
    def __init__(self,text,size=30):
        self.font = pygame.font.SysFont(None, size)
        self.text = self.font.render(text, True, GREEN)
        self.textrect = self.text.get_rect()
        

    def draw(self, screen,x,y,mode=0):
        
        if (mode == 1):
            self.textrect.x = x
        else:
            self.textrect.centerx = x
        self.textrect.centery = y
        screen.blit(self.text, self.textrect)

   
        
        
        
        
