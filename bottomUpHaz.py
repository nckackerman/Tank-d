import pygame
import colors
import math
import player
import getSpawnCoordinates
import Lists
import constants


class bottomUpHaz(pygame.sprite.Sprite):

    def __init__(self,color,width,height,maxSpeed):
        # Call the parent class (Sprite) constructor

        pygame.sprite.Sprite.__init__(self)
        self.reced = False
        self.pauseTime = 10
        self.initialTime = pygame.time.get_ticks()
        self.image = pygame.Surface([width+40,height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)

        pygame.draw.rect(self.image,color,[0,10,width+40,height])
        knifeSpacing = -40
        while knifeSpacing < constants.screen_width+40:
            pygame.draw.polygon(self.image,colors.SOFT_RED,[[knifeSpacing+10,0],[knifeSpacing+20,10],[knifeSpacing,10]])
            knifeSpacing += 20

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = constants.screen_height+constants.menu_height

        self.xVel = -4.0
        self.yVel = 1.0

    def update(self):
        print 'size: ' + str(len(Lists.haz_list))
        if self.rect.y < constants.screen_height/2+constants.menu_height:
            if (pygame.time.get_ticks()-self.initialTime)/1000 > self.pauseTime:
                self.yVel = -1.0
                self.reced = True
            else:
                self.yVel = 0
        if self.rect.x < -20:
            self.rect.x = 0
        if self.reced:
            if self.rect.y > constants.screen_height + constants.menu_height:
                self.kill()
        # Move the bullet up 5 pixels
        self.rect.y -= self.yVel
        self.rect.x += self.xVel

def spawnBottomUpHaz(color):
    haz = bottomUpHaz(color, constants.screen_width, constants.screen_height, 1)

    Lists.haz_list.add(haz)
    Lists.all_sprites_list.add(haz)










