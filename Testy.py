import pygame, sys
from pygame.locals import *

class Tank:
    def __init(self,x,y,hp,dmg,speed,img):
        self.x=x
        self.y=y
        self.hp=hp
        self.dmg=dmg
        self.speed=speed
    def update(self):
        pass
    def render(self):
        return self.img, (self.x,self.y)           
    
    
'''objectHandler służy do wywoływania funkcji renderujących i update-ujących wszystkihc obiektów na planszy w każdej klatce'''

class ObjectHandler:
    #Handler pobiera liste wszystkich obiektów na planszy
    def __init__(self,display,gameObjectList=[]):
        self.gameObjectList=gameObjectList
        self.display=display
    #Metoda update updatuje wszystkie obiekty iterując po każdym el listy obiektów wywołując ich funkcje update  
    def update(self):
        pass
    #Metoda render updatuje wszystkie obiekty podobnie jak update
    def render(self):
        for object in self.gameObjectList:
            self.display.blit(object.render)
        return self.display
        

WIDTH=1280
HEIGHT=720
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
tank1=Tank(50,50,100,2,2,pygame.image.load('tank1.png'))
handler=ObjectHandler(DISPLAYSURF,{})
pygame.display.set_caption('Hello World!')
while True: # main game loop
    DISPLAYSURF=handler.render
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()