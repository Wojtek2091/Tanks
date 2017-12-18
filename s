def buildMap(toParse, BLOCKSIZE, WIDTH, HEIGHT):
    x = 0
    y = 0
    neutralGroup = pygame.sprite.Group([])
    bricksImg = pygame.image.load('Sprites/bricks.png')
    for ch in toParse:
        if ch == "X":
            neutralGroup.add(NormalBricksBlock(x, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y, bricksImg))
            neutralGroup.add(NormalBricksBlock(x, y + 25, bricksImg))
            neutralGroup.add(NormalBricksBlock(x + 25, y + 25, bricksImg))
    if (x + BLOCKSIZE)>WIDTH:
        y += BLOCKSIZE
    else:
        x += BLOCKSIZE
    return neutralGroup


class Boom (GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, 1)
        self.img1 = pygame.image.load('Sprites/boom1.png')
        self.img2 = pygame.image.load('Sprites/boom2.png')
        self.img3 = pygame.image.load('Sprites/boom3.png')
        self.img4 = pygame.image.load('Sprites/boom4.png')
        self.img5 = pygame.image.load('Sprites/boom5.png')
        self.img6 = pygame.image.load('Sprites/boom6.png')
        self.img7 = pygame.image.load('Sprites/boom7.png')
        self.timer = 0

    def update(self, groupsList):
        for i in range(0, 3):
            for gameObject in pygame.sprite.spritecollide(self, groupsList[i], False):
                if gameObject.decreaseHp(1) <= 0:
                    groupsList[i].remove(gameObject)
        if self.timer >= 0 and self.timer < 3:
            self.image = self.img1
        elif self.timer >= 3 and self.timer < 6:
            self.image = self.img2
        elif self.timer >= 6 and self.timer < 9:
            self.image = self.img3
        elif self.timer >= 9 and self.timer < 12:
            self.image = self.img4
        elif self.timer >= 12 and self.timer < 15:
            self.image = self.img5
        elif self.timer >= 15 and self.timer < 20:
            self.image = self.img6
        elif self.timer >= 20 and self.timer < 25:
            self.image = self.img7
        else:
            groupsList[4].remove(self)
        self.timer += 1
