import pygame
import colors

class diagnolbullet(pygame.sprite.Sprite):

    def __init__(self,color,width,height,xVel,yVel):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height]).convert()
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)

        # Draw the ellipse
        pygame.draw.polygon(self.image,color,[[0,0],[8,-8],[9,-8],[1,0]],5)

        self.rect = self.image.get_rect()
        self.xVel = xVel
        self.yVel = yVel

    def update(self):

        # Move the bullet up 5 pixels
        self.rect.y -= self.yVel
        self.rect.x -= self.xVel