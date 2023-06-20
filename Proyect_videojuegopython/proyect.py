import pygame, sys,random,time


pygame.init()#iniciar libreria



#definir colores en escala rgb
negro=(0,0,0)
blanco=(255,255,255)
verde=(0,255,0)
rojo=(255,0,0)
azul=(0,0,255)

size=(800,500) #establecer dimencsiones de ventana de 800 a 500

#crear ventana
screen= pygame.display.set_mode(size)
#crear reloj
clock=pygame.time.Clock()
#creacion de bucle de juego
coor_list=[]

#lluvia

for i in range(10):
        x=random.randint(0,800)
        y=random.randint(80,420)
        coor_list.append([x,y])
    


fondo=pygame.image.load("fond.jpg").convert()
fondopasto=pygame.image.load("fondopasto.jpg").convert()
fondofinal=pygame.image.load("ganar2.jpg").convert()
fondofinal2=pygame.image.load("ganar.png").convert()
fondofinal3=pygame.image.load("perdiste.jpg").convert()
fondofinal2.set_colorkey(blanco)



""""
barco=pygame.image.load("barco.png").convert()
alien=pygame.image.load("nave.png").convert()
misiil=pygame.image.load("misil.png").convert()
misiil.set_colorkey(blanco)
alien.set_colorkey(blanco)
bombaa=pygame.image.load("bomba.png").convert()
bombaa.set_colorkey(blanco)
barco.set_colorkey(blanco)"""





#creando clase misil
class Misil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("misil.png")
        self.image.set_colorkey(blanco)
        self.rect=self.image.get_rect()
#creando clase alien
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("nave.png")
        self.image.set_colorkey(blanco)
        self.rect=self.image.get_rect()

        

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bomba.png")
        self.image.set_colorkey(blanco)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y+=7
        
        if self.rect.y>450:
            self.rect.y=80

class Barco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("barco.png")
        self.image.set_colorkey(blanco)
        self.rect=self.image.get_rect()

all_sprite_list=pygame.sprite.Group()
bomb_list=pygame.sprite.Group()
coor_list2=[]
for i in range(2):
    
    bomb=Bomb()
    bomb.rect.y=80
    coor_list2.append(bomb)
    bomb_list.add(bomb)

barco=Barco()
alien=Alien()
misil=Misil()

alien_group= pygame.sprite.Group(alien)
alienybomb_group= pygame.sprite.Group(alien,bomb)
all_sprite_list.add(misil)
all_sprite_list.add(alien)
all_sprite_list.add(barco)





def gameLoop():
    perdiste=False
    Gameover=False
    Gameover2=False
    
    posx=0
    c=1
    misil.rect.y=450
    ataque=0
    choque_misilalien=False
    bombachoca=False
    contador=0
    pygame.mouse.set_visible(0)
    perdiste=False
    contadorfuente=pygame.font.Font(None,50)


    while not perdiste:
                      
                  
        while Gameover==True:
            screen.blit(fondofinal3,[0,0])
            pygame.display.update()
            for event in pygame.event.get(): 
                print(event)#registra eventos en consola
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_n:
                        pygame.quit()
                    if event.key==pygame.K_s:
                        gameLoop()
        while Gameover2==True:#gana
            screen.blit(fondofinal,[0,0])
            screen.blit(fondofinal2,[0,0])
            pygame.display.update()
            for event in pygame.event.get(): 
                print(event)#registra eventos en consola
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_n:
                        pygame.quit()
                    if event.key==pygame.K_s:
                        gameLoop()
        
        for event in pygame.event.get(): 
            print(event)#registra eventos en consola
            if event.type==pygame.QUIT:
                pygame.quit()#con estp ya podemos cerrar nuestra ventana de pygame
        
        
        ##movimiento de villan

        

        #establecer el color de fondo como azul
        screen.blit(fondo,[0,0])
        screen.blit(fondopasto,[0,420])
        if (posx>700):
            c=2

        elif(posx<3):
            c=1

        if(c==1):
            posx+=15
        else:
            posx-=15

        alien.rect.x=posx
        ###---zona de dibujo


        

    #nubes
        for i in range(100,600,230):
            pygame.draw.circle(screen,(blanco),(i,80),20)
            pygame.draw.circle(screen,(blanco),(i+20,80),20)
            pygame.draw.circle(screen,(blanco),(i+40,60),20)
            pygame.draw.circle(screen,(blanco),(i+20,60),20)
            pygame.draw.circle(screen,(blanco),(i+40,80),20)
            pygame.draw.circle(screen,(blanco),(i+60,80),20)
    #edificios

        for i in range (100,700,300):
            pygame.draw.rect(screen,(negro),(i+40,360,95,100))
        
        for i in range (200,700,300):
            pygame.draw.rect(screen,(negro),(i+40,160,95,300))

        for i in range (0,700,300):
            pygame.draw.rect(screen,(negro),(i+40,260,95,200))
        # ventanas     
        for i in range (200,700,300):
            for j in range(0,250,30):
                pygame.draw.rect(screen,(226, 255, 0),(i+95,170+j,25,15))
                pygame.draw.rect(screen,(226, 255, 0),(i+95,170+j,25,15))
                pygame.draw.rect(screen,(226, 255, 0),(i+45,170+j,25,15))
                pygame.draw.rect(screen,(226, 255, 0),(i+45,170+j,25,15))
        for i in range (100,700,300):
            for j in range(0,60,30):
                pygame.draw.rect(screen,(247, 255, 180),(i+95,385+j,25,15))
                pygame.draw.rect(screen,(247, 255, 180),(i+95,385+j,25,15))
                pygame.draw.rect(screen,(247, 255, 180),(i+45,385+j,25,15))
                pygame.draw.rect(screen,(247, 255, 180),(i+45,385+j,25,15))
        for i in range (0,700,300):
            for j in range(0,120,30):
                pygame.draw.rect(screen,(200, 200, 200),(i+95,290+j,25,15))
                pygame.draw.rect(screen,(200, 200, 200),(i+95,290+j,25,15))
                pygame.draw.rect(screen,(200, 200, 200),(i+45,290+j,25,15))
                pygame.draw.rect(screen,(200, 200, 200),(i+45,290+j,25,15))
            
        #lluvia
        for coord in coor_list:
            pygame.draw.circle(screen,azul,coord,3)
            coord[1]+=3
            if coord[1]>420:
                coord[1]=80


        #villano
        alien.rect.x=posx
        alien.rect.y=60

        #personaje
        posicionmouse=pygame.mouse.get_pos()

        barco.rect.x=posicionmouse[0]
        barco.rect.y=400

        #ataque
        b=0
        if(pygame.mouse.get_pressed()[0]==True and ataque==0):
            ataque=1
            misilx= barco.rect.x
        if(ataque==1):
            misil.rect.x=misilx
            misil.rect.y=misil.rect.y-9
            if (misil.rect.y<110):
                misil.rect.y=450
                ataque=0


        coor_list2[0].rect.x=posx+50
        coor_list2[0].rect.y=coor_list2[0].rect.y+2
        coor_list2[1].rect.x=posx+50



        if misil.rect.colliderect(alien):
            choque_misilalien=True
        
        if (choque_misilalien==True):
            Gameover2=True
            

        elif(choque_misilalien==False and bombachoca==False):
            if choque_misilalien==False:
                bomb_list.draw(screen)
            elif bombachoca==False:
                bomb_list.draw(screen)


        if ((barco.rect.colliderect(coor_list2[0]) or barco.rect.colliderect(coor_list2[1]))==True):
            bombachoca=True
            if contador==0:
                contador=1
            elif contador==2 and c==1:
                contador=3

            
            
            print (contador)
        elif((barco.rect.colliderect(coor_list2[0]) or barco.rect.colliderect(coor_list2[1]))==False and (posx<30 or posx>700)):
            bombachoca=False
            if contador==1:
                contador=2


        contadortexto=contadorfuente.render("vidas: "+str(3-contador),0,negro)
        screen.blit(contadortexto,(0,20))
            
        if contador>2:
            Gameover=True

        all_sprite_list.draw(screen)
        all_sprite_list.update()
        bomb_list.update()
        #fin zona de dibujo
        #actualizar pantalla
        pygame.display.flip()
        clock.tick(30)
gameLoop()
  
    
    
