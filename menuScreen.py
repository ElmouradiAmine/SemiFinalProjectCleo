import pygame

#Personal imports
from colors import *
from settings import *
from shapes import *
from playnowScreen import *
from loginScreen import *
from signupScreen import *


"""Il s'agit du PlayScreen class
Cette classe permet d'afficher la premiere page du jeu
et de diriger le programme vers les differentes route selon
l'option choisie par l'utilisateur"""
class MenuScreen:
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
        self.margin = MARGIN_DEFAULT
        self.padding = PADDING_DEFAULT

        self.imagesPath = [ './Images/Buttons/exit.png' ]

        #Le text qui sera dans les buttons
        self.buttonsText = [ 'PLAY NOW' , 'LOGIN' , 'SIGN UP' ,'EXIT' ]
        #Ici on crée une liste de l'objet button qui prend en parametre le text
        self.buttons = [Button(self.buttonsText[i]) for i in range(4)]
        
        #Apres avoir créer les buttons il faudra definir leur position respective.
        for i in range(4):
            self.buttons[i].setCoord(WIDTH/2,(self.buttons[i].height + self.padding)*i + self.margin,DRAW_FROM_CENTER)
        self.buttons[self.selected].isSelected = True
        
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
        
        #Ici on boucle sur tout les evenements generés
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if (pygame.mouse.get_rel()!=(0,0)):
                for i in range(4):
                    if(i!= self.selected):
                        self.buttons[i].isSelected = False
                    if(self.buttons[i].checkMouseIn(x,y)):
                        self.selected = i
                   
            #Si on clique sur le button croix de la fenettre on quitte le jeu
            if event.type == pygame.QUIT:
                self.running = False
                self.release()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ( self.selected == EXIT ):
                        self.running = False
                        self.release()
                    elif ( self.selected == PLAYNOW):
                        playnowScreen = PlaynowScreen(self.screen)
                        playnowScreen.run()
                    elif (self.selected == LOGIN):
                        loginScreen = LoginScreen(self.screen)
                        loginScreen.run()
                    elif ( self.selected == SIGNUP):
                        signupScreen = SignupScreen(self.screen)
                        signupScreen.run()
                
                
                
            if event.type == pygame.KEYDOWN:
                #Ce bloc permet de traquer le button actuellement selectionné
                if event.key == pygame.K_UP:
                    if self.selected == 0:
                        self.selected = self.length - 1
                    else:
                        self.selected -= 1

                if event.key == pygame.K_DOWN:
                    if self.selected == self.length -1:
                        self.selected = 0
                    else:
                        self.selected += 1
                for button in self.buttons:
                    button.isSelected = False
                self.buttons[self.selected].isSelected = True

                if event.key == pygame.K_RETURN:
                    if (self.selected == EXIT ):
                        self.running = False
                        self.release()
                    elif (self.selected == PLAYNOW):
                        playnowScreen = PlaynowScreen(self.screen)
                        playnowScreen.run()
                    elif (self.selected == LOGIN):
                        loginScreen = LoginScreen(self.screen)
                        loginScreen.run()
                    elif ( self.selected == SIGNUP):
                        signupScreen = SignupScreen(self.screen)
                        signupScreen.run()
                        
                        
                


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.fill(BLACK)
        #on dessine les buttons.
        for button in self.buttons:
            button.draw(self.screen)
    
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

        
    def update(self):
        pass

    def release(self):
        pygame.quit()
        quit()
