import pygame
import random
import colors

# This class represents the ball
# It derives from the "Sprite" class in Pygame

blockHeight = 15
blockWidth = 20

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)

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
        self.image = self.image.convert()
        self.rect = self.image.get_rect()





