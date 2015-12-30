import pygame
import random
import constants
import colors
import Lists
import getSpawnCoordinates

# This class represents the ball
# It derives from the "Sprite" class in Pygame

triangleHeight = 20
triangleWidth = 12
triangleSpeed = 4
triangleThickness = 4

class triangle(pygame.sprite.Sprite):

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
        pygame.draw.polygon(self.image,color,[[-1,triangleHeight/2],[triangleWidth-2,triangleHeight-1],[triangleWidth-2,0]],triangleThickness)

        self.xConstant = random.randrange(-1,1)
        if self.xConstant == 0:
            self.xConstant = 1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,color,[[triangleWidth-1,triangleHeight/2],[0,triangleHeight],[0,0]],triangleThickness)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.image = self.image.convert()

    def update(self):

        if self.rect.x >= constants.screen_width - triangleWidth:
            self.xConstant = -1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,self.color,[[-1.5,triangleHeight/2],[triangleWidth-1.5,triangleHeight],[triangleWidth-1.5,0]],triangleThickness)
        elif self.rect.x <= 0:
            self.xConstant = 1
            self.image.fill(colors.WHITE)
            pygame.draw.polygon(self.image,self.color,[[triangleWidth-1,triangleHeight/2],[0,triangleHeight],[0,0]],triangleThickness)

        #these are to move only in the y plane
        self.yConstant = 0
        if self.rect.y >= constants.screen_height+constants.menu_height:
            self.yConstant = -1
        elif self.rect.y <= constants.menu_height:
            self.yConstant = 1

        if self.rect.x < constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.8
        elif self.rect.x <= 2*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.5
        elif self.rect.x <= 3*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.2
        elif self.rect.x <=5*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx
        elif self.rect.x <= 6*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.2
        elif self.rect.x <= 7*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.5
        elif self.rect.x > 7*constants.screen_width/8:
            self.currentSpeedx = self.maxSpeedx/1.8

        self.rect.x += ((self.currentSpeedx) * self.xConstant)
        self.rect.y += ((self.changeY) * self.yConstant)

def spawnTriangle(spawnCount,playerX,playerY,playerW,playerH,triangleMaxSpeed,color):
    # creates triangle enemies
    for i in range(spawnCount):
        triangle_enemy = triangle(color, triangleMaxSpeed)

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






