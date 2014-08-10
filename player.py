import pygame
import constants
import Lists

playerHeight = 15
playerWidth = 15

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    def __init__(self,color,x,y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([playerWidth, playerHeight])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.image.convert()

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def getChangeX(self):
        global change_x
        return self.change_x

    def getChangeY(self):
        global change_y
        return self.change_y

    def setXY(self,X,Y):
        self.rect.x = X
        self.rect.y = Y

    def setSpeed(self,deltX,deltaY):
        self.change_x = deltX
        self.change_y = deltaY

    def changespeed(self,deltX,deltaY):
        self.change_x += deltX
        self.change_y += deltaY

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x > constants.screen_width:
            self.rect.x = 0
        elif self.rect.x < -playerWidth/2:
            self.rect.x = constants.screen_width
        self.rect.y += self.change_y
        if self.rect.y > constants.screen_height + constants.menu_height:
            self.rect.y = constants.menu_height
        elif self.rect.y < -playerHeight/2 + constants.menu_height:
            self.rect.y = constants.menu_height + constants.screen_height





