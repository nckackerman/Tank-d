import pygame
import colors
import math
import player
import getSpawnCoordinates
import Lists
import constants
import deathCircle

fattyWidth = 40
fattyHeight = 40

class fatty(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        # Call the parent class (Sprite) constructor
        self.spawnTime = pygame.time.get_ticks()
        self.color = color
        self.rush = False
        self.health = 9
        self.width = width
        self.height = height
        font = pygame.font.SysFont("Arial", 10)
        healthText = font.render(str(self.health),True,colors.BLACK)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE)
        self.image.set_colorkey(colors.WHITE)
        self.image.blit(healthText, [16.5,13])

        pygame.draw.polygon(self.image,color,[[0,5*height/16.0],[0,11*height/16.0],[5*width/16.0,height-1],[11*width/16.0,height-1],[width-1,11*height/16.0],[width-1,5*height/16.0],[11*width/16.0,0],[5*width/16.0,0]],5)

        self.rect = self.image.get_rect()

        self.xVel = 0.0
        self.yVel = 0.0
        self.image = self.image.convert()


def spawnFatty(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyFatty = fatty(color, fattyWidth, fattyHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,fattyWidth,fattyHeight)

        enemyFatty.rect.x = list[len(list)-2]
        enemyFatty.rect.y = list[len(list)-1]


        if constants.activeMode == 2:
            if color == colors.BLUE:
                Lists.bluefatty_list.add(enemyFatty)
            else:
                Lists.redfatty_list.add(enemyFatty)
        Lists.all_sprites_list.add(enemyFatty)
        Lists.fatty_list.add(enemyFatty)

def moveFatty():
     #Behavior of fatties
    font = pygame.font.SysFont("Arial", 18)
    if constants.activeMode != 3:
        for thisFatty in Lists.fatty_list:
            if (pygame.time.get_ticks() - thisFatty.spawnTime)/1000 > 20:
                constants.game_over = True
            else:
                timeValue = (pygame.time.get_ticks()-thisFatty.spawnTime)/1000
                if timeValue > 9:
                    timeFlash = (pygame.time.get_ticks()-thisFatty.spawnTime)/500
                    if timeFlash % 2 == 0:
                        thisFatty.color = colors.SOFT_RED
                    else:
                        thisFatty.color = colors.BLACK
                timeText = font.render(str(timeValue),True,colors.BLACK)
                thisFatty.image.fill(colors.WHITE)
                pygame.draw.polygon(thisFatty.image,thisFatty.color,[[0,5*thisFatty.height/16.0],[0,11*thisFatty.height/16.0],[5*thisFatty.width/16.0,thisFatty.height-1],[11*thisFatty.width/16.0,thisFatty.height-1],[thisFatty.width-1,11*thisFatty.height/16.0],[thisFatty.width-1,5*thisFatty.height/16.0],[11*thisFatty.width/16.0,0],[5*thisFatty.width/16.0,0]],5)
                if timeValue < 10:
                    thisFatty.image.blit(timeText, [16.5,13])
                else:
                    thisFatty.image.blit(timeText, [11.5,13])

        moveFattyLogic(Lists.fatty_list,Lists.bullet_list)
    else:
        moveFattyLogic(Lists.bluefatty_list,Lists.red_bullet_list)
        moveFattyLogic(Lists.redfatty_list,Lists.blue_bullet_list)

def moveFattyLogic(fattyType, bulletType):

    for thisBullet in bulletType:
        bullet_hit_list = pygame.sprite.spritecollide(thisBullet, fattyType, False)
        for hit in bullet_hit_list:
            thisBullet.kill()
            hit.health -= 1
            if (hit.health == 0):
                constants.score+=10
                deathCircle.spawndeathCircle(1, colors.SOFT_ORANGE, hit.rect.x+15, hit.rect.y+20)
                hit.kill()



