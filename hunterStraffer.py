import block
import pygame
import random
import constants
import getSpawnCoordinates
import Lists
import colors

strafferWidth = 10
strafferHeight = 10
strafferThickness = 5

class hunterStraffer(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.strafferTimer = 0
        self.strafferRadius = 9
        self.maxSpeed = 1
        self.deltaTheta = 0.0

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE)

        pygame.draw.rect(self.image,color,[0,0,strafferWidth,strafferHeight],strafferThickness)

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
        self.yVel = 0
        self.xVel = 0

    def update(self):

        self.rect.y -= self.yVel
        self.rect.x -= self.xVel


def spawnHunterStraffer(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyStraffer = hunterStraffer(color, strafferWidth, strafferHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,strafferWidth,strafferHeight)

        enemyStraffer.rect.x = list[len(list)-2]
        enemyStraffer.rect.y = list[len(list)-1]

        # Add the block to the list of objects
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
        # add to the circle list to get the hunt behavior
        Lists.circle_list.add(enemyStraffer)

def moveHunterStraffer():
    if constants.activeMode != 2:
        moveHunterStrafferLogic(Lists.straffer_list,Lists.bullet_list)
    else:
        moveHunterStrafferLogic(Lists.bluestraffer_list,Lists.red_bullet_list)
        moveHunterStrafferLogic(Lists.redstraffer_list,Lists.blue_bullet_list)

def moveHunterStrafferLogic(strafferType,bulletType):
    strafferRadius = 9
    strafferPadding = 50
    for thisStraffer in strafferType:
        for thisbullet in bulletType:
            rangeXtop = thisbullet.rect.x + strafferRadius
            rangeXbottom = thisbullet.rect.x - (strafferRadius + 20)
            rangeYtop = thisbullet.rect.y + strafferRadius
            rangeYbottom = thisbullet.rect.y - (strafferRadius + 20)

            if (thisbullet.rect.x <= thisStraffer.rect.x):
                strafferX_Direction = 1
            else:
                strafferX_Direction = -1

            if (thisbullet.rect.y <= thisStraffer.rect.y):
                strafferY_Direction = 1
            else:
                strafferY_Direction = -1


            if thisStraffer.rect.x <= rangeXtop and thisStraffer.rect.x >= rangeXbottom and thisStraffer.rect.y <= rangeYtop and thisStraffer.rect.y >= rangeYbottom:
                if (thisStraffer.strafferTimer <5):
                    thisStraffer.strafferTimer += 1
                elif (thisStraffer.strafferTimer >=0):
                    thisStraffer.strafferTimer = 10
                    if thisStraffer.rect.y < rangeYtop and thisStraffer.rect.y > rangeYbottom:
                        if (thisStraffer.strafferTimer == 10):
                            if ((thisStraffer.rect.y + strafferPadding) < constants.screen_height+constants.menu_height and (thisStraffer.rect.y - strafferPadding) > 0):
                                thisStraffer.rect.y += 6*strafferY_Direction
                                thisStraffer.strafferTimer = 0

                            if ((thisStraffer.rect.x + strafferPadding) < constants.screen_width and (thisStraffer.rect.x - strafferPadding) > 0):
                                thisStraffer.rect.x += 6*strafferX_Direction
                                thisStraffer.strafferTimer = 0
