import pygame, sys, os
from pygame.locals import *


#  klasa rozszerza klase Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, hp, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = hp
        self.toTargetImg = image
        self.speed=speed

    def update(self, neutralGroup):
        #  sterowanie(sprawdzanie czy został wciśniety klawisz aż do wykrycia jednego z nich)
        while True:
            if pygame.key.get_pressed()[pygame.K_UP] == 1:
                self.moveY(-self.speed, neutralGroup)
                self.rotate(90)
                break
            if pygame.key.get_pressed()[pygame.K_DOWN] == 1:
                self.moveY(self.speed, neutralGroup)
                self.rotate(-90)
                break
            if pygame.key.get_pressed()[pygame.K_RIGHT] == 1:
                self.moveX(self.speed, neutralGroup)
                self.rotate(0)
                break
            if pygame.key.get_pressed()[pygame.K_LEFT] == 1:
                self.moveX(-self.speed, neutralGroup)
                self.rotate(180)
                break
            else:
                break

    # obrót (Sprita)zarówno wyświetlanego obrazka jak i rectangla
    def rotate(self,angle):
        savedX = self.rect.x
        savedY = self.rect.y
        self.image = pygame.transform.rotate(self.toTargetImg, angle)
        self.rect = self.image.get_rect()
        self.rect.x = savedX
        self.rect.y = savedY

    # przesuwanie vertykalnie i sprawdzanie czy nastąpiła intersekcja z obiektami neutralnymi
    # jeśli tak to sprite jest przesuwany w przeciwnym kieruku o 1 pixel aż do ustąpienie intersekcji
    def moveX(self, amount, neutralGroup):
        self.rect.x += amount
        while pygame.sprite.spritecollide(self, neutralGroup, False):
            self.rect.x -= amount/abs(amount)

    # tak jak moveX tylko że hryzontalnie
    def moveY(self, amount, neutralGroup):
        self.rect.y += amount
        while pygame.sprite.spritecollide(self, neutralGroup, False):
            self.rect.y -= amount/abs(amount)


# blok cegieł
class NormalBricksBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


