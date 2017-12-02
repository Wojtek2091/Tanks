import pygame, sys, os
from pygame.locals import *


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# klasa po której dziedzicą wszystkie tanki
class Tank(GameObject):
    bulletSpeed = 350

    def __init__(self, x, y, image, hp, speed, bulletImg):
        super().__init__(x,y,image)
        self.hp = hp
        self.toTargetImg = image
        self.speed=speed
        self.direction = 'right'
        self.bulletImg = bulletImg

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

    def shoot(self, handler):
        if self.direction == 'up':
            x = self.rect.x + self.image.get_width()/2 -self.bulletImg.get_width()/2
            y = self.rect.y
            handler.addBullet(Bullet(x, y, self.bulletImg, 0, -self.bulletSpeed))
        elif self.direction == 'down':
            x = self.rect.x + self.image.get_width()/2 -self.bulletImg.get_width()/2
            y = self.rect.y + self.image.get_height()
            handler.addBullet(Bullet(x, y, self.bulletImg, 0, self.bulletSpeed))
        elif self.direction == 'right':
            x = self.rect.x + self.image.get_width()
            y = self.rect.y + self.image.get_height()/2 - self.bulletImg.get_height()/2
            handler.addBullet(Bullet(x, y,self.bulletImg, self.bulletSpeed, 0))
        elif self.direction == 'left':
            x = self.rect.x
            y = self.rect.y + self.image.get_height()/2 - self.bulletImg.get_height()/2
            handler.addBullet(Bullet(x, y,self.bulletImg, -self.bulletSpeed, 0))


#  klasa rozszerza klase tank
class Player(Tank):
    bulletSpeed = 0

    def __init__(self, x, y, image, hp, speed, bulletImg, delay):
        super().__init__(x, y, image, hp, speed, bulletImg)
        self.delay = delay

    def update(self, handler, neutralGroup):
        #  sterowanie(sprawdzanie czy został wciśniety klawisz aż do wykrycia jednego z nich)
        while True:
            if pygame.key.get_pressed()[pygame.K_UP] == 1:
                self.moveY(-self.speed, neutralGroup)
                self.rotate(90)
                self.direction = 'up'
                break
            if pygame.key.get_pressed()[pygame.K_DOWN] == 1:
                self.moveY(self.speed, neutralGroup)
                self.rotate(-90)
                self.direction = 'down'
                break
            if pygame.key.get_pressed()[pygame.K_RIGHT] == 1:
                self.moveX(self.speed, neutralGroup)
                self.rotate(0)
                self.direction = 'right'
                break
            if pygame.key.get_pressed()[pygame.K_LEFT] == 1:
                self.moveX(-self.speed, neutralGroup)
                self.rotate(180)
                self.direction = 'left'
                break
            else:
                break
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.delay <= 0:
                self.shoot(handler)
                self.delay = 25
        self.delay -= 1

# pocisk
class Bullet(GameObject):
    def __init__(self, x, y, image, velocityX, velocityY):
        super().__init__(x, y, image)
        self.velocityX = velocityX
        self.velocityY = velocityY

    def update(self):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY


# blok cegieł
class NormalBricksBlock(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x,y,image)

    def update(self, bulletGroup, ownGroup):
        if pygame.sprite.spritecollide(self, bulletGroup, True):
            ownGroup.remove(self)



