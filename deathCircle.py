import pygame
import colors
import math
import player
import getSpawnCoordinates
import Lists
import constants

width = 125
height = 125

class deathCircle(pygame.sprite.Sprite):

    def __init__(self,color,X,Y):
        # Call the parent class (Sprite) constructor
        self.currspred = 5
        self.color = color
        self.x = 0
        self.y = 0

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.currspred,self.currspred])
        pygame.draw.rect(self.image,color,[self.x,self.y,self.currspred,self.currspred])

        self.rect = self.image.get_rect()
        self.x2 = X
        self.y2 = Y

        self.wait = True

        self.xVel = 0.0
        self.yVel = 0.0
        self.image = self.image.convert()

    def update(self):
        if self.wait:
            self.wait = False
        else:
            self.x2 -= 1
            self.y2 -= 1
            self.wait = True
        if self.currspred < height:
            self.currspred += 1
            self.image = pygame.Surface([self.currspred,self.currspred])
            self.rect = self.image.get_rect()
            self.rect.x = self.x2
            self.rect.y = self.y2
            pygame.draw.rect(self.image,self.color,[self.x,self.y,self.currspred,self.currspred])
            self.image.convert()
        else:
            self.kill()

def spawndeathCircle(spawnCount,color,x,y):
    for i in range(spawnCount):
        enemyCircle = deathCircle(color, x, y)

        enemyCircle.rect.x = x
        enemyCircle.rect.y = y

        Lists.deathCircle_list.add(enemyCircle)
