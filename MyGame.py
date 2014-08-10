##Author: Nick Ackerman
##Contact
# E-mail:    ncackerman@wisc.edu
# cellphone: 715-897-7639
# github:    github.com/ncackerman/Tankd

import pygame
import math
import random
import block
import goodBlock
import badBlock
import constants
import player
import bullets
import triangle
import circle
import colors
import straffer
import fatties
import fourSquare
import fastCircle
import hunterStraffer
import Lists
from pygame.locals import *

#--- Global constants ---
# --- Classes ---

# This class represents an instance of the game. If we need to
# reset the game we'd just need to create a new instance of this
# class.
class Game():

    # --- Class methods
    # Set up the game
    def __init__(self):
        constants.score = 0
        constants.game_over = False

        self.strafferXDirection = 1
        self.strafferYDirection = 1

        self.gameTime = 0
        self.triggerTime = 0

        self.fattyNumber = 1
        self.goodBlockNumber = 0
        self.badBlockNumber = 3
        self.triangleNumber = 0
        self.circleNumber = 0
        self.strafferNumber = 0
        self.fourSquareNumber = 0
        self.fastCircles = 0
        self.hunterStrafferNumber = 0

        self.wavePower = False

        # Create the player
        constants.player = player.Player(colors.BLUE, constants.playerSpawnX, constants.menu_height+constants.playerSpawnY)
        self.introScreenPlayer = player.Player(colors.BLUE, constants.screen_width/2, constants.menu_height+constants.screen_height/4)
        Lists.all_sprites_list.add(constants.player)
        Lists.player_list.add(constants.player)


    def initial_Spawn(self):
        if constants.activeMode == 0:
            color = colors.BLACK
            goodBlock.spawnGoodBlock(self.goodBlockNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight)
            triangle.spawnTriangle(self.triangleNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,triangle.triangleSpeed,color)
            badBlock.spawnBadBlock(self.badBlockNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            fourSquare.spawnFourSquare(self.fourSquareNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            fatties.spawnFatty(self.fattyNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            circle.spawnCircle(self.circleNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            straffer.spawnStraffer(self.strafferNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            fastCircle.spawnfastCircle(self.fastCircles,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            hunterStraffer.spawnHunterStraffer(self.hunterStrafferNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
            #bottomUpCountDown.spawnbottomUpCountDown(colors.SOFT_RED)
            #bottomUpHaz.spawnBottomUpHaz(colors.SOFT_RED)
        else:
            goodBlock.spawnGoodBlock(self.goodBlockNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight)
            triangle.spawnTriangle(self.triangleNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,triangle.triangleSpeed,colors.BLUE)
            badBlock.spawnBadBlock(self.badBlockNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.RED)
            fourSquare.spawnFourSquare(self.fourSquareNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.BLUE)
            fatties.spawnFatty(self.fattyNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.RED)
            circle.spawnCircle(self.circleNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.RED)
            straffer.spawnStraffer(self.strafferNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.BLUE)
            fastCircle.spawnfastCircle(self.fastCircles,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.RED)
            hunterStraffer.spawnHunterStraffer(self.hunterStrafferNumber,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,colors.RED)

    # Process all of the events. Return a "True" if we need
    # to close the window.
    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.quit_game = True
                return True
            elif event.type == pygame.KEYDOWN:
                ## quit keyes
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    constants.quit_game = True
                    return True
                if event.key == pygame.K_LEFT:
                    constants.player.changespeed(-3,0)
                    constants.currHold += constants.currHoldL
                    if constants.spaceHold == False:
                        constants.shotDir = constants.shotDirL
                elif event.key == pygame.K_RIGHT:
                    constants.player.changespeed(3,0)
                    constants.currHold += constants.currHoldR
                    if constants.spaceHold == False:
                        constants.shotDir = constants.shotDirR
                elif event.key == pygame.K_UP:
                    constants.player.changespeed(0,-3)
                    constants.currHold += constants.currHoldU
                    if constants.spaceHold == False:
                        constants.shotDir = constants.shotDirU
                elif event.key == pygame.K_DOWN:
                    constants.player.changespeed(0,3)
                    constants.currHold += constants.currHoldD
                    if constants.spaceHold == False:
                        constants.shotDir = constants.shotDirD
                elif event.key == pygame.K_SPACE:
                    constants.spaceHold = True
                    if constants.currHold != 0:
                        constants.shotDir = constants.currHold
                elif (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and (constants.activeMode == 1 or constants.activeMode == 2):
                    #constants.player = constants.switchPlayerColor(constants.player)
                    if constants.playerColor == 0:
                        constants.playerColor = 1
                        newPlayer = player.Player(colors.RED, constants.player.getX(), constants.player.getY())
                        newPlayer.setSpeed(constants.player.getChangeX(), constants.player.getChangeY())
                        for p in Lists.player_list:
                            p.remove()
                            p.kill()
                        constants.player = newPlayer
                        Lists.player_list.add(constants.player)
                        Lists.all_sprites_list.add(constants.player)
                    elif constants.playerColor == 1:
                        constants.playerColor = 0
                        newPlayer = player.Player(colors.BLUE, constants.player.getX(), constants.player.getY())
                        newPlayer.setSpeed(constants.player.getChangeX(), constants.player.getChangeY())
                        for p in Lists.player_list:
                            p.remove()
                            p.kill()
                        constants.player = newPlayer
                        Lists.player_list.add(constants.player)
                        Lists.all_sprites_list.add(constants.player)
#                     if constants.game_over:
#                         #this resets to a new instance of the game if game over is true and the space bar is pressed
#                         self.__init__()

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    constants.currHold -= constants.currHoldL
                    constants.player.changespeed(3,0)
                elif event.key == pygame.K_RIGHT:
                    constants.currHold -= constants.currHoldR
                    constants.player.changespeed(-3,0)
                elif event.key == pygame.K_UP:
                    constants.currHold -= constants.currHoldU
                    constants.player.changespeed(0,3)
                elif event.key == pygame.K_DOWN:
                    constants.currHold -= constants.currHoldD
                    constants.player.changespeed(0,-3)
                elif event.key == pygame.K_SPACE:
                    constants.shotCount = 0
                    constants.spaceHold = False

        #method that handles bullet generation. Spawning the bullets based on
        #current held directio  or last preivously held direction. Also has
        #a shot clock to prevent bullets from coming out as a constant stream
        if constants.spaceHold:
            if self.wavePower:
                if constants.shotCount == 0:
                    bullets.fireWave(constants.player)
                    constants.shotCount = 1
                elif constants.shotCount == 15:
                    constants.shotCount = 0
                else:
                    constants.shotCount +=1
            else:
                if constants.shotCount == 0:
                    bullets.fireNorm(constants.player)

                    constants.shotCount = 1
                elif constants.shotCount == 8:
                    constants.shotCount = 0
                else:
                    constants.shotCount +=1
        if constants.game_over:
            return True
        else:
            return False

    # This method is run each time through the frame. It
    # updates positions and checks for collisions.
    def spawn_enemies(self):

        if (pygame.time.get_ticks()-constants.lastEndTime-constants.pauseTimeSinceStart)/1000 == 20:
            print 'A'
            constants.minEnemyCount = 8
        elif (pygame.time.get_ticks()-constants.lastEndTime-constants.pauseTimeSinceStart)/1000 == 40:
            print 'B'
            constants.minEnemyCount = 11
        elif (pygame.time.get_ticks()-constants.lastEndTime-constants.pauseTimeSinceStart)/1000 == 60:
            print 'C'
            constants.minEnemyCount = 15
        elif (pygame.time.get_ticks()-constants.lastEndTime-constants.pauseTimeSinceStart)/1000 == 80:
            print 'D'
            constants.minEnemyCount = 20

        #(constants.pauseTimeSinceStart-constants.lastEndTime)
        deltaSeconds = ((pygame.time.get_ticks()-constants.lastEndTime-constants.pauseTimeSinceStart)-constants.lastSpawnTime)/1000
        if deltaSeconds >= constants.timeTillSpawn or len(Lists.Enemy_list) < constants.minEnemyCount:
            constants.timeTillSpawn = constants.secondsTillNextSpawnList[random.randrange(0,len(constants.secondsTillNextSpawnList))]
            scoreRate  = constants.score - constants.scoreForSpawnRate
            spawnValue = random.random()
            constants.spawnCounter = 10 + scoreRate/constants.scoreRateAdjuster + random.randrange(pygame.time.get_ticks()/5000 + 1)
            currEnemyCount = len(Lists.Enemy_list)
            while constants.spawnCounter + currEnemyCount > constants.maxEnemyCount:
                constants.spawnCounter = constants.spawnCounter/2
            constants.lastSpawnTime = pygame.time.get_ticks() - constants.lastEndTime - constants.pauseTimeSinceStart
            constants.count = 0
            #spawn a random number of enemies
        if constants.count < constants.spawnCounter:
            spawnValue = random.random()
            if constants.activeMode != 0:
                colorValue = random.random()
                if colorValue > 0.5:
                    color = colors.RED
                else:
                    color = colors.BLUE
            else:
                color = colors.BLACK
            if (self.gameTime-constants.pauseTimeSinceStart-constants.lastEndTime)/1000 < 60:
                if spawnValue < 0.14:
                    triangle.spawnTriangle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,5,color)
                elif spawnValue < 0.24:
                    badBlock.spawnBadBlock(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.42:
                    if len(Lists.fourSquare_list) <3 and (pygame.time.get_ticks() - constants.timeSinceLastFourSquareSpawn)/1000 > 10:
                        fourSquare.spawnFourSquare(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                        constants.timeSinceLastFourSquareSpawn = pygame.time.get_ticks()
                    else:
                        constants.count -= 1
                elif spawnValue < 0.56:
                    if len(Lists.fatty_list) <3 and (pygame.time.get_ticks() - constants.timeSinceLastFattySpawn)/1000 > 10:
                        fatties.spawnFatty(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                        constants.timeSinceLastFattySpawn = pygame.time.get_ticks()
                    else:
                        constants.count -= 1
                elif spawnValue < 0.75:
                    circle.spawnCircle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.95 - pygame.time.get_ticks()/500000:
                    hunterStraffer.spawnHunterStraffer(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.975 - pygame.time.get_ticks()/500000:
                    fastCircle.spawnfastCircle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 1:
                    triangle.spawnTriangle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,5,color)
            else:
                if spawnValue < 0.125:
                    triangle.spawnTriangle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,5,color)
                elif spawnValue < 0.25:
                    badBlock.spawnBadBlock(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.50:
                    if len(Lists.fourSquare_list) <3 and (pygame.time.get_ticks() - constants.timeSinceLastFourSquareSpawn)/1000 > 10:
                        fourSquare.spawnFourSquare(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                        constants.timeSinceLastFourSquareSpawn = pygame.time.get_ticks()
                    else:
                        constants.count -= 1
                elif spawnValue < 0.55:
                    if len(Lists.fatty_list) <3 and (pygame.time.get_ticks() - constants.timeSinceLastFattySpawn)/1000 > 10:
                        fatties.spawnFatty(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                        constants.timeSinceLastFattySpawn = pygame.time.get_ticks()
                    else:
                        constants.count -= 1
                elif spawnValue < 0.60:
                    circle.spawnCircle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.80 - pygame.time.get_ticks()/500000:
                    hunterStraffer.spawnHunterStraffer(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 0.90 - pygame.time.get_ticks()/500000:
                    fastCircle.spawnfastCircle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,color)
                elif spawnValue < 1:
                    triangle.spawnTriangle(1,constants.player.rect.x, constants.player.rect.y, player.playerWidth, player.playerHeight,5,color)
            constants.count += 1
            constants.scoreForSpawnRate = constants.score
            constants.scoreRateAdjuster += 3



    def spawn_hazards(self,screen,background):
        reducedGameTime = (self.gameTime-constants.pauseTimeSinceStart-constants.lastEndTime)/1000
        while reducedGameTime > constants.hazardSpawnInterval:
            reducedGameTime -= constants.hazardSpawnInterval
        if  reducedGameTime == constants.hazardSpawnInterval and constants.hazard == 0:
            constants.hazard = constants.hazardList[random.randrange(0,len(constants.hazardList))]
            constants.hazardSpawnCount += 1
        else:
            constants.hazardSpawnCount += 1



    def run_logic(self, screen,pointsGained):

        if not constants.game_over:

            straffer.moveStraffer()
            hunterStraffer.moveHunterStraffer()
            fourSquare.moveFourSquare()
            bullets.removeBullets()
            fatties.moveFatty()
            circle.moveCircle()
            bullets.bulletHitEnemy(pointsGained)


            # Move just the player
            #Lists.player_list.update()
            # Move all the sprites
            if not constants.timeStop:
                Lists.all_sprites_list.update()
                Lists.deathCircle_list.update()
            else:
                constants.timeStop = constants.timeStopPowerup(constants.firstTime)


            #see if player hit a type of enemy
            if constants.activeMode ==0:
                triangle_hit_list = pygame.sprite.spritecollide(constants.player, Lists.triangle_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in triangle_hit_list:
                    constants.game_over = True
                Bad_block_hit_list = pygame.sprite.spritecollide(constants.player, Lists.Bad_block_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in Bad_block_hit_list:
                    constants.game_over = True
                circle_hit_list = pygame.sprite.spritecollide(constants.player, Lists.circle_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in circle_hit_list:
                    constants.game_over = True
                straffer_hit_list = pygame.sprite.spritecollide(constants.player, Lists.straffer_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in straffer_hit_list:
                    constants.game_over = True
                fatty_hit_list = pygame.sprite.spritecollide(constants.player, Lists.fatty_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in fatty_hit_list:
                    constants.game_over = True
#                     for dead in deathCircle_hit_list:
#                         dead.kill()
            else:
                if constants.activeMode ==2:
                    for blueBullet in Lists.blue_bullet_list:
                        bullets_hit_list = pygame.sprite.spritecollide(blueBullet, Lists.red_bullet_list, True, pygame.sprite.collide_rect_ratio(.9))
                        for bullet in bullets_hit_list:
                            blueBullet.kill()
                    if constants.playerColor == 0:
                        redBullet_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.red_bullet_list, True, pygame.sprite.collide_rect_ratio(.75))
                        for enemy in redBullet_hit_list:
                            constants.game_over = True
                    else:
                        blueBullet_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.blue_bullet_list, True, pygame.sprite.collide_rect_ratio(.75))
                        for enemy in blueBullet_hit_list:
                            constants.game_over = True
                redEnemy_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.Red_Enemy_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in redEnemy_hit_list:
                        constants.game_over = True
                blueenemy_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.Blue_Enemy_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in blueenemy_hit_list:
                    constants.game_over = True
                fatty_hit_list = pygame.sprite.spritecollide(constants.player, Lists.fatty_list, True, pygame.sprite.collide_rect_ratio(.75))
                for enemy in fatty_hit_list:
                    constants.game_over = True


            deathCircle_hit_list = pygame.sprite.spritecollide(constants.player, Lists.deathCircle_list, True, pygame.sprite.collide_rect_ratio(.9))
            for enemy in deathCircle_hit_list:
                constants.game_over = True

#                 if constants.playerColor == 0:
#                     redEnemy_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.Red_Enemy_list, True, pygame.sprite.collide_rect_ratio(.75))
#                     for enemy in redEnemy_hit_list:
#                         constants.game_over = True
#                     if constants.activeMode == 2:

#
#                 else:
#                     blueenemy_hit_list =  pygame.sprite.spritecollide(constants.player, Lists.Blue_Enemy_list, True, pygame.sprite.collide_rect_ratio(.75))
#                     for enemy in blueenemy_hit_list:
#                         constants.game_over = True
#                     if constants.activeMode == 2:


            blocks_hit_list = pygame.sprite.spritecollide(constants.player, Lists.Good_block_list, True)
            for block in blocks_hit_list:
                constants.score +=1
            for dead in Lists.deathCircle_list:
                deathCircle_hit_list = pygame.sprite.spritecollide(dead, Lists.all_sprites_list, True, pygame.sprite.collide_rect_ratio(.9))




    # Display everything to the screen for the game.

    # altered to not take backgroundimage or menu image as parameters for dist testing
    # def display_frame(self, screen,backgroundImage,menuImage):

    #this may be improvable with the .clear() method
    def display_frame(self, screen,clock,background,backForHaz):
        #screen.blit(background, (0,0))
        if constants.hazard != 0:
            screen.blit(backForHaz, (0,constants.menu_height))
        Lists.all_sprites_list.clear(screen, background)
        Lists.deathCircle_list.clear(screen, background)

        #removed for distribuitino testing
        # screen.blit(backgroundImage, [0,constants.menu_height])
        # screen.blit(menuImage,[0,0])



        if constants.game_over:
#             font = pygame.font.SysFont("serif", 25)
#             text = font.render("Game Over, press SpaceBar to continue", True, colors.BLACK)
#             x = (constants.screen_width // 2) - (text.get_width() // 2)
#             y = ((constants.screen_height+constants.menu_height) // 2) - (text.get_height() // 2)
#             screen.blit(text, [x, y])
            for i in range(0,len(Lists.removePointLists)/2):
                x = Lists.removePointLists.pop(0)
                y = Lists.removePointLists.pop(0)
                pygame.draw.rect(background,colors.WHITE,[y,x,30,10])
            if constants.highScore < constants.score:
                constants.highScore = constants.score
            Lists.reset()
            constants.reset()
            constants.lastEndTime = self.gameTime + constants.pauseTimeSinceStart
            xSpeed = constants.player.change_x
            ySpeed = constants.player.change_y
            currDirection = constants.currHold
            #remove any lingering inputs
            self.__init__()
            constants.player.changespeed(xSpeed, ySpeed)
            constants.currHold = currDirection

        else:

            ##indicate the hazard direction

            #display the fps
#             if (pygame.time.get_ticks()/1000 % 2 == 0):
#                 fpsFont = pygame.font.Font(None, 25)
#                 fpsText = fpsFont.render(str(clock.get_fps()),True,colors.VIOLET)
#                 pygame.draw.rect(screen,colors.WHITE,[constants.screen_width-40,constants.menu_height,40,20])
#                 screen.blit(fpsText, [constants.screen_width-40,constants.menu_height])

            Lists.all_sprites_list.draw(screen)
            Lists.deathCircle_list.draw(screen)

            #animatePointGains(screen,background)

             # Draws the menu at the top of the screen
#             pygame.draw.polygon(screen,colors.RED,[[100,constants.menu_height/4],[100+constants.menu_height/4,constants.menu_height/4]],2)
#             pygame.draw.polygon(screen,colors.RED,[[100+constants.menu_height/4,constants.menu_height/4],[100+constants.menu_height/4,constants.menu_height/2]],2)
#             pygame.draw.polygon(screen,colors.RED,[[100+constants.menu_height/4,constants.menu_height/2],[100,constants.menu_height/2]],2)
#             pygame.draw.polygon(screen,colors.RED,[[100,constants.menu_height/2],[100,constants.menu_height/4]],2)
            self.gameTime = pygame.time.get_ticks()
            if constants.timeStop:
                pygame.draw.rect(screen, colors.RED, [100,constants.menu_height/4,2+constants.menu_height/4,2+constants.menu_height/4])

            if constants.hazard != 0:
                constants.hazCountDown(screen, constants.hazard)
                constants.hazSpawn(screen, constants.player, constants.hazard)
        pygame.display.update([0,constants.menu_height,constants.screen_width,constants.screen_height])

    def display_title(self,screen,game,background):
        screen.fill(colors.LIGHT_GREEN_YELLOW)
        if constants.firstPlay:
            game.instruction(screen,background)
        else:
            bigFont = pygame.font.Font(None, 100)
            tankdText = bigFont.render('Tank\'d',True,colors.WHITE)
            screen.blit(tankdText, [constants.screen_width/3,constants.screen_height/2])
            constants.titleFlashText(screen, self.introScreenPlayer)
        pygame.display.flip()

    ##start game on space press
    def titleScreenLogic(self,game,screen,background):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                constants.quit_game = True
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    constants.quit_game = True
                    return False
                if event.key == pygame.K_LEFT:
                    constants.player.changespeed(-3,0)
                    constants.currHold += constants.currHoldL
                elif event.key == pygame.K_RIGHT:
                    constants.player.changespeed(3,0)
                    constants.currHold += constants.currHoldR
                elif event.key == pygame.K_UP:
                    constants.modeSelect(-1)
                    constants.player.changespeed(0,-3)
                    constants.currHold += constants.currHoldU
                elif event.key == pygame.K_DOWN:
                    constants.player.changespeed(0,3)
                    constants.modeSelect(1)
                    constants.currHold += constants.currHoldD
                elif event.key == pygame.K_SPACE:
                    self.spaceHold = True
                    constants.screenFlashTime =0
                    constants.titleScreenAnimation = 0
                    Lists.introScreenList.empty()
                    screen.blit(background, (0,0))
                    if constants.firstPlay:
                        constants.firstPlay = False
                        return True
                    else:
                        game.initial_Spawn()
                        return False

                # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    constants.currHold -= constants.currHoldL
                    constants.player.changespeed(3,0)
                elif event.key == pygame.K_RIGHT:
                    constants.currHold -= constants.currHoldR
                    constants.player.changespeed(-3,0)
                elif event.key == pygame.K_UP:
                    constants.currHold -= constants.currHoldU
                    constants.player.changespeed(0,3)
                elif event.key == pygame.K_DOWN:
                    constants.currHold -= constants.currHoldD
                    constants.player.changespeed(0,-3)
                elif event.key == pygame.K_SPACE:
                    self.spaceHold = False
            else:
                return True
        return True

    def instruction(self,screen,background):
        majorSpacing  = 25
        minorSpacing  = 20
        font = pygame.font.Font(None, 24)
        bigFont = pygame.font.Font(None, 36)
        instructions1 = font.render('How To Play:',True,colors.BLACK)
        instructions2 = font.render('1. Move using the arrow keys. Up Down Left Right and Diagnols',True,colors.GREEN_BLACK)
        instructions3 = font.render('2. Shoot using space bar. Hold to fire continuously',True,colors.GREEN_BLACK)
        instructions4 = font.render('Bullets travel in the direction that is currently held,',True,colors.GREEN_BLACK)
        instructions5 = font.render('moving to the right and then pressing and holding space will',True,colors.GREEN_BLACK)
        instructions6 = font.render('shoot bullets to the right until the space bar is released',True,colors.GREEN_BLACK)
        instructions7 = font.render('3. Hit the enemy shapes to gain points',True,colors.GREEN_BLACK)
        instructions8 = font.render('4. A special enemy will light up its sides when hit. Once all four',True,colors.GREEN_BLACK)
        instructions9 = font.render('sides are lit up. run into the enemy to stop time for a moment.',True,colors.GREEN_BLACK)
        instructions17 = font.render('5. Bombs look like octagons and blow up after 20 seconds',True,colors.GREEN_BLACK)
        instructions18 = font.render('kill them before or the game will end',True,colors.GREEN_BLACK)
        instructions19 = font.render('6. Moving past the left boundary shoots you to the right boundary',True,colors.GREEN_BLACK)
        instructions10 = font.render('Medium and Hard modes only:',True,colors.BLACK)
        instructions11 = font.render('1. Pressing shift changes the color of the player and',True,colors.GREEN_BLACK)
        instructions12 = font.render('the color of bullets fired',True,colors.GREEN_BLACK)
        instructions13 = font.render('2. Only red bullets can kill blue enemies and',True,colors.GREEN_BLACK)
        instructions14 = font.render('only blue bullets can kill red enemies',True,colors.GREEN_BLACK)
        instructions15 = font.render('Hard mode only:',True,colors.BLACK)
        instructions16 = font.render('1. Certain sides will kill you if you try to pass through',True,colors.GREEN_BLACK)
        instructions20 = bigFont.render('Press Space To Continue',True,colors.WHITE)

        screen.blit(instructions1, [40,50])
        screen.blit(instructions2, [40,50+majorSpacing])
        screen.blit(instructions3, [40,50 + majorSpacing*2])
        screen.blit(instructions4, [61,50 + majorSpacing*2 + minorSpacing])
        screen.blit(instructions5, [61,50 + majorSpacing*2 + minorSpacing*2])
        screen.blit(instructions6, [61,50 + majorSpacing*2 + minorSpacing*3])
        screen.blit(instructions7, [40,50 + majorSpacing*3 + minorSpacing*3])
        screen.blit(instructions8, [40,50 + majorSpacing*4 + minorSpacing*3])
        screen.blit(instructions9, [61,50 + majorSpacing*4 + minorSpacing*4])
        screen.blit(instructions17, [40,50 + majorSpacing*5 + minorSpacing*4])
        screen.blit(instructions18, [61,50 + majorSpacing*5 + minorSpacing*5])
        screen.blit(instructions19, [40,50 + majorSpacing*6 + minorSpacing*5])
        screen.blit(instructions10, [40,50+  majorSpacing*7 + minorSpacing*5])
        screen.blit(instructions11, [40,50+  majorSpacing*8 + minorSpacing*5])
        screen.blit(instructions12, [61,50+  majorSpacing*8 + minorSpacing*6])
        screen.blit(instructions13, [40,50+  majorSpacing*9 + minorSpacing*6])
        screen.blit(instructions14, [61,50+  majorSpacing*9 + minorSpacing*7])
        screen.blit(instructions15, [40,50+  majorSpacing*10 + minorSpacing*7])
        screen.blit(instructions16, [40,50+  majorSpacing*11 + minorSpacing*7])
        screen.blit(instructions20, [180,50+  majorSpacing*12 + minorSpacing*7])

# cycle through and flash score over a recently killed enemy
def animatePointGains(screen,background):
    if (Lists.startAnimateTimes_list):
        font = pygame.font.Font(None, 18)
        z = Lists.startAnimateTimes_list.pop(0)
        Lists.startAnimateTimes_list.insert(0, z)
        #pops the oldest flashed score coordinents, once that score has been on for .7 seconds
        if (pygame.time.get_ticks() - z >= 700):
            z = Lists.startAnimateTimes_list.pop(0)
            pointsGained = font.render('+' + str(10),True,colors.VIOLET)
            #screen.blit(pointsGained, [Lists.pointFade_List.pop(1),Lists.pointFade_List.pop(0)])\
            x = Lists.removePointLists.pop(0)
            y = Lists.removePointLists.pop(0)
            pygame.draw.rect(background,colors.WHITE,[y,x,30,10])
            #pygame.draw.rect(screen,colors.WHITE,[y,x,30,10])

        for i in range(0,(len(Lists.pointFade_List)/2)):
            pointsGained = font.render('+' + str(10),True,colors.VIOLET)
            x = Lists.pointFade_List.pop(0)
            y = Lists.pointFade_List.pop(0)
            background.blit(pointsGained, [y,x])
            screen.blit(pointsGained, [y,x])
            Lists.removePointLists.append(x)
            Lists.removePointLists.append(y)
    else:
        return False

# draws a background grid
def backGroundGrid(screen):
    yDivs = 20
    xDivs = 20
    spacing = 5
    unitGridWidth = (constants.screen_width-((yDivs+1)*spacing))/yDivs
    unitGridHeight = (constants.screen_height-((xDivs+1)*spacing))/xDivs
    for i in range(yDivs):
        for j in range(xDivs):
            pygame.draw.rect(screen,colors.YELLOW,[spacing*i + spacing +(i)*unitGridWidth,spacing*j + spacing + j*unitGridHeight + constants.menu_height,unitGridWidth,unitGridHeight],spacing)

# --- Main Function ---
def main():

    # Initialize Pygame and set up the window
    pygame.init()
    size = [constants.screen_width, constants.menu_height+constants.screen_height]
    flags = DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)
    #screen = pygame.display.set_mode(size)
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    background.fill(colors.BACKGROUND)
    pygame.draw.line(background, colors.GREEN, [0,constants.menu_height], [0,constants.menu_height+constants.screen_height], 3)
    pygame.draw.line(background, colors.GREEN, [0,constants.menu_height+1], [constants.screen_width,constants.menu_height+1], 3)
    pygame.draw.line(background, colors.GREEN, [constants.screen_width-1,constants.menu_height], [constants.screen_width-1,constants.menu_height+constants.screen_height], 3)
    pygame.draw.line(background, colors.GREEN, [0,constants.menu_height+constants.screen_height-1], [constants.screen_width,constants.menu_height+constants.screen_height-1], 3)
    pygame.draw.rect(background, colors.SOFT_GREY, [0,0,constants.screen_width,constants.menu_height])
    backForHaz = pygame.Surface([constants.screen_width,constants.screen_height+20])
    backForHaz.fill(colors.BACKGROUND)
    pygame.draw.line(backForHaz, colors.GREEN, [0,0], [0,0+constants.screen_height], 3)
    pygame.draw.line(backForHaz, colors.GREEN, [0,0+1], [constants.screen_width,0+1], 3)
    pygame.draw.line(backForHaz, colors.GREEN, [constants.screen_width-1,0], [constants.screen_width-1,0+constants.screen_height], 3)
    pygame.draw.line(backForHaz, colors.GREEN, [0,0+constants.screen_height-1], [constants.screen_width,0+constants.screen_height-1], 3)

    # removed for distribuitino testing
    # menuImage = pygame.image.load("menu2.bmp").convert()
    # backgroundImage = pygame.image.load("gameBackground.bmp").convert()

    pygame.display.set_caption("Tank'd")
    pygame.mouse.set_visible(True)

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    titleScreen = True
    secInt = 0

    font = pygame.font.Font(None, 18)
    pointsGained = font.render('+' + str(10),True,colors.VIOLET)

    # Main game loop
    while not done:
        #pygame.time.wait(4)
        #stay in title screen till player selecets an input. include code to so if the left button is held the player will start moving to the left
        while titleScreen:
            game.display_title(screen,game,background)
            titleScreen = game.titleScreenLogic(game,screen,background)
            constants.pauseTimeSinceStart = pygame.time.get_ticks() - constants.lastEndTime

        # Process events (keystrokes, mouse clicks, etc)
        titleScreen = game.process_events()

        #spawn enemies
        game.spawn_enemies()
        game.spawn_hazards(screen,background)

        # altered to not take backgroundimage or menu image as parameters for dist testing
        # game.display_frame(screen,backgroundImage,menuImage)
        game.display_frame(screen,clock,background,backForHaz )
        if pygame.time.get_ticks()/1000 > secInt:
            pygame.draw.rect(screen, colors.SOFT_GREY, [0,0,constants.screen_width,constants.menu_height])
            secInt = pygame.time.get_ticks()/1000
            font = pygame.font.Font(None, 25)
            scoreText = font.render('score  ' + str(constants.score),True,colors.GREEN)
            gameTimeText = font.render('time  ' + str((pygame.time.get_ticks()-constants.pauseTimeSinceStart-constants.lastEndTime)/1000),True,colors.GREEN)
            highScoreText = font.render('high  ' + str(constants.highScore),True,colors.GREEN)

#             for thisFatty in Lists.fatty_list:
#                 fattyHealth = font.render(str(thisFatty.health),True,colors.BLACK)
#                 screen.blit(fattyHealth, [thisFatty.rect.x+16.5,thisFatty.rect.y+13])

            # Put the image of the text on the screen at 250x250
            screen.blit(scoreText, [0,0])
            screen.blit(gameTimeText, [300,0])
            screen.blit(highScoreText, [500,0])

        # Update object positions, check for collisions
        game.run_logic(screen,pointsGained)
        # Draw the current frame

        #should the screen exit? Yes! if the red x is clicked on the game window
        done = constants.quit_game

        # Pause for the next frame
        clock.tick(60)
    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()



