import pygame
import Lists
import constants
import colors
import player
import math
import pointGains

bulletWidth = 3
bulletHeight = 8
straightSpeed = 5
diagonalBulletSpeed = 3.5
shotDir = 0

class bullet(pygame.sprite.Sprite):

    def __init__(self,width,height,xVel,yVel,color,posX,posY):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.xVel = xVel
        self.yVel = yVel
        self.image = self.image.convert()
        self.initX = posX
        self.initY = posY
    def update(self):

        # Move the bullet up 5 pixels
        self.rect.y -= self.yVel
        self.rect.x -= self.xVel

def spawnBullets(xSpeed,ySpeed,posX,posY):
    if constants.activeMode != 2 or constants.playerColor == 0:
        color = colors.BLUE
    else:
        color = colors.RED
    if xSpeed == 0:
        #leftbullet
        bullet1 = bullet(bulletWidth,bulletHeight,xSpeed,ySpeed,color,posX,posY)
        #right bullet
        bullet2 = bullet(bulletWidth,bulletHeight,xSpeed,ySpeed,color,posX,posY)
        bullet1.rect.x = posX
        bullet1.rect.y = posY
        bullet2.rect.x = posX + player.playerWidth-bulletWidth
        bullet2.rect.y = posY
    else:
        #Upbullet
        bullet1 = bullet(bulletHeight,bulletWidth,xSpeed,ySpeed,color,posX,posY)
        #downbullet
        bullet2 = bullet(bulletHeight,bulletWidth,xSpeed,ySpeed,color,posX,posY)
        bullet1.rect.x = posX
        bullet1.rect.y = posY
        bullet2.rect.x = posX
        bullet2.rect.y = posY + player.playerHeight-bulletWidth

    if constants.activeMode != 2:
        Lists.bullet_list.add(bullet1)
        Lists.bullet_list.add(bullet2)
    else:
        if constants.playerColor == 0:
            Lists.blue_bullet_list.add(bullet1)
            Lists.blue_bullet_list.add(bullet2)
        else:
            Lists.red_bullet_list.add(bullet1)
            Lists.red_bullet_list.add(bullet2)

    Lists.all_sprites_list.add(bullet1)
    Lists.all_sprites_list.add(bullet2)
    Lists.bullet_list.add(bullet1)
    Lists.bullet_list.add(bullet2)

    # Add the bullet to the lists

def spawnOneBullet(xSpeed,ySpeed,posX,posY):
    if constants.activeMode == 0 or constants.playerColor == 0:
        color = colors.BLUE
    else:
        color = colors.RED
    if xSpeed == 0:
        singleBullet = bullet(bulletWidth,bulletHeight,xSpeed,ySpeed,color,posX,posY)
        singleBullet.rect.x = posX
        singleBullet.rect.y = posY
        Lists.bullet_list.add(singleBullet)
        Lists.all_sprites_list.add(singleBullet)
    elif ySpeed == 0:
        singleBullet = bullet(bulletHeight,bulletWidth,xSpeed,ySpeed,color,posX,posY)
        singleBullet.rect.x = posX
        singleBullet.rect.y = posY
        Lists.bullet_list.add(singleBullet)
        Lists.all_sprites_list.add(singleBullet)
    else:
        singleBullet = bullet(bulletHeight,bulletWidth,xSpeed,ySpeed,color,posX,posY)
        singleBullet.rect.x = posX
        singleBullet.rect.y = posY
        Lists.bullet_list.add(singleBullet)
        Lists.all_sprites_list.add(singleBullet)

    # Add the bullet to the lists

def removeBullets():
    #removes bullets that go off the screen
#     if constants.activeMode != 2:
        for thisBullet in Lists.bullet_list:
            if thisBullet.rect.y <constants.player.rect.y - 200:
                thisBullet.kill()
            if thisBullet.rect.y >constants.player.rect.y + 200   :
                thisBullet.kill()
            elif thisBullet.rect.x >constants.player.rect.x + 200:
                thisBullet.kill()
            elif thisBullet.rect.x < constants.player.rect.x - 200:
                thisBullet.kill()
#     else:
#         for thisBullet in Lists.bullet_list:
#             if thisBullet.rect.y <constants.menu_height:
#                 thisBullet.yVel = -math.fabs(thisBullet.yVel)
#             if thisBullet.rect.y >constants.screen_height+constants.menu_height:
#                 thisBullet.yVel = math.fabs(thisBullet.yVel)
#             elif thisBullet.rect.x > constants.screen_width:
#                 thisBullet.xVel = math.fabs(thisBullet.xVel)
#             elif thisBullet.rect.x < 0:
#                 thisBullet.xVel = -math.fabs(thisBullet.xVel)

def removeTitleBullets():
    #removes bullets that go off the screen
    for thisBullet in Lists.introScreenListBullets:
        if thisBullet.rect.y <constants.menu_height:
            thisBullet.kill()
        if thisBullet.rect.y >constants.screen_height+constants.menu_height:
            thisBullet.kill()
        elif thisBullet.rect.x > constants.screen_width:
            thisBullet.kill()
        elif thisBullet.rect.x < 0:
            thisBullet.kill()

def bulletHitEnemy(pg):
    if constants.activeMode != 2:
        for bullet in Lists.bullet_list:
            Lists.bullet_hit_list = pygame.sprite.spritecollide(bullet, Lists.Enemy_list, True)
            thisBullet = bullet
            for bullet in Lists.bullet_hit_list:
                thisBullet.kill()
                constants.score += 10
                pointGains.spawnNewPoints(colors.WHITE,thisBullet.rect.x,thisBullet.rect.y,10,pygame.time.get_ticks(),pg)
#                 Lists.startAnimateTimes_list.append(pygame.time.get_ticks())
#                 Lists.pointFade_List.append(thisBullet.rect.y)
#                 Lists.pointFade_List.append(thisBullet.rect.x)
    else:
        for bullet in Lists.red_bullet_list:
            Lists.red_bullet_hit_list = pygame.sprite.spritecollide(bullet, Lists.Blue_Enemy_list, True)
            thisBullet = bullet
            for bullet in Lists.red_bullet_hit_list:
                thisBullet.kill()
                constants.score += 10
                Lists.startAnimateTimes_list.append(pygame.time.get_ticks())
                Lists.pointFade_List.append(thisBullet.rect.y)
                Lists.pointFade_List.append(thisBullet.rect.x)
        for bullet in Lists.blue_bullet_list:
            Lists.blue_bullet_hit_list = pygame.sprite.spritecollide(bullet, Lists.Red_Enemy_list, True)
            thisBullet = bullet
            for bullet in Lists.blue_bullet_hit_list:
                thisBullet.kill()
                constants.score += 10
                Lists.startAnimateTimes_list.append(pygame.time.get_ticks())
                Lists.pointFade_List.append(thisBullet.rect.y)
                Lists.pointFade_List.append(thisBullet.rect.x)

def fireWave(gamePlayer):
# shoot up
    if constants.shotDir == 0 or constants.shotDir == constants.currHoldU:
        spawnBullets(0,straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(0,straightSpeed,gamePlayer.rect.x + constants.playerSpawnX,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(0,straightSpeed,gamePlayer.rect.x - constants.playerSpawnX/2,gamePlayer.rect.y - constants.playerSpawnY/2)

        ##this code will make 6 bullets come out instead of 4
        #spawnOneBullet(0,straightSpeed,gamePlayer.rect.x + constants.playerSpawnX*1.5,gamePlayer.rect.y - constants.playerSpawnY)
        #spawnOneBullet(0,straightSpeed,gamePlayer.rect.x - constants.playerSpawnX,gamePlayer.rect.y - constants.playerSpawnY)
    # Shoot right
    elif constants.shotDir == 1 or constants.shotDir == constants.currHoldR:
        spawnBullets(-straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(-straightSpeed,0,gamePlayer.rect.x + constants.playerSpawnX/2,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(-straightSpeed,0,gamePlayer.rect.x + constants.playerSpawnX/2,gamePlayer.rect.y + constants.playerSpawnY)

    # Shoot down
    elif constants.shotDir == 2 or constants.shotDir == constants.currHoldD:
        spawnBullets(0,-straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(0,-straightSpeed,gamePlayer.rect.x + constants.playerSpawnX,gamePlayer.rect.y + constants.playerSpawnY/2)
        spawnOneBullet(0,-straightSpeed,gamePlayer.rect.x - constants.playerSpawnX/2,gamePlayer.rect.y + constants.playerSpawnY/2)

    # shoot left!
    elif constants.shotDir == 3 or constants.shotDir == constants.currHoldL:
        spawnBullets(straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(straightSpeed,0,gamePlayer.rect.x - constants.playerSpawnX/2,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(straightSpeed,0,gamePlayer.rect.x - constants.playerSpawnX/2,gamePlayer.rect.y + constants.playerSpawnY)

    #Up right bullet
    elif constants.shotDir == constants.currHoldU+constants.currHoldR:
        spawnBullets(-diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y + constants.playerSpawnY/4)
        spawnOneBullet(-diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x + constants.playerSpawnX/4,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(-diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x + constants.playerSpawnX/1.5,gamePlayer.rect.y + constants.playerSpawnY*1.25)
    #UP Left bullet
    elif constants.shotDir == constants.currHoldU+constants.currHoldL:
        spawnBullets(diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x - constants.playerSpawnX/3,gamePlayer.rect.y - constants.playerSpawnY/1.5)
        spawnOneBullet(diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x - constants.playerSpawnX/1.5,gamePlayer.rect.y + constants.playerSpawnY)
    #Down Left bullet
    elif constants.shotDir == constants.currHoldD+constants.currHoldL:
        spawnBullets(diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x - constants.playerSpawnX/2,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x - constants.playerSpawnX/3,gamePlayer.rect.y + constants.playerSpawnY*1.25)
    #Down Right bullet
    elif constants.shotDir == constants.currHoldD+constants.currHoldR:
        spawnBullets(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
        spawnOneBullet(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x + constants.playerSpawnX/1.5,gamePlayer.rect.y - constants.playerSpawnY/2)
        spawnOneBullet(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x + constants.playerSpawnX/2,gamePlayer.rect.y + constants.playerSpawnY*1.25)
    #default to handle any odd occurences
    else:
        spawnBullets(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)


def fireNorm(gamePlayer):
    if constants.shotDir == 0:
        spawnBullets(0,straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == 1:
        spawnBullets(-straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == 2:
        spawnBullets(0,-straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == 3:
        spawnBullets(straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == constants.currHoldL:
        spawnBullets(straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == constants.currHoldD:
        spawnBullets(0,-straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == constants.currHoldR:
        spawnBullets(-straightSpeed,0,gamePlayer.rect.x,gamePlayer.rect.y)
    elif constants.shotDir == constants.currHoldU:
        spawnBullets(0,straightSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    #Up right bullet
    elif constants.shotDir == constants.currHoldU+constants.currHoldR:
        spawnBullets(-diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    #UP Left bullet
    elif constants.shotDir == constants.currHoldU+constants.currHoldL:
        spawnBullets(diagonalBulletSpeed,diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    #Down Left bullet
    elif constants.shotDir == constants.currHoldD+constants.currHoldL:
        spawnBullets(diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    #Down Right bullet
    elif constants.shotDir == constants.currHoldD+constants.currHoldR:
        spawnBullets(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)
    #default to handle any odd occurences
    else:
        spawnBullets(-diagonalBulletSpeed,-diagonalBulletSpeed,gamePlayer.rect.x,gamePlayer.rect.y)





