from colors import *
from settings import *
from widgets import *
from firebase import firebase
from crypting import cryptage
from sys import *
import pygame
import os
import random

pygame.init()
pygame.display.set_mode()

    




##some spagetti global variables
img_playerRight = pygame.image.load(os.path.join('Images', 'heroRight.png')).convert()
img_playerLeft = pygame.image.load(os.path.join('Images', 'heroLeft.png')).convert()


img_mob1Right = pygame.image.load(os.path.join('Images', 'mob1Right.png')).convert()
img_mob1Left = pygame.image.load(os.path.join('Images', 'mob1Left.png')).convert()

block_air = pygame.image.load(os.path.join(
    'Images', 'block-air.png')).convert()
block_air_left = pygame.image.load(os.path.join(
    'Images', 'block-air-left.png')).convert()
block_air_right = pygame.image.load(os.path.join(
    'Images', 'block-air-right.png')).convert()

tileGround = pygame.image.load(os.path.join(
    'Images', 'tileGround.png')).convert()

obstacle1 = pygame.image.load(os.path.join('Images', 'spike_A.png')).convert()

end = pygame.image.load(os.path.join('Images', 'end.png')).convert()
stage2 = pygame.image.load('stage2.jpg')

score = 0
hp = 1000

bg=pygame.image.load('3.jpg')
bg1=pygame.image.load('2.jpg')
bg2=pygame.image.load('1.jpg')
bggo=pygame.image.load('Background3dth.png')
got_logo = pygame.image.load('egypt_png.png')
nk_pic=pygame.image.load('main_character1.png')
LeftKey=pygame.image.load('LeftKey.png')
RightKey=pygame.image.load('RightKey.png')
SpaceBar=pygame.image.load('SpaceBar.png')
dragon_pics=[pygame.image.load('Dragon4.png'),pygame.image.load('Dragon5.png'),pygame.image.load('Dragon6.png')]
BulletSound=pygame.mixer.Sound('bullet.wav')
HitSound=pygame.mixer.Sound('hit.wav')

all_sprites = pygame.sprite.Group()
dragons = pygame.sprite.Group()
bullets=pygame.sprite.Group()


def show_home_screen(screen, msg1,msg2,msg3,blit):
    screen.blit(bggo,(100,0))
    screen.blit(got_logo,(110,-20))
    if blit :
        screen.blit(LeftKey,(155,HEIGHT/4+127))
        screen.blit(RightKey,(250,HEIGHT/4+127))
        screen.blit(SpaceBar,(WIDTH/2-175,HEIGHT/4+185))
    draw_text(screen,BLACK,msg1,20,WIDTH/2,HEIGHT/4+140)
    draw_text(screen,BLACK,msg2,20,WIDTH/2+30,HEIGHT/4+200)
    draw_text(screen,BLACK,msg3,22,WIDTH/2,HEIGHT/4+250)
    pygame.display.flip()
    pygame.time.wait(1000)
    waiting=True
    while waiting :
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                game_over = False
                waiting = False
                
font_name=pygame.font.match_font('arial')
def draw_text(surface,color,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)

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
                    if ( self.selected == EXIT and self.buttons[3].checkMouseIn(x,y)):
                        self.running = False
                        #self.release()
                    elif ( self.selected == PLAYNOW and self.buttons[0].checkMouseIn(x,y)):
                        playnowScreen = PlaynowScreen(self.screen)
                        playnowScreen.run()
                    elif (self.selected == LOGIN and self.buttons[1].checkMouseIn(x,y)):
                        loginScreen = LoginScreen(self.screen)
                        loginScreen.run()
                    elif ( self.selected == SIGNUP and self.buttons[2].checkMouseIn(x,y)):
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
    def __init__(self,screen,username=""):

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
        self.textUsername = Text("Welcome " + username + " !",42,RED)
        
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
                    if ( self.selected == EXIT and self.buttons[3].checkMouseIn(x,y) ):
                        self.release()
                    if ( self.selected == PLAYNOW and self.buttons[0].checkMouseIn(x,y)):
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
        self.textUsername.draw(self.screen,400,50)
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

        self.buttonLogin = Button('LOGIN','assets/LoginButton.png','assets/LoginButtonEffect.png')
        self.buttonLogin.setCoord(550,450)

        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',1)
        self.buttonBack.setCoord(20,520)
        self.showError = False
        self.errorText = Text("An error has occured !",30,RED)
        
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
                self.showError = False
                for i in range(2):
                    self.editTextGroup[i].isSelected = False
                if event.button == 1 and self.buttonLogin.isSelected:
                    print(self.editTextGroup[0].textString)
                    print(self.editTextGroup[1].textString)
                    if (self.connect(self.editTextGroup[0].textString,self.editTextGroup[1].textString)):
                        playnowScreen = PlaynowScreen(self.screen,self.editTextGroup[0].textString)
                        playnowScreen.run()
                        print("connected")
                    else:
                        self.showError = True
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
        if self.showError:
            self.errorText.draw(self.screen,400,420)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()

        
    def update(self):
        pass


    def connect(self,username,password):
        try:
            firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)
            result = firebaseObj.get('/Users/', '')
            connSucc = False

            for key in result:
                
                if result[key]['Username'] == username and  result[key]['Password'] == password:
                    print('Connection successful')
                    connSucc = True
                    break
            return connSucc
        except:
            return False


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
        self.margin = MARGIN_DEFAULT
        self.padding = PADDING_DEFAULT*1.3
        self.textStringList = [ "USERNAME" , "PASSWORD" , "CONFIRM PASSWORD" ]
        self.textGroup = [ Text(self.textStringList[i]) for i in range(3)]
        self.editTextGroup = [ EditText((i+1)//2) for i in range(3)]
        self.buttonLogin = Button('SIGNUP','assets/SignUpButton.png','assets/SignUpButtonEffect.png')
        self.buttonLogin.setCoord(600,480)
        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',1)
        self.buttonBack.setCoord(20,520)

        self.textError = Text('An error has occured',30,RED)
        self.showError = False
        
        self.editTextGroup[2].addPadding(10)
        self.editTextGroup[1].addPadding(10)
        
        for i in range(3):
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
                for i in range(3):
                    self.editTextGroup[i].isSelected = False
                if event.button == 1 and self.buttonLogin.isSelected:
                    print(self.editTextGroup[0].textString)
                    print(self.editTextGroup[1].textString)
                    if(self.signup(self.editTextGroup[0].textString,self.editTextGroup[1].textString)):
                        playnowScreen = PlaynowScreen(self.screen,self.editTextGroup[0].textString)
                        playnowScreen.run()
                    else:
                        self.showError = True

                elif event.button == 1 and self.buttonBack.isSelected:
                    self.running = False
                    
            for i in range(3):
                self.editTextGroup[i].events(event)
            
            
         


    #c'est ici ou on dessine dans l'ecran
    def draw(self):
        self.screen.blit(self.background, (0,0))
        for i in range(3):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        if self.showError:
            self.textError.draw(self.screen,400,450)
        pygame.display.update()

    def update(self):
        pass



    def signup(self,username,password):
        if (username == "" or password == ""):
            return False
        
        try:
            firebaseObj = firebase.FirebaseApplication('https://python-test-f77c7.firebaseio.com/', None)  
            data = {
                    'Username': username,
                    'Password': password,
                    'Score': 0,
                }

            result = firebaseObj.post('/Users',data)
            return True
            print('Subscription successful')
        except:
            return False



    def release(self):
        pygame.quit()
        quit()


class LevelSelection:
    def __init__(self,screen):
        self.screen = screen

    def run(self):
        backdrop = pygame.image.load(
        os.path.join('Images', 'stage2.jpg')).convert()
        backdropbox = self.screen.get_rect()
        font = pygame.font.SysFont('Times New Roman, Arial', 16, True, False)
        font2 = pygame.font.SysFont('Arial', 50 , True, False)
        gameOver = font2.render('GAME OVER', 1, RED)

        player = Player()

        # Create the ennemy
        ennemy_list = []

        # Create all the levels
        level_list = []
        level_list.append(Level_01(player))
        level_list.append(Level_02(player))

        # Set the current level
        current_level_no = 0
        current_level = level_list[current_level_no]

        active_sprite_list = pygame.sprite.Group()
        player.level = current_level

        player.rect.x = 340
        player.rect.y = SCREEN_HEIGHT - player.rect.height
        active_sprite_list.add(player)

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_a:
                        mini2 = miniGame2(self.screen)
                        mini2.run()
                    if event.key == pygame.K_s:
                        miniGame1.run(self.screen)
                    if event.key == pygame.K_d:
                        mini3 = miniGame3(self.screen)
                        mini3.run()

                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.left <= 120:
                diff = 120 - player.rect.left
                player.rect.left = 120
                current_level.shift_world(diff)

            # If the player gets to the end of the level, go to the next level
            current_position = player.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                player.rect.x = 120
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player.level = current_level

            

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.screen.blit(stage2, (0, 0))
            

            current_level.draw(self.screen)
            active_sprite_list.draw(self.screen)
            
            scoreText = font.render('Score: ' + str(score), 1, BLACK)
            self.screen.blit(scoreText, (720, 10))
            hpText = font.render('HP: ' + str(hp), 1, RED)
            self.screen.blit(hpText, (10, 10))

            if hp == 0:
                self.screen.fill(BLACK)
                self.screen.blit(gameOver, (300,250))
               

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.update()
            pygame.display.flip()
    """def __init__(self,screen):
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
        self.buttonBack = Button('BACK','assets/SmallButtons/MoveLeftButton.png','assets/SmallButtons/MoveLeftButton.png',True)
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.release()
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
        
        
        self.screen.blit(self.background, (0,0))
        for i in range(4):
            self.editTextGroup[i].draw(self.screen)
            self.textGroup[i].draw(self.screen,self.editTextGroup[i].x+self.editTextGroup[i].width/2,self.editTextGroup[i].y-20)

        self.buttonLogin.draw(self.screen)
        self.buttonBack.draw(self.screen)
        #Il ne faut pas oublier cette ligne sinon les changements ne seront pas visibles.
        pygame.display.update()
        pygame.draw.rect(self.screen, RED , [275, 325, 250, 3])
        for i in range(4):
            self.buttons[i].draw(self.screen)
        self.buttonFinalBoss.draw(self.screen)
        pygame.display.update()




    def release(self):
        pygame.quit()
        quit()

    
"""


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # width = 40
        # height = 60
        #self.image = pygame.Surface([width, height])
        # self.image.fill(RED)

        img_playerRight.convert_alpha()
        img_playerRight.set_colorkey(ALPHA)
        img_playerLeft.convert_alpha()
        img_playerLeft.set_colorkey(ALPHA)
        

        self.images = []
        self.images.append(img_playerRight)
        self.images.append(img_playerLeft)


        self.image = self.images[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        # health bar
        global hp
        self.health = hp

    def update(self):
        global hp
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x


        #  PLATFORMS
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0


        # Collision with TRAPS

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.trap_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right



        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.trap_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0


        # collision with enemies
        hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in hit_list:
            if hp > 0:
                hp -= 1
                
            
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.image = self.images[1]

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.image = self.images[0]
        
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


class Enemy(pygame.sprite.Sprite):
    # Spawn an enemy
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(img[0])
        self.images.append(img[1])

        self.image = self.images[0]

        for i in range(len(self.images)):
            self.images[i].convert_alpha()
            self.images[i].set_colorkey(ALPHA)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.counter = 0

    def move(self):
        # ai movements lol
        distance = 100
        speed = 2

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
            self.image = self.images[0]
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
            self.image = self.images[1]
        else:
            self.counter = 0

        self.counter += 1

    def hit(self):
        self.kill()

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self, sprite):  # def __init___(self, width, height)
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()

        # self.image = pygame.Surface([width, height])
        # self.image.fill(BROWN)

        self.image = sprite

        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)

        self.rect = self.image.get_rect()

class Trap(pygame.sprite.Sprite):
    """ Platform deals damage to player """

    def __init__(self, sprite):
        super().__init__()

        # self.image = pygame.Surface([width, height])
        # self.image.fill(BROWN)

        self.image = sprite

        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)

        self.rect = self.image.get_rect()


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    platform_list = None
    trap_list = None
    enemy_list = None
    background = None

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.trap_list = pygame.sprite.Group()

        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.trap_list = pygame.sprite.Group()

        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.trap_list.update()

        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.blit(stage2,(0,0))
        #screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.trap_list.draw(screen)
        self.enemy_list.draw(screen)
        for e in self.enemy_list:
            e.move()

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for trap in self.trap_list:
            trap.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def enemyLvl(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], [img_mob1Right,img_mob1Left])
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)

        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(
            os.path.join('images', 'stage2.jpg')).convert()

        self.level_limit = -2500

        # pop the ennemy/mobs
        eloc = []
        eloc1 = [730, 300]
        eloc2 = [830,500]
        self.enemy_list.add(Level.enemyLvl(1, eloc1))
        self.enemy_list.add(Level.enemyLvl(1, eloc2))

        # Array with width, height, x, and y of platform
        levelPlatform = [
                [block_air_left, 405, 500],
                [block_air, 500, 500],
                [block_air_right, 595, 500],

                [block_air_left, 705, 400],
                [block_air, 800, 400],
                [block_air_right, 895, 400],

                [block_air_left, 1025, 280],
                [block_air, 1120, 280],
                [block_air_right, 1215, 280],

                [block_air_left, 1425, 200],
                [block_air, 1520, 200],
                [block_air_right, 1615, 200],

                [block_air_left, 1825, 350],
                [block_air, 1920, 350],
                [block_air_right, 2015, 350],

                # [end, 2200, 530],
                # [end, 2200, 402],
                # [end, 2200, 274],
                # [end, 2200, 146],
                # [end, 2200, 18],
                # [end, 2200, 0],
        ]

        levelTrap = [
                [obstacle1, 1025, 530],
                [obstacle1, 1100, 530],
                [obstacle1, 1175, 530],
                [obstacle1, 1250, 530],
                [obstacle1, 1325, 530],
                [obstacle1, 1400, 530],
        ]

        # Go through the array above and add platforms
        for platform in levelPlatform:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            # moving platforms needs to know the player's position at any time
            block.player = self.player
            self.platform_list.add(block)

        # go through the array to add traps
        for trap in levelTrap:
            block = Trap(trap[0])
            block.rect.x = trap[1]
            block.rect.y = trap[2]
            # moving platforms needs to know the player's position at any time
            block.player = self.player
            self.trap_list.add(block)

class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[block_air, 450, 570],
                 [block_air, 850, 420],
                 [block_air, 1000, 520],
                 [block_air, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)



class miniGame1:
    def __init__(self,screen):
        self.screen = screen


    
    def run(self):
        global all_sprites,dragons,bullets
        nk=NightKing()
        all_sprites.add(nk)
        for i in range(10):
           d=Dragon()
           all_sprites.add(d)
           dragons.add(d)
        
        life = 0
        score=0
        game_over=True
        running = True
        msg1="PRESS              OR             TO MOVE"
        msg2="SPACE BAR TO SHOOT !"
        msg3="NOW PRESS ANY KEY TO START THE GAME"
        
        clock = pygame.time.Clock()
        while running:
         #keep loop running at right speed
            if game_over :
                show_home_screen(self,msg1,msg2,msg3,True)
                
                game_over=False
                running = True
                all_sprites = pygame.sprite.Group()
                dragons = pygame.sprite.Group()
                bullets=pygame.sprite.Group()
                nk=NightKing()
                all_sprites.add(nk)
                for i in range(10):
                   d=Dragon()
                   all_sprites.add(d)
                   if len(dragons) < 10:
                       dragons.add(d)
                # Game loop
                life = 0
                score=0
                
            clock.tick(60)
            #process input (events)
            for event in pygame.event.get():
                #check for closing window
                if event.type == pygame.QUIT:
                    running = False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        BulletSound.play()
                        nk.shoot()
            # add dragons speed
            if pygame.time.get_ticks()>10000 :
                d.speedx+=1/3
                d.speedy+=1/2
            # Update
            all_sprites.update()
           
            # draw/ render
            if life ==0:
                self.blit(bg,(200,0))
            elif life==-1:
                self.blit(bg1,(200,0))
            elif life==-2:
                self.blit(bg2,(200,0))
            else :
                game_over=True
            
            
            
            all_sprites.draw(self)
            pygame.draw.rect(self,BLACK,[600,0,200,600])
            pygame.draw.rect(self,BLACK,[0,0,200,600])
            #collision
            hits=pygame.sprite.groupcollide(bullets,dragons,True,True)
            if hits:
                HitSound.play()
                score+=10
                d=Dragon()
                all_sprites.add(d)
                dragons.add(d)
            hits=pygame.sprite.spritecollide(nk,dragons,True,pygame.sprite.collide_circle)
            for hit in hits :
                #nk_pic=pygame.image.load('NightKingWasHit.png')
                life-=1
                pygame.time.wait(1000)
                d=Dragon()
                all_sprites.add(d)
                dragons.add(d)
                
            # after drawing everything
            
            draw_text(self,BLACK,str(score),30,WIDTH/2,10)
            #score reaches its maximum : 1000
            if score==500:
                draw_text(self,BLACK,'Vous avez tue le monstre.',30,WIDTH/2,10)                
                running = False
            pygame.display.flip()
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Bullet1.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.speedy=-10
        self.rect.centerx=x
        self.rect.bottom=y
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(dragon_pics)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.speedx=random.randrange(-5,5)
        self.speedy = random.randrange(1,8)
    def update(self):
        self.rect.y +=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left<-80 or self.rect.right>WIDTH+25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,10)
            self.speedx=random.randrange(-5,5)

class NightKing(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = nk_pic.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.radius=20
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.speedx = 0
        self.lives=3
        self.visible=True

    def update(self):
        self.speedx = 0
        #pygame.draw.rect(screen,WHITE,self.rect)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class miniGame2:
    def __init__(self,screen):
        self.screen = screen

    def run(self):
        #Screen specifities
        WIDTH = 600
        HEIGHT = 300
        GREEN = (0,255,0)
        BLACK = (0,0,0)
        RED= (255,0,0)
        BLUE= (0,0,255)
        WHITE = (255,255,255)
        #Data
        mon_premier= ["se trouve dans la gueule du loup.", "est un oiseau noir à queue blanche.", "est au milieu de la figure.", "ouvre les portes.", "est le contraire de haut.", "se trouve au milieu du visage.", "est entre 1 et 3.", "est un animal qui vit sur les têtes.", "est un insecte qui vit dans les cheveux.", "est le trou d’une aiguille.", "se trouve sur le visage des personnes âgées.", "est un objet qui sert à faire le ménage.", "est un animal herbivore.", "est un métal précieux.", "est un rongeur à queue longue."]
        #rep_premier= ["croc", "pie", "nez", "clé", "bas", "nez", "deux", "pou", "poux", "chas", "ride", "sceau ", "cerf", "or", "rat"]
        mon_deuxieme= ["est indispensable à la vie.", "coule dans mon corps ", "est le contraire d'habillé.", "est vitale.", "est le contraire de rapide.", "est un métal. ", "est l'inverse de la mort.", "est le liquide que nous donnent les vaches.", "est le contraire de laide.", "est un poisson.", "est une boisson.", "est une petite montagne.", "est le roi de la volaille. Très joli.", "est un habitant des cieux.", "est le contraire de tard"]
        #rep_deuxieme= ["eau", "sang", "nu", "eau", "lent", "fer", "vie", "Lait", "belle", "thon", "eau", "mont", "paon", "ange", "tôt "]
        mon_troisieme= ["est un jeu.", "est l'objet ou l'on dort.", "dirige les bateaux en mer la nuit.", "est garde les troupeaux.", "est le contraire de matin.", "est un célèbre canari que gros minet aimerait bien manger.", "est l'inverse de flou.","", "", "", "", "", "", "",""]
        #rep_troisieme=["dé", "lit", "phar", "pâtre", "soir", "titi", "nez", "", "", "", "", "", "", "",""]
        mon_quatrieme= ["est au milieu de la mer.", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        #rep_quatrieme=["ile", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        mon_tout= ["vit dans les fleuve d’Amazonie.", "est une fleur.", "est une fleur sur l'eau.", "est un(e) grand personnage historique !", "s’accroche aux branches des arbres.", "a été une reine d’Égypte.", "est ce que tu fais en pensant au tout.", "est bon quand il est rôti.", "est vide dans un camion", "est un bébé animal.", "est un tissus.", "est un poisson très bon.", "est un reptile venimeux.", "est un fruit délicieux.", "est un objet utile quand on fait le jardin."]
        rep_tout= ["crocodile", "pissenlit", "nenuphar", "cleopatre", "balancoire", "nefertiti", "devinette", "poulet", "poubelle", "chaton", "rideau", "saumon", "serpent", "orange", "rateau "]
        bg=pygame.image.load('background.jpg')
        #Input
        rep_user = ["","","",""]
        userInput = ""
        currentCharade = random.randint(0,14)
        score = 0
        correctVisible = False
        compteur = 0
        listIndexUsedCharade = []
        running = True
        running = True
        while running:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            running = False

                    if event.type == pygame.KEYDOWN and compteur == 4:
                        running = False
                    if event.type == pygame.KEYDOWN and compteur < 4:
                            if event.key == pygame.K_a:
                                    userInput = userInput + 'a'
                            if event.key == pygame.K_b:
                                    userInput = userInput + 'b'
                            if event.key == pygame.K_c:
                                    userInput = userInput + 'c'
                            if event.key == pygame.K_d:
                                    userInput = userInput + 'd'
                            if event.key == pygame.K_e:
                                    userInput = userInput + 'e'
                            if event.key == pygame.K_f:
                                    userInput = userInput + 'f'
                            if event.key == pygame.K_g:
                                    userInput = userInput + 'g'
                            if event.key == pygame.K_h:
                                    userInput = userInput + 'h'
                            if event.key == pygame.K_i:
                                    userInput = userInput + 'i'
                            if event.key == pygame.K_j:
                                    userInput = userInput + 'j'
                            if event.key == pygame.K_k:
                                    userInput = userInput + 'k'
                            if event.key == pygame.K_l:
                                    userInput = userInput + 'l'
                            if event.key == pygame.K_m:
                                    userInput = userInput + 'm'
                            if event.key == pygame.K_n:
                                    userInput = userInput + 'n'
                            if event.key == pygame.K_o:
                                    userInput = userInput + 'o'
                            if event.key == pygame.K_p:
                                    userInput = userInput + 'p'
                            if event.key == pygame.K_q:
                                    userInput = userInput + 'q'
                            if event.key == pygame.K_r:
                                    userInput = userInput + 'r'
                            if event.key == pygame.K_s:
                                    userInput = userInput + 's'
                            if event.key == pygame.K_t:
                                    userInput = userInput + 't'
                            if event.key == pygame.K_u:
                                    userInput = userInput + 'u'
                            if event.key == pygame.K_v:
                                    userInput = userInput + 'v'
                            if event.key == pygame.K_w:
                                    userInput = userInput + 'w'
                            if event.key == pygame.K_x:
                                    userInput = userInput + 'x'
                            if event.key == pygame.K_y:
                                    userInput = userInput + 'y'
                            if event.key == pygame.K_z:
                                    userInput = userInput + 'z'
                            if event.key == pygame.K_BACKSPACE:
                                    userInput = userInput[0:len(userInput)-1]
                            #reste a faire les autres lettre de aphabet, notemment accents
                            if event.key == pygame.K_SPACE:
                                    print(userInput)
                                    print(currentCharade)
                                    if userInput == rep_tout[currentCharade]:
                                            print('passed')
                                            score += 1
                                            compteur += 1
                                            currentCharade	 = random.randint(0,15)
                                            while (currentCharade  in listIndexUsedCharade):
                                                    currentCharade	= random.randint(0,15)
                                                    pass
                                            listIndexUsedCharade += [currentCharade]
                    
                                            userInput = ''
                                            correctVisible = False

                                    else:
                                            correctVisible = True

                                            #afficher msg bonne rep
                            
                                            #afficher msg mauv rep
            self.screen.blit(bg , (100,150))
            if ( compteur < 4): 
                    draw_text(self.screen,WHITE,'Mon premier ' + mon_premier[currentCharade],16,WIDTH/2 + 100,50+150)
                    draw_text(self.screen,WHITE,'Mon deuxieme ' + mon_deuxieme[currentCharade],16,WIDTH/2+100,80 + 150)
                    if mon_troisieme[currentCharade] != "": 
                            draw_text(self.screen,WHITE,'Mon troisieme ' + mon_troisieme[currentCharade],16,WIDTH/2+100,110+150)
                    if mon_quatrieme[currentCharade] != "":
                            draw_text(self.screen,WHITE,'Mon quatrieme ' + mon_quatrieme[currentCharade],16,WIDTH/2+100,140+150)
                    draw_text(self.screen,WHITE,'Mon tout ' + mon_tout[currentCharade],16,WIDTH/2+100,170+150)
                    draw_text(self.screen,BLUE,'Votre score est: ' + str(score),16,70+100,20+150)
                    draw_text(self.screen,RED,userInput,16,WIDTH/2+100,200+150)

                    if correctVisible:
                            draw_text(self.screen,WHITE,'Mauvaise reponse , ressayer' ,16,WIDTH/2+100,230+150)

            else:
                draw_text(self.screen,WHITE,'Vous avez tué le monstre.',16,WIDTH/2+100,80+150)
            pygame.display.update()


class miniGame3:
    def __init__(self,screen):
        self.screen = screen
        self.currentBackground = 0
        self.answer = random.choice(mots)
        self.zoneText=""
        self.temp1 = list(self.answer)
        self.zoneText ="_ "*len(self.temp1)
        self.usedLetters = ""
        self.step=0
        self.tries = 0

    def run(self):
        mots = ["pyramid","egyptian", "tomb","history","afterlife","mummy","symbol","god","ancient"]
        #mots=["god","dog","no"]
        #Colors
        RED = (255,0,0)
        BLACK = (0,0,0)

        #Loading images
        background = pygame.image.load("background.jpg").convert()
        backgrounds = [
                pygame.image.load("background1.jpg").convert(),
                pygame.image.load("try1.jpg").convert(),
                pygame.image.load("try2.jpg").convert(),
                pygame.image.load("try3.jpg").convert(),
                pygame.image.load("try4.jpg").convert(),
                pygame.image.load("gameover.jpg").convert(),
                

            ]
        cadre_zonetext= pygame.image.load("téléchargé.png").convert()
        currentBackground = 0
        
        def check_answer(letter):
            # resoudre le bug de plusieur occurence 
            self.tries=0
            if self.tries<4:
                if self.answer.find(letter)!= -1:#attention find retourne la premiere occurence
                    '''temp = list(zoneText)
                    index = 0
                    while index < len(answer):
                        index = answer.find(letter,index)
                        temp[index*2] = letter
                        index+=1
                    zoneText = ''.join(temp)'''
                    self.temp = list(self.zoneText)
                    self.temp1 = list(self.answer)
                    
                    
                    self.temp[self.answer.find(letter)*2] = letter
                    self.zoneText = ''.join(self.temp)
                    self.temp1[self.answer.find(letter)] = '*'
                    self.answer = ''.join(self.temp1)
                    
                else:
                    self.tries+=1
                    self.currentBackground +=1
                    if letter not in self.usedLetters:
                        self.usedLetters += letter
            

        running = True


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and self.step==3:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_c and self.currentBackground == 5):
                        self.currentBackground=0
                        self.answer = random.choice(mots)
                        self.zoneText=""
                        self.temp1 = list(self.answer)
                        self.zoneText ="_ "*len(self.temp1)
                        self.usedLetters = ""
                    
                    if self.currentBackground >= 1 and self.currentBackground < 5:
                        check_answer(pygame.key.name(event.key))
                        
                    if event.key == pygame.K_c:
                        if self.currentBackground == 0:
                            self.currentBackground +=1
            # SI le joueur depasse 3 try : game over screen
            #lui donner la possibilite de rejouer par une touche ou de quitter
            #mais il faut changer le mot
            # SI le joueur gagne AFFICHER message de victoire
            

            self.screen.blit(backgrounds[self.currentBackground],(100,100))
            if self.currentBackground == 0 and self.step==0:
                draw_text(self.screen,RED,'Welcome to Hangman!!',30,300+100,150+100)
                draw_text(self.screen,BLACK,'Press C to start the game!',30,300+100,200+100)
            if 0<self.currentBackground<=4:
                draw_text(self.screen,BLACK,self.zoneText,30,300+100,40+100)
                draw_text(self.screen,RED,self.usedLetters,25,300+100,360+100)
                self.screen.blit(cadre_zonetext,(178+100,40+100))
                self.screen.blit(cadre_zonetext,(178+100,349+100))
                
                #ajouter des cadres sur la zone de texte et sur les letters utilise
            if self.currentBackground==5:
                draw_text(self.screen,BLACK,'Press C to replay',30,300+100,150+100)
            
            if self.step==3:
                draw_text(self.screen,RED,'Vous avez tue le monstre.!',30,300+100,150+100)
                self.currentBackground=0
                
            compteur = 0
            answerList = list(self.answer)
            for i in range(len(answerList)):
                if answerList[i] == '*':
                    compteur+= 1

            if compteur == len(answerList):
                self.step+=1
                self.currentBackground=1
                draw_text(self.screen,BLACK,'Now you have to guess the next word.',30,300+100,150+100)
                self.answer = random.choice(mots)
                self.zoneText= ""
                self.temp1 = list(self.answer)
                self.zoneText ="_ "*len(self.temp1)
                self.usedLetters = ""

            
            pygame.display.update()
        
        
        
        
        
mots = ["pyramid","egyptian", "tomb","history","afterlife","mummy","symbol","god","ancient"]

        

    
