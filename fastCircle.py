import pygame
import colors
import math
import player
import getSpawnCoordinates
import Lists
import constants

circleWidth = 15
circleHeight = 15
circleMaxSpeed = 3

class fastCircle(pygame.sprite.Sprite):

    def __init__(self,color,width,height,maxSpeed):
        # Call the parent class (Sprite) constructor
        self.maxSpeed = maxSpeed
        self.deltaTheta = 0.0

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)

        pygame.draw.ellipse(self.image,color,[0,0,width,height],6)

        self.rect = self.image.get_rect()

        self.xVel = 0.0
        self.yVel = 0.0
        self.image = self.image.convert()

    def update(self):


        # Move the bullet up 5 pixels
        self.rect.y -= self.yVel
        self.rect.x -= self.xVel

def spawnfastCircle(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyCircle = fastCircle(color, circleWidth, circleHeight, circleMaxSpeed)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,circleWidth,circleHeight)

        enemyCircle.rect.x = list[len(list)-2]
        enemyCircle.rect.y = list[len(list)-1]

        if constants.activeMode != 2:
            Lists.Enemy_list.add(enemyCircle)
        else:
            if color == colors.BLUE:
                Lists.Blue_Enemy_list.add(enemyCircle)
            else:
                Lists.Red_Enemy_list.add(enemyCircle)
        Lists.all_sprites_list.add(enemyCircle)

        Lists.circle_list.add(enemyCircle)
