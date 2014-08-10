import block
import random
import constants
import colors
import getSpawnCoordinates
import Lists

badBlockWidth = 20
badBlockHeight = 20

class badBlock(block.Block):

    def update(self):

        changeX = random.randrange(0,3)
        changeY = random.randrange(0,3)

        if self.rect.x >= constants.screen_width - badBlockHeight +2:
            self.xConstant = -1
        elif self.rect.x <= 0:
            self.xConstant = 1

        if self.rect.y >= constants.screen_height+constants.menu_height - badBlockHeight +8:
            self.yConstant = -1
        elif self.rect.y <= constants.menu_height:
            self.yConstant = 1

        self.rect.x += ((changeX) * self.xConstant)
        self.rect.y += ((changeY) * self.yConstant)


def spawnBadBlock(spawnCount,playerX,playerY,playerW,playerH,color):
    for i in range(spawnCount):
        enemyBlock = badBlock(color, block.blockWidth, block.blockHeight)
        list = getSpawnCoordinates.generateCoords(playerX, playerY, playerW, playerH, badBlockWidth, badBlockHeight)

        enemyBlock.rect.x = list[len(list)-2]
        enemyBlock.rect.y = list[len(list)-1]

        # Add the block to the list of objects
        if constants.activeMode != 2:
            Lists.Enemy_list.add(enemyBlock)
        else:
            if color == colors.BLUE:
                Lists.Blue_Enemy_list.add(enemyBlock)
            else:
                Lists.Red_Enemy_list.add(enemyBlock)
        Lists.all_sprites_list.add(enemyBlock)
        Lists.Bad_block_list.add(enemyBlock)

