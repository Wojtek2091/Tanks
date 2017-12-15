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
