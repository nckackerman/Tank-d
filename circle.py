import pygame
import colors
import math
import player
import getSpawnCoordinates
import Lists
import constants

circleWidth = 15
circleHeight = 15
circleMaxSpeed = 1

class Circle(pygame.sprite.Sprite):

    def __init__(self,color,width,height,maxSpeed):
        # Call the parent class (Sprite) constructor
        self.maxSpeed = maxSpeed
        self.deltaTheta = 0.0

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)

        pygame.draw.ellipse(self.image,color,[0,0,width,height],2)

        self.rect = self.image.get_rect()

        self.xVel = 0.0
        self.yVel = 0.0
        self.image = self.image.convert()
    def update(self):


        # Move the bullet up 5 pixels
        self.rect.y -= self.yVel
        self.rect.x -= self.xVel

def spawnCircle(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyCircle = Circle(color, circleWidth, circleHeight, circleMaxSpeed)
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

def moveCircle():
    if pygame.time.get_ticks()%5 == 0:
        for player in Lists.player_list:
            for thisCircle in Lists.circle_list:
                modError = 0.6
                deltaX = thisCircle.rect.x - player.rect.x
                deltaY = thisCircle.rect.y - player.rect.y
                if deltaX < 5 and deltaX > -5:
                    deltaTheta = 2*math.pi
                elif deltaY < 5 and deltaY > -5:
                    deltaTheta = math.pi/2
                else:
                    deltaTheta = math.atan((math.fabs(deltaX))/(math.fabs(deltaY)))

                if player.rect.x > thisCircle.rect.x:
                    thisCircle.xVel = -thisCircle.maxSpeed*(math.sin(deltaTheta))
                    if ((thisCircle.xVel - modError) < -thisCircle.maxSpeed):
                        thisCircle.xVel = -thisCircle.maxSpeed
                else:
                    thisCircle.xVel = thisCircle.maxSpeed*(math.sin(deltaTheta))
                    if ((thisCircle.xVel - modError) < -thisCircle.maxSpeed):
                        thisCircle.xVel = -thisCircle.maxSpeed


                if player.rect.y > thisCircle.rect.y:
                    thisCircle.yVel = -thisCircle.maxSpeed*(math.cos(deltaTheta))
                    if ((thisCircle.yVel - modError) < -thisCircle.maxSpeed):
                        thisCircle.yVel = -thisCircle.maxSpeed
                else:
                    thisCircle.yVel = thisCircle.maxSpeed*(math.cos(deltaTheta))
                    if ((thisCircle.yVel + modError) > thisCircle.maxSpeed):
                        thisCircle.yVel = thisCircle.maxSpeed










