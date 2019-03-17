import pygame

#Personal imports
from colors import *
from settings import *
from shapes import *
from login import *
from playnowScreen import *
from signup import *

class SignupScreen:
    def __init__(self,screen):
        #pygame.display.set_icon(ICON)
        self.screen = screen
        #On crée un objet clock qui va nous permettre de traquer le temps du jeu
        #et aussi contrôler la vitesse du jeu ( càd les FPS )
        self.clock = pygame.time.Clock()

        #C'est le flag qui contrôle l'execution du jeu une fois mis à false le jeu se ferme
        self.running = True

        #Cette variable pointe vers le button actuel selectionné par l'utilisateur
        self.selected = 0

        #Le nombre de button dans le MenuScreen
        self.length = 4
        
        #Control la disposition des buttons dans l'ecran
        self.margin = MARGIN_DEFAULT/2
        self.padding = PADDING_DEFAULT*1.3
        self.textStringList = [ "USERNAME" , "EMAIL" , "PASSWORD" , "CONFIRM PASSWORD" ]
        self.textGroup = [ Text(self.textStringList[i]) for i in range(4)]
        self.editTextGroup = [ EditText(i//2) for i in range(4)]
        self.buttonLogin = Button('SIGN UP')
        self.buttonLogin.setCoord(600,520)
        self.buttonBack = Button('BACK')
        self.buttonBack.setCoord(20,520)
        
        self.editTextGroup[2].addPadding(10)
        self.editTextGroup[3].addPadding(10)
        for i in range(4):
            self.editTextGroup[i].setCoord(WIDTH/2, self.margin+(self.padding+self.editTextGroup[i].height)*i)
        self.editTextGroup[0].isSelected = True
        

        
    #Il s'agit de la boucle principale
    #C'est ici ou il y'a un check des events, update des elements de l'UI..
    def run(self):
        while self.running:
            #Voir la definition de ces methodes en bas
            self.events()
            self.draw()
            #regle la vitesse du jeu
            self.clock.tick(FPS)
    

    #c'est la methode qui track les evenements de l'utilisateur
    def events(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if ( self.buttonLogin.checkMouseIn(mouse_x,mouse_y)):
            self.buttonLogin.isSelected = True
        else:
             self.buttonLogin.isSelected =False

        if ( self.buttonBack.checkMouseIn(mouse_x,mouse_y)):
            self.buttonBack.isSelected = True
        else:
             self.buttonBack.isSelected =False
             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    self.editTextGroup[i].isSelected = False
                if event.button == 1 and self.buttonLogin.isSelected:
                    print(self.editTextGroup[0].textString)
                    print(self.editTextGroup[1].textString)
                    signup(self.editTextGroup[0].textString,self.editTextGroup[2].textString,self.editTextGroup[1].toString())
                    playnowScreen = PlaynowScreen(self.screen)
                    playnowScreen.run()

                elif event.button == 1 and self.buttonBack.isSelected:
                    self.running = False
                    
            for i in range(4):
                self.editTextGroup[i].events(event)
            
            
         


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.fill(BLACK)
        for i in range(4):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

        
    def update(self):
        pass

    def release(self):
        pygame.quit()
        quit()
