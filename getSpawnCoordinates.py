import pygame
import random
import colors
import constants

# This class represents the ball
# It derives from the "Sprite" class in Pygame

spawnPadding = 200
coorList = []

def generateCoords(playerX, playerY,playerW,playerH,unitWidth,unitHeight):
    invalidX = True
    invalidY = True
    while (invalidX and invalidY):
        if invalidX:
            xLocation = random.randrange(constants.screen_width - unitWidth)
            if xLocation <= playerX+playerW-spawnPadding or xLocation >= playerX+playerW+spawnPadding:
                invalidX = False
        if invalidY:
            yLocation = random.randrange(constants.screen_height - unitHeight) + constants.menu_height
            if yLocation <= playerY+playerH-spawnPadding or yLocation >= playerY+playerH+spawnPadding:
                invalidY = False
    coorList.append(xLocation)
    coorList.append(yLocation)



    return coorList

def triangleSpawnCoords(playerX, playerY,playerW,playerH,unitWidth,unitHeight):
    invalidX = True
    invalidY = True
    while (invalidX and invalidY):
        xLocation = random.randrange(constants.screen_width - unitWidth)
        if xLocation <= playerX+playerW-spawnPadding or xLocation >= playerX+playerW+spawnPadding:
            invalidX = False
        yLocation = random.randrange(constants.screen_height - unitHeight) + constants.menu_height
        if yLocation <= playerY+playerH-spawnPadding or yLocation >= playerY+playerH+spawnPadding:
            invalidY = False
    coorList.append(xLocation)
    coorList.append(yLocation)

    return coorList







