import pygame
import random
import constants
import colors
import Lists
import getSpawnCoordinates

# This class represents the ball
# It derives from the "Sprite" class in Pygame

triangleWidth = 20
triangleHeight = 12
triangleSpeed = 4
triangleThickness = 4

class triangleUD(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, maxSpeedx):
        # Call the parent class (Sprite) constructor
        self.maxSpeedx = maxSpeedx
        self.currentSpeedx = maxSpeedx
        self.changeY = 0
        self.color = color

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([triangleWidth, triangleHeight])
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)
        pygame.draw.polygon(self.image,self.color,[[-1,triangleHeight-2],[triangleWidth/2-1,0],[triangleWidth-1,triangleHeight-2]],triangleThickness)
        self.xConstant = 0
        self.yConstant = random.randrange(-1,1)
        if self.yConstant == 0:
            self.yConstant = 1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,self.color,[[-1,0],[triangleWidth/2,triangleHeight-1],[triangleWidth,0]],triangleThickness)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.image = self.image.convert()

    def update(self):

#         if self.rect.x >= constants.screen_width - triangleWidth:
#             self.xConstant = -1
#             self.image.fill(colors.WHITE)
#             pygame.draw.polygon(self.image,self.color,[[-1.5,triangleHeight/2],[triangleWidth-1.5,triangleHeight],[triangleWidth-1.5,0]],triangleThickness)
#         elif self.rect.x <= 0:
#             self.xConstant = 1
#             self.image.fill(colors.WHITE)
#             pygame.draw.polygon(self.image,self.color,[[triangleWidth-1,triangleHeight/2],[0,triangleHeight],[0,0]],triangleThickness)

        #these are to move only in the y plane
        if self.rect.y >= constants.screen_height+constants.menu_height:
            self.yConstant = -1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,self.color,[[-1,triangleHeight-2],[triangleWidth/2-1,0],[triangleWidth-1,triangleHeight-2]],triangleThickness)
        elif self.rect.y <= constants.menu_height:
            self.yConstant = 1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,self.color,[[-1,0],[triangleWidth/2,triangleHeight-1],[triangleWidth,0]],triangleThickness)

        if self.rect.y < constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.8
        elif self.rect.y <= 2*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.5
        elif self.rect.y <= 3*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.2
        elif self.rect.y <=5*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx
        elif self.rect.y <= 6*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.2
        elif self.rect.y <= 7*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.5
        elif self.rect.y > 7*constants.screen_height/8+constants.menu_height:
            self.currentSpeedy = self.maxSpeedx/1.8

        self.rect.x += ((self.currentSpeedx) * self.xConstant)
        self.rect.y += ((self.currentSpeedy) * self.yConstant)

def spawnTriangleUD(spawnCount,playerX,playerY,playerW,playerH,triangleMaxSpeed,color):
    # creates triangle enemies
    for i in range(spawnCount):
        triangle_enemy = triangleUD(color, triangleMaxSpeed)

        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,triangleWidth,triangleHeight)
        triangle_enemy.rect.x = list[len(list)-2]
        triangle_enemy.rect.y = list[len(list)-1]

        if constants.activeMode != 2:
            Lists.Enemy_list.add(triangle_enemy)
        else:
            if color == colors.BLUE:
                Lists.Blue_Enemy_list.add(triangle_enemy)
            else:
                Lists.Red_Enemy_list.add(triangle_enemy)
        Lists.all_sprites_list.add(triangle_enemy)
        Lists.triangle_list.add(triangle_enemy)






