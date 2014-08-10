import block
import pygame
import random
import constants
import colors
import getSpawnCoordinates
import Lists

goodBlockHeight = 15
goodBlockWidth = 15

class goodBlock(block.Block):

    def update(self):

        #changeX = random.randrange(-2,3)
        changeY = random.randrange(0,6)

        #self.rect.x += changeX
        self.rect.y += changeY

        if self.rect.y >= constants.menu_height+constants.screen_height:
            self.rect.y = -10 + constants.menu_height
            self.rect.x = random.randrange(constants.screen_width)

def spawnGoodBlock(spawnCount,playerX,playerY,playerW,playerH):
    for i in range(spawnCount):
        gBlock = goodBlock(colors.BLACK, goodBlockWidth, goodBlockHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH,goodBlockWidth,goodBlockHeight)
        gBlock.rect.x = list[len(list)-2]
        gBlock.rect.y = list[len(list)-1]

        # Add the block to the list of objects
        Lists.Good_block_list.add(gBlock)
        Lists.all_sprites_list.add(gBlock)



