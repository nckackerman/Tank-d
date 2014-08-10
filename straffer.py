import block
import pygame
import random
import constants
import getSpawnCoordinates
import Lists
import colors

strafferWidth = 10
strafferHeight = 10
strafferTimer = 0
strafferRadius = 3

class straffer(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.strafferTimer = 0
        self.strafferRadius = 3

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE)

        pygame.draw.polygon(self.image,color,[[0,0],[0,height]],2)
        pygame.draw.polygon(self.image,color,[[0,height-2],[width,height-2]],2)
        pygame.draw.polygon(self.image,color,[[width-2,height],[width-2,0]],2)
        pygame.draw.polygon(self.image,color,[[width,0],[0,0]],2)

        self.xConstant = random.randrange(-1,1)
        if self.xConstant == 0:
            self.xConstant = 1
        self.yConstant = random.randrange(-1,1)
        if self.yConstant == 0:
            self.yConstant = 1

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.image = self.image.convert()

    def update(self):

        changeX = random.randrange(0,3)
        changeY = random.randrange(0,3)

        if self.rect.x >= constants.screen_width - strafferWidth+2:
            self.xConstant = -1
        elif self.rect.x <= 0:
            self.xConstant = 1

        if self.rect.y >= constants.screen_height+constants.menu_height - strafferHeight+2:
            self.yConstant = -1
        elif self.rect.y <= constants.menu_height:
            self.yConstant = 1

        self.rect.x += ((changeX) * self.xConstant)
        self.rect.y += ((changeY) * self.yConstant)


def spawnStraffer(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyStraffer = straffer(color, strafferWidth, strafferHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,strafferWidth,strafferHeight)

        enemyStraffer.rect.x = list[len(list)-2]
        enemyStraffer.rect.y = list[len(list)-1]


        if constants.activeMode == 2:
            if color == colors.BLUE:
                Lists.bluestraffer_list.add(enemyStraffer)
                Lists.Blue_Enemy_list.add(enemyStraffer)
            else:
                Lists.redstraffer_list.add(enemyStraffer)
                Lists.Red_Enemy_list.add(enemyStraffer)

        Lists.straffer_list.add(enemyStraffer)
        Lists.all_sprites_list.add(enemyStraffer)
        Lists.Enemy_list.add(enemyStraffer)

def moveStraffer():
    if constants.activeMode == 0:
        moveStrafferLogic(Lists.straffer_list,Lists.bullet_list)
    else:
        moveStrafferLogic(Lists.bluestraffer_list,Lists.red_bullet_list)
        moveStrafferLogic(Lists.redstraffer_list,Lists.blue_bullet_list)

def moveStrafferLogic(strafferType,bulletType):
    strafferRadius = 25
    strafferPadding = 50
    for thisStraffer in strafferType:
        for thisbullet in bulletType:
            rangeXtop = thisbullet.rect.x + strafferRadius
            rangeXbottom = thisbullet.rect.x - (strafferRadius)
            rangeYtop = thisbullet.rect.y + strafferRadius
            rangeYbottom = thisbullet.rect.y - (strafferRadius)

            if (thisbullet.rect.x <= thisStraffer.rect.x):
                strafferX_Direction = 1
            else:
                strafferX_Direction = -1

            if (thisbullet.rect.y <= thisStraffer.rect.y):
                strafferY_Direction = 1
            else:
                strafferY_Direction = -1


            if thisStraffer.rect.x <= rangeXtop and thisStraffer.rect.x >= rangeXbottom and thisStraffer.rect.y <= rangeYtop and thisStraffer.rect.y >= rangeYbottom:
                if (thisStraffer.strafferTimer <6):
                    thisStraffer.strafferTimer += 1
                    break
                elif (thisStraffer.strafferTimer >=0):
                    thisStraffer.strafferTimer = 10
                    if thisStraffer.rect.y < rangeYtop and thisStraffer.rect.y > rangeYbottom:
                        if (thisStraffer.strafferTimer == 10):
                            if ((thisStraffer.rect.y + strafferPadding) < constants.screen_height+constants.menu_height and (thisStraffer.rect.y - strafferPadding) > 0):
                                thisStraffer.rect.y += 7*strafferY_Direction
                                thisStraffer.strafferTimer = 0

                            if ((thisStraffer.rect.x + strafferPadding) < constants.screen_width and (thisStraffer.rect.x - strafferPadding) > 0):
                                thisStraffer.rect.x += 7*strafferX_Direction
                                thisStraffer.strafferTimer = 0
