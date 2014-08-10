import pygame
import random
import colors
import Lists
import math
import getSpawnCoordinates
import constants

# This class represents the ball
# It derives from the "Sprite" class in Pygame

fourSquareHeight = 20
fourSquareWidth = 60

class fourSquare(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.LeftBoolean = False
        self.RightBoolean = False
        self.DownBoolean = False
        self.UpBoolean = False
        self.height = height
        self.width = width
        self.color = color

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)
        pygame.draw.polygon(self.image,color,[[0,0],[0,height-1]],2)
        pygame.draw.polygon(self.image,color,[[0,height-2],[width-2,height-2]],2)
        pygame.draw.polygon(self.image,color,[[width-2,height-2],[width-2,0]],2)
        pygame.draw.polygon(self.image,color,[[width-2,0],[0,0]],2)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.image = self.image.convert()

    def update(self):

        if not self.LeftBoolean:
            pygame.draw.polygon(self.image,self.color,[[0,0],[0,self.height-1]],2)
        else:
            pygame.draw.polygon(self.image,colors.SOFT_ORANGE,[[0,0],[0,self.height-1]],2)

        if not self.DownBoolean:
            pygame.draw.polygon(self.image,self.color,[[0,self.height-2],[self.width-2,self.height-2]],2)
        else:
            pygame.draw.polygon(self.image,colors.SOFT_ORANGE,[[0,self.height-2],[self.width-2,self.height-2]],2)

        if not self.RightBoolean:
            pygame.draw.polygon(self.image,self.color,[[self.width-2,self.height-2],[self.width-2,0]],2)
        else:
            pygame.draw.polygon(self.image,colors.SOFT_ORANGE,[[self.width-2,self.height-2],[self.width-2,0]],2)

        if not self.UpBoolean:
            pygame.draw.polygon(self.image,self.color,[[0,0],[self.width-2,0]],2)
        else:
            pygame.draw.polygon(self.image,colors.SOFT_ORANGE,[[0,0],[self.width-2,0]],2)



def spawnFourSquare(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyFourSquare = fourSquare(color, fourSquareWidth, fourSquareHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH, fourSquareWidth, fourSquareHeight)

        enemyFourSquare.rect.x = list[len(list)-2]
        enemyFourSquare.rect.y = list[len(list)-1]

        if constants.activeMode == 2:
            if color == colors.BLUE:
                Lists.blue_fourSquare_list.add(enemyFourSquare)
            else:
                Lists.red_fourSquare_list.add(enemyFourSquare)
        Lists.all_sprites_list.add(enemyFourSquare)
        Lists.fourSquare_list.add(enemyFourSquare)

def moveFourSquare():
    if constants.activeMode != 2:
        FourSquareMoveLogic(Lists.fourSquare_list,Lists.bullet_list)
    else:
        FourSquareMoveLogic(Lists.blue_fourSquare_list,Lists.red_bullet_list)
        FourSquareMoveLogic(Lists.red_fourSquare_list,Lists.blue_bullet_list)

    for player in Lists.player_list:
        fourSquare_hit_list = pygame.sprite.spritecollide(player, Lists.fourSquare_list, True, pygame.sprite.collide_rect_ratio(.75))
        for enemy in fourSquare_hit_list:
            if enemy.LeftBoolean and enemy.RightBoolean and enemy.UpBoolean and enemy.DownBoolean:
                constants.timeStop = True
                constants.firstTime = pygame.time.get_ticks()
            else:
                constants.game_over = True

def FourSquareMoveLogic(foursquareListType,bulletListType):
    for thisFourSquare in foursquareListType:
            for thisBullet in bulletListType:
                if thisBullet.rect.x >= thisFourSquare.rect.x+1 and thisBullet.rect.x <= 6 + thisFourSquare.rect.x and thisBullet.rect.y <= thisFourSquare.rect.y+thisFourSquare.height+2 and thisBullet.rect.y >= thisFourSquare.rect.y-1:
                    if (thisFourSquare.LeftBoolean):
                        thisBullet.xVel = math.fabs(thisBullet.xVel)
                    else:
                        thisFourSquare.LeftBoolean = True
                        thisBullet.kill()
                if thisBullet.rect.x <= thisFourSquare.rect.x+thisFourSquare.width-1 and thisBullet.rect.x>=thisFourSquare.width-6 + thisFourSquare.rect.x and thisBullet.rect.y <= thisFourSquare.rect.y+thisFourSquare.height+2 and thisBullet.rect.y >= thisFourSquare.rect.y-1:
                    if (thisFourSquare.RightBoolean):
                        thisBullet.xVel = -math.fabs(thisBullet.xVel)
                    else:
                        thisFourSquare.RightBoolean = True
                        thisBullet.kill()
                if thisBullet.rect.y <= thisFourSquare.rect.y-1 and thisBullet.rect.y >= thisFourSquare.rect.y-6 and thisBullet.rect.x <= thisFourSquare.rect.x+thisFourSquare.width+2 and thisBullet.rect.x >= thisFourSquare.rect.x-1:
                    if (thisFourSquare.UpBoolean):
                        thisBullet.yVel = math.fabs(thisBullet.yVel)
                    else:
                        thisFourSquare.UpBoolean = True
                        thisBullet.kill()
                if thisBullet.rect.y >= thisFourSquare.rect.y+thisFourSquare.height-6 and thisBullet.rect.y <= thisFourSquare.rect.y+thisFourSquare.height-1 and thisBullet.rect.x <= thisFourSquare.rect.x+thisFourSquare.width+2 and thisBullet.rect.x >= thisFourSquare.rect.x-1:
                    if (thisFourSquare.DownBoolean):
                        thisBullet.yVel = -math.fabs(thisBullet.yVel)
                    else:
                        thisFourSquare.DownBoolean = True
                        thisBullet.kill()







