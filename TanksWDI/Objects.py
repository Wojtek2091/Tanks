import pygame, sys, os
from pygame.locals import *
import random


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, hp):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = hp

    # Sprawdza czy obiekt nie jest poza mapa
    def hasGoodPos(self):
        if self.rect.x < 0 or self.rect.y <  0 or self.rect.x > 1300-self.image.get_width() or self.rect.y > 700-self.image.get_height():
            return False
        else:
            return True

    def decreaseHp(self,amount):
        self.hp -= amount
        return self.hp

# klasa po której dziedzicą wszystkie tanki
class Tank(GameObject):
    bulletSpeed = 20

    def __init__(self, x, y, image, hp, speed, bulletImg):
        super().__init__(x,y,image, hp)
        self.toTargetImg = image
        self.speed = speed
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

    # przesuwanie vertykalnie i sprawdzanie czy nastąpiła intersekcja z innymi obiektami nawet ze swojej sprite grupy
    # jeśli tak to sprite jest przesuwany w przeciwnym kieruku o 1 pixel aż do ustąpienie intersekcji
    # Ponadto sprawdzamy czy obiekt ma goodpos
    #
    def moveX(self, amount, groupsList):
        isIn = False
        self.rect.x += amount
        for i in range(0, 4):
            if self in groupsList[i].sprites():
                groupsList[i].remove(self)
                isIn = True
            while pygame.sprite.spritecollide(self, groupsList[i], False) or not self.hasGoodPos():
                self.rect.x -= amount/abs(amount)
            if isIn:
                groupsList[i].add(self)
                isIn = False

    # tak jak moveX tylko że hryzontalnie
    def moveY(self, amount, groupsList):
        isIn = False
        self.rect.y += amount
        for i in range(0, 4):
            if self in groupsList[i].sprites():
                groupsList[i].remove(self)
                isIn = True
            while pygame.sprite.spritecollide(self, groupsList[i], False) or not self.hasGoodPos():
                self.rect.y -= amount/abs(amount)
            if isIn:
               groupsList[i].add(self)
               isIn = False

    def moveUp(self, groupsList):
        self.moveY(-self.speed, groupsList)
        self.rotate(90)
        self.direction = 'up'

    def moveDown(self, groupsList):
        self.moveY(self.speed, groupsList)
        self.rotate(-90)
        self.direction = 'down'                                         # metody do poruszania sie czołgu/czołgiem

    def moveRight(self, groupsList):
        self.moveX(self.speed, groupsList)
        self.rotate(0)
        self.direction = 'right'

    def moveLeft(self, groupsList):
        self.moveX(-self.speed, groupsList)
        self.rotate(180)
        self.direction = 'left'

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
    bulletSpeed = 20

    def __init__(self, x, y, image, hp, speed, bulletImg, delay):
        super().__init__(x, y, image, hp, speed, bulletImg)
        self.delay = delay

    def update(self, handler, groupsList):
        #  sterowanie(sprawdzanie czy został wciśniety klawisz aż do wykrycia jednego z nich)
        while True:
            if pygame.key.get_pressed()[pygame.K_UP] == 1:
                self.moveUp(groupsList)
                break
            if pygame.key.get_pressed()[pygame.K_DOWN] == 1:
                self.moveDown(groupsList)
                break
            if pygame.key.get_pressed()[pygame.K_RIGHT] == 1:
                self.moveRight(groupsList)
                break
            if pygame.key.get_pressed()[pygame.K_LEFT] == 1:
                self.moveLeft(groupsList)
                break
            else:
                break
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.delay <= 0:
                self.shoot(handler)
                self.delay = 25
        self.delay -= 1


class Enemy(Tank):
    def __init__(self, x, y, image, hp, speed, bulletImg, delay):
        super().__init__(x, y, image, hp, speed, bulletImg)
        self.delay = delay

    def trace(self, player, groupsList, handler):
        shooted = False
        player = player.sprites()[0]
        diffX = self.rect.x - player.rect.x
        diffY = self.rect.y - player.rect.y
        if abs(diffX) >= abs(diffY) and (abs(diffY) - self.speed) > 0:
            if diffY >= 0:
                self.moveUp(groupsList)
            else:
                self.moveDown(groupsList)
        elif (abs(diffX) - self.speed) > 0:
            if diffX >= 0:
                self.moveLeft(groupsList)
            else:
                self.moveRight(groupsList)
        else:
            if diffY > 0:
                self.moveUp(groupsList)
            elif diffY < 0:
                self.moveDown(groupsList)

        if ((abs(diffX) - self.speed -3) < 0) or ((abs(diffY) - self.speed -3) < 0):
            if self.delay <= 0:
                self.shoot(handler)
                self.delay = 45
        self.delay -= 1

        if shooted:
            return "shoot"
        else:
            return "move"

    def update(self, handler, groupsList):
        currX = self.rect.x
        currY = self.rect.y
        if self.trace(groupsList[0], groupsList, handler) == "move":
            if ((self.rect.x - currX) == 0) and ((self.rect.y - currY) == 0) and self.delay <= 0:
                self.shoot(handler)
                self.delay = 45





# pocisk
class Bullet(GameObject):
    boomImage = pygame.image.load('Sprites/boom.png')
    def __init__(self, x, y, image, velocityX, velocityY):
        super().__init__(x, y, image,1)
        self.velocityX = velocityX
        self.velocityY = velocityY

    def update(self, groupsList):
        self.rect.x += self.velocityX
        self.rect.y += self.velocityY
        if not self.hasGoodPos():
            groupsList[3].remove(self)
        for i in range(0,3):
            if pygame.sprite.spritecollide(self, groupsList[i], False):  # Jeśli w coś uderzy to tworzy wybuch - boom
                groupsList[4].add(Boom(self.rect.x - 3, self.rect.y -3, self.boomImage,))
                groupsList[3].remove(self)


# Zmniejsza hp obiektów w swoim zasiegu
class Boom (GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, 1)

    def update(self, groupsList):
        for i in range(0, 3):
            for gameObject in pygame.sprite.spritecollide(self, groupsList[i], False):
                if gameObject.decreaseHp(1) <= 0:
                    groupsList[i].remove(gameObject)
        groupsList[4].remove(self)


# blok cegieł
class NormalBricksBlock(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x,y,image, 1)




