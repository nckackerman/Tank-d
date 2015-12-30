import pygame
import colors
import math
import player
import getSpawnCoordinates
import bottomUpHaz
import Lists
import constants


class bottomUpCountDown(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        # Call the parent class (Sprite) constructor

        pygame.sprite.Sprite.__init__(self)
        self.reced = False
        self.pauseTime = 20
        self.initialTime = pygame.time.get_ticks()
        self.image = pygame.Surface([width,height])
        self.image.fill(colors.BLUE)
        self.image.set_colorkey(colors.WHITE)
        self.image.convert()
        self.width = width
        self.height = height

        pygame.draw.rect(self.image, colors.SOFT_RED, [self.width/2-constants.hazArrowWidth/2, 20,constants.hazArrowWidth,self.height])
        pygame.draw.polygon(self.image, colors.SOFT_RED, [[constants.hazArrowPointerWidth/2,0],[0,20],[self.width,20]])

        self.rect = self.image.get_rect()
        self.rect.x = (constants.screen_width - constants.hazArrowWidth - self.width)/2
        self.rect.y = constants.screen_height+constants.menu_height - constants.hazArrowOffset - self.height

    def update(self):

        if (pygame.time.get_ticks() - self.initialTime)/500 == 1 or (pygame.time.get_ticks() - self.initialTime)/500 == 3 or (pygame.time.get_ticks() - self.initialTime)/500 == 5 or (pygame.time.get_ticks() - self.initialTime)/500 == 7:
            self.image.fill(colors.WHITE)
            self.image.set_colorkey(colors.WHITE)
            self.image.convert()
        elif (pygame.time.get_ticks() - self.initialTime)/500 == 2 or (pygame.time.get_ticks() - self.initialTime)/500 == 4 or (pygame.time.get_ticks() - self.initialTime)/500 == 6 or (pygame.time.get_ticks() - self.initialTime)/500 == 8:
            pygame.draw.rect(self.image, colors.SOFT_RED, [self.width/2-constants.hazArrowWidth/2, 20,constants.hazArrowWidth,self.height])
            pygame.draw.polygon(self.image, colors.SOFT_RED, [[constants.hazArrowPointerWidth/2,0],[0,20],[self.width,20]])
            self.image.convert()
        elif (pygame.time.get_ticks() - self.initialTime)/500 == 9:
            self.kill()
            print 'here'
            bottomUpHaz.spawnBottomUpHaz(colors.SOFT_RED)

def spawnbottomUpCountDown(color):
    haz = bottomUpCountDown(color, constants.hazArrowPointerWidth, 60)

    Lists.haz_list.add(haz)
    Lists.all_sprites_list.add(haz)










