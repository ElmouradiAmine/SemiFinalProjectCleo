from colors import *
from settings import *
from widgets import *
from firebase import firebase
from crypting import cryptage
from sys import *
import pygame


"""
**************************************************
*              MENU SCREEN CLASS                 *
**************************************************
"""
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
        self.margin = MARGIN_DEFAULT-30
        self.padding = PADDING_DEFAULT
        self.background = pygame.image.load('./Images/background/background.png')

        self.imagesPath = [ 'assets/PlayButton.png','assets/LoginButton.png', 'assets/SignUpButton.png','assets/ExitButton.png' ]
        self.imagesPathEffect = [ 'assets/PlayButtonEffect.png','assets/LoginButtonEffect.png', 'assets/SignUpButtonEffect.png','assets/ExitButtonEffect.png' ]

        #Le text qui sera dans les buttons
        self.buttonsText = [ 'PLAY NOW' , 'LOGIN' , 'SIGN UP' ,'EXIT' ]
        #Ici on crée une liste de l'objet button qui prend en parametre le text
        self.buttons = [Button(self.buttonsText[i],self.imagesPath[i],self.imagesPathEffect[i]) for i in range(4)]
        
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
                    if ( self.selected == EXIT):
                        self.running = False
                        #self.release()
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
                        #self.release()
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
        self.screen.blit(self.background , (0,0))
        #on dessine les buttons.
        for button in self.buttons:
            button.draw(self.screen)
    
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

        
    def update(self):
        pass

    def release(self):
        pygame.quit()
        sys.exit(1)
        quit()
        
        







"""
**************************************************
*              PLAY NOW SCREEN CLASS             *
**************************************************
"""
class PlaynowScreen:
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
        self.length = 5
        
        #Control la disposition des buttons dans l'ecran
        self.margin = MARGIN_DEFAULT -30
        self.padding = PADDING_DEFAULT
        self.background = pygame.image.load('./Images/background/background.png')

        #Le text qui sera dans les buttons
        self.imagesPath = [ 'assets/PlayButton.png','assets/ResumeButton.png', 'assets/AboutUsButton.png','assets/ExitButton.png', 'assets/SmallButtons/MoveLeftButton.png' ]
        self.imagesPathEffect = [ 'assets/PlayButtonEffect.png','assets/ResumeButtonEffect.png', 'assets/AboutUsButtonEffect.png','assets/ExitButtonEffect.png', 'assets/SmallButtons/MoveLeftButton.png']
        
        self.buttonsText = [ 'PLAY' , 'RESUME' , 'ABOUT US' ,'EXIT' , 'BACK' ]
        #Ici on crée une liste de l'objet button qui prend en parametre le text
        self.buttons = [Button(self.buttonsText[i],self.imagesPath[i],self.imagesPathEffect[i], True if i == self.length -1 else False) for i in range(self.length)]
        #Apres avoir créer les buttons il faudra definir leur position respective.
        for i in range(self.length-1):
            self.buttons[i].setCoord(WIDTH/2,(self.buttons[i].height + self.padding)*i + self.margin,DRAW_FROM_CENTER)
        self.buttons[self.selected].isSelected = True


        self.buttons[4].setCoord(20,520)
        
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
                for i in range(self.length):
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
                    self.running = False
                    if ( self.selected == EXIT ):
                        self.release()
                    if ( self.selected == PLAYNOW):
                        levelSelection = LevelSelection(self.screen)
                        levelSelection.run()
                
                
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
                    self.running = False
                    if ( self.selected == EXIT ):
                        self.release()
                    if ( self.selected == PLAYNOW):
                        levelSelection = LevelSelection(self.screen)
                        levelSelection.run()
                


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.blit(self.background,(0,0))
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








"""
**************************************************
*              LOGIN SCREEN CLASS                *
**************************************************
"""



class LoginScreen:
    def __init__(self,screen):

        #pygame.display.set_icon(ICON)
        self.screen = screen
        #On crée un objet clock qui va nous permettre de traquer le temps du jeu
        #et aussi contrôler la vitesse du jeu ( càd les FPS )
        self.clock = pygame.time.Clock()

        #C'est le flag qui contrôle l'execution du jeu une fois mis à false le jeu se ferme
        self.running = True

        #Cette variable pointe vers le button actuel selectionné par l'utilisateur
        self.background = pygame.image.load('./Images/background/background.png')

        #Le nombre de button dans le MenuScreen
        self.length = 4
        
        #Control la disposition des buttons dans l'ecran
        self.margin = MARGIN_DEFAULT*1.5
        self.padding = PADDING_DEFAULT*2
        self.textStringList = [ "Username" , "Password" ]
        self.textGroup = [ Text(self.textStringList[i]) for i in range(2)]
        self.editTextGroup = [ EditText(i) for i in range(2)]

        self.buttonLogin = Button('LOGIN','assets/LoginButton.png','assets/LoginButton.png')
        self.buttonLogin.setCoord(550,450)

        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',1)
        self.buttonBack.setCoord(20,520)
        
        self.editTextGroup[1].addPadding(10)
        for i in range(2):
            self.editTextGroup[i].setCoord(WIDTH/2,self.margin + (self.padding+self.editTextGroup[i].height)*i)
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
             self.buttonBack.isSelected = False

             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.release()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(2):
                    self.editTextGroup[i].isSelected = False
                if event.button == 1 and self.buttonLogin.isSelected:
                    print(self.editTextGroup[0].textString)
                    print(self.editTextGroup[1].textString)
                    if (connect(self.editTextGroup[0].textString,self.editTextGroup[1].textString)):
                        playnowScreen = PlaynowScreen(self.screen)
                        playnowScreen.run()
                        print("connected")
                    else:
                        print("Failed connexion")
                    
                    print("PRESSED LOGIN")
                elif event.button == 1 and self.buttonBack.isSelected:
                    self.running = False
                    
                    
            for i in range(2):
                self.editTextGroup[i].events(event)
            
            
         


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.blit(self.background,(0,0))
        for i in range(2):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

        
    def update(self):
        pass




    def connect(username,password):
        firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)
        result = firebaseObj.get('/Users/', '')
        connSucc = False

        for key in result:
            
            if result[key]['Username'] == username and  result[key]['Password'] == password:
                print('Connection successful')
                connSucc = True
                break;
        return connSucc


        def release(self):
            pygame.quit()
            quit()








"""
**************************************************
*              SIGN UP SCREEN CLASS              *
**************************************************
"""

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
        self.background = pygame.image.load('./Images/background/background.png')
        #Control la disposition des buttons dans l'ecran
        self.margin = MARGIN_DEFAULT/2
        self.padding = PADDING_DEFAULT*1.3
        self.textStringList = [ "USERNAME" , "EMAIL" , "PASSWORD" , "CONFIRM PASSWORD" ]
        self.textGroup = [ Text(self.textStringList[i]) for i in range(4)]
        self.editTextGroup = [ EditText(i//2) for i in range(4)]
        self.buttonLogin = Button('SIGNUP','assets/SignUpButton.png','assets/SignUpButtonEffect.png')
        self.buttonLogin.setCoord(600,480)
        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',1)
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
        self.screen.blit(self.background, (0,0))
        for i in range(4):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

    def update(self):
        pass



    def signup(username,password,email):  
        firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)  
        data = {
                'Username': username,
                'Password': password,
                'Email' : email,
                'Score': 0,
            }

        result = firebaseObj.post('/Users',data)
        print('Subscription successful')



    def release(self):
        pygame.quit()
        quit()


class LevelSelection:
    def __init__(self,screen):
    #pygame.display.set_icon(ICON)
        self.screen = screen
    #On crée un objet clock qui va nous permettre de traquer le temps du jeu
    #et aussi contrôler la vitesse du jeu ( càd les FPS )
        self.clock = pygame.time.Clock()

    #C'est le flag qui contrôle l'execution du jeu une fois mis à false le jeu se ferme
        self.running = True
        self.background = pygame.image.load('./Images/background/levelSelectionBackground.jpg')
    #Cette variable pointe vers le button actuel selectionné par l'utilisateur
        self.selected = 0
        self.buttons = [ Button('LockedButton', 'assets\SmallButtons\lockButton.png', 'assets\SmallButtons\lockButton.png', 1) for i in range(4) ]
        for i in range(4):
            self.buttons[i].setCoord(250+i*80,300)
        self.buttonFinalBoss = Button('Final button' , './assets/SmallButtons/finalBoss3.png', './assets/SmallButtons/finalBoss3.png',2)
        self.buttonFinalBoss.setCoord(350,400)

        """#Le nombre de button dans le MenuScreen
        self.length = 4
        self.background = pygame.image.load('./Images/background/background.png')
        #Control la disposition des buttons dans l'ecran
        self.margin = MARGIN_DEFAULT/2
        self.padding = PADDING_DEFAULT*1.3
        self.textStringList = [ "USERNAME" , "EMAIL" , "PASSWORD" , "CONFIRM PASSWORD" ]
        self.textGroup = [ Text(self.textStringList[i]) for i in range(4)]
        self.editTextGroup = [ EditText(i//2) for i in range(4)]
        self.buttonLogin = Button('SIGNUP','assets/SignUpButton.png','assets/SignUpButtonEffect.png')
        self.buttonLogin.setCoord(600,480)
        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',True)
        self.buttonBack.setCoord(20,520)
        
        self.editTextGroup[2].addPadding(10)
        self.editTextGroup[3].addPadding(10)
        for i in range(4):
            self.editTextGroup[i].setCoord(WIDTH/2, self.margin+(self.padding+self.editTextGroup[i].height)*i)
        self.editTextGroup[0].isSelected = True"""
        

        
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.release()
        """mouse_x, mouse_y = pygame.mouse.get_pos()
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
                self.editTextGroup[i].events(event)"""
            
            
         


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.blit(self.background, (0,0))
        
        
        """self.screen.blit(self.background, (0,0))
        for i in range(4):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()"""
        pygame.draw.rect(self.screen, RED , [275, 325, 250, 3])
        for i in range(4):
            self.buttons[i].draw(self.screen)
        self.buttonFinalBoss.draw(self.screen)
        pygame.display.update()




    def release(self):
        pygame.quit()
        quit()

    
