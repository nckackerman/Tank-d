import Lists
import pygame
import colors
import bullets
import player
import bottomUpHaz
import pygame

screen_width=640
screen_height=480
menu_height = 50
timeSinceLastFourSquareSpawn = 0
scoreForSpawnRate = 0
timeStop = True
firstTime = 0
game_over = False
quit_game = False
score = 0
enemySpawnList = [0,1,2,3,4,5]
timeSinceLastFattySpawn = 0
scoreRateAdjuster = 40
secondsTillNextSpawnList = [5,6,6,7,5,8,4]
timeTillSpawn = 5
lastSpawnTime = 0
maxEnemyCount = 60
lastEndTime = 0
pauseTimeSinceStart = 0
hazardList = [1,2,3,4]
hazard = 0
hazardSpawnCount = 0
time_bottomUpHaz = 100.0
knifeCycle = 0
hazardWarningTime = 1
hazardWaitTime = 200
hazardCounter = -hazardWaitTime -20
hazardRecedTime = 0
hazardSpawnInterval = 40
highScore = 0
hazArrowOffset = 20
hazArrowWidth = 10
hazArrowHeight = 40
hazArrowPointerWidth = 20
playerSpawnX = 20
playerSpawnY = 20
currHold = 0
currHoldU = 5
currHoldR = 9
currHoldD = 7
currHoldL = 8
straightSpeed = 5
shotDir = 0
shotDirU = 0
shotDirL = 3
shotDirR = 1
shotDirD = 2
spaceHold = False
shotCount = 0
screenFlashTime = 0
titleScreenAnimation = 0
activeMode = 0
modePossible = 2
titleMenuSep = 40
playerColor = 0
player = None
wavePower = False
count = 0
spawnCounter = 0
firstPlay = True
minEnemyCount = 5
logicOffSet = 0

def reset():
    global score, lastSpawnTime, hazard, hazardCounter, hazardRecedTime, hazardWarningTime, wavePower, playerColor
    score = 0
    lastSpawnTime = 0
    hazard = 0
    hazardCounter = -220
    hazardRecedTime = 0
    hazardWarningTime = 0
    wavePower = False
    playerColor = 0


def timeStopPowerup(time):
    firstTime = time
    secondTimeStop = pygame.time.get_ticks()
    Lists.player_list.update()
    Lists.bullet_list.update()
    Lists.fourSquare_list.update()
    timeStop = True
    if secondTimeStop - firstTime > 3000:
        timeStop = False
    return timeStop

def hazCountDown(screen,haz):
    if(haz == 1):
        bottomUpHazCountDown(screen)
    elif(haz == 2):
        topDownHazCountDown(screen)
    elif(haz == 3):
        leftRightHazCountDown(screen)
    elif(haz == 4):
        rightLeftHazCountDown(screen)

def hazSpawn(screen, player, haz):
    global hazardCounter, hazardRecedTime, hazardWarningTime, hazard
    if(haz == 1):
        if hazardCounter < time_bottomUpHaz*2 + hazardWaitTime:
            bottomUpHaz(screen, player)
        else:
            hazard = 0
            hazardCounter = -220
            hazardRecedTime = 0
            hazardWarningTime = 0
    elif(haz == 2):
        if hazardCounter < time_bottomUpHaz*2 + hazardWaitTime:

            topDownHaz(screen, player)
        else:
            hazard = 0
            hazardCounter = -220
            hazardRecedTime = 0
            hazardWarningTime = 0
    elif(haz == 3):
        if hazardCounter < time_bottomUpHaz*2 + hazardWaitTime:
            leftRightHaz(screen, player)
        else:
            hazard = 0
            hazardCounter = -220
            hazardRecedTime = 0
            hazardWarningTime = 0
    elif(haz     == 4):
        if hazardCounter < time_bottomUpHaz*2 + hazardWaitTime:
            rightLeftHaz(screen, player)
        else:
            hazard = 0
            hazardCounter = -220
            hazardRecedTime = 0
            hazardWarningTime = 0
    pygame.draw.rect(screen,colors.SOFT_GREY,[[0,menu_height-20],[screen_width,20]])


def bottomUpHazCountDown(screen):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazArrowOffset, hazArrowHeight, hazArrowWidth, hazArrowPointerWidth, hazardWaitTime

    if hazardWarningTime < hazardWaitTime:
        reducedTime = hazardWarningTime
        while reducedTime > 50:
            reducedTime -= 50
        if reducedTime > 25:
            topOfArrowStem = menu_height+screen_height - hazArrowOffset
            pygame.draw.rect(screen, colors.SOFT_RED, [(screen_width/2)-hazArrowWidth/2, topOfArrowStem-hazArrowHeight,hazArrowWidth,hazArrowHeight])
            pygame.draw.polygon(screen, colors.SOFT_RED, [[(screen_width/2)-hazArrowPointerWidth,topOfArrowStem-hazArrowHeight],[(screen_width/2)+hazArrowPointerWidth,topOfArrowStem-hazArrowHeight],[screen_width/2,topOfArrowStem-hazArrowHeight-hazArrowPointerWidth]])
        hazardWarningTime +=1

def bottomUpHaz(screen,player):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazardRecedTime

    if hazardCounter < time_bottomUpHaz:
        depth = menu_height+screen_height-(((screen_height/2)/time_bottomUpHaz) * hazardCounter)
    elif hazardCounter <= time_bottomUpHaz + hazardWaitTime:
        depth = menu_height+screen_height/2
    else:
        depth = menu_height+screen_height/2+(((screen_height/2)/time_bottomUpHaz)*hazardRecedTime)
        hazardRecedTime +=1
    pygame.draw.rect(screen, colors.SOFT_RED, [0,depth,screen_width,menu_height+screen_height/2])
    if hazardCounter % 10 == 0 and hazardCounter > 0:
        if player.rect.y+12 > depth:
            player.kill()
            game_over = True
        for sprite in Lists.Enemy_list:
            if sprite.rect.y+10 > depth:
                sprite.kill()
    hazardCounter += 1
    if knifeCycle == 40:
        knifeCycle =0
    else:
        knifeCycle += 4
    knifeSpacing = -40
    while knifeSpacing < screen_width:
        pygame.draw.polygon(screen,colors.SOFT_RED,[[knifeSpacing+10+knifeCycle,depth-10],[knifeSpacing+20+knifeCycle,depth],[knifeSpacing+knifeCycle,depth]])
        knifeSpacing += 20

def topDownHazCountDown(screen):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazArrowOffset, hazArrowHeight, hazArrowWidth, hazArrowPointerWidth, hazardWaitTime

    if hazardWarningTime < hazardWaitTime:
        reducedTime = hazardWarningTime
        while reducedTime > 50:
            reducedTime -= 50
        if reducedTime > 25:
            topOfArrowStem = menu_height + hazArrowOffset
            pygame.draw.rect(screen, colors.SOFT_RED, [(screen_width/2)-5, topOfArrowStem,hazArrowWidth,hazArrowHeight])
            pygame.draw.polygon(screen, colors.SOFT_RED, [[(screen_width/2)-hazArrowPointerWidth,topOfArrowStem+hazArrowHeight],[(screen_width/2)+hazArrowPointerWidth,topOfArrowStem+hazArrowHeight],[screen_width/2,topOfArrowStem+hazArrowHeight+hazArrowPointerWidth]])
        hazardWarningTime +=1

def topDownHaz(screen,player):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazardRecedTime
    if hazardCounter > 0:
        if hazardCounter < time_bottomUpHaz:
            depth = menu_height+(((screen_height/2)/time_bottomUpHaz) * hazardCounter)
        elif hazardCounter <= time_bottomUpHaz + hazardWaitTime:
            depth = menu_height+screen_height/2
        else:
            depth = menu_height+screen_height/2-(((screen_height/2)/time_bottomUpHaz)*hazardRecedTime)
            hazardRecedTime +=1
        pygame.draw.rect(screen, colors.SOFT_RED, [0,menu_height,screen_width,depth-menu_height])
        if hazardCounter % 10 == 0 and hazardCounter > 0:
            if player.rect.y < depth:
                player.kill()
                game_over = True
            for sprite in Lists.Enemy_list:
                if sprite.rect.y < depth:
                    sprite.kill()
        if knifeCycle == 40:
            knifeCycle =0
        else:
            knifeCycle += 4
        knifeSpacing = -40
        while knifeSpacing < screen_width:
            pygame.draw.polygon(screen,colors.SOFT_RED,[[knifeSpacing+10+knifeCycle,depth+10],[knifeSpacing+20+knifeCycle,depth],[knifeSpacing+knifeCycle,depth]])
            knifeSpacing += 20
    hazardCounter += 1

def leftRightHazCountDown(screen):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazArrowOffset, hazArrowHeight, hazArrowWidth, hazArrowPointerWidth, hazardWaitTime

    if hazardWarningTime < hazardWaitTime:
        reducedTime = hazardWarningTime
        while reducedTime > 50:
            reducedTime -= 50
        if reducedTime > 25:
            topOfArrowStem = hazArrowOffset + hazArrowHeight
            pygame.draw.rect(screen, colors.SOFT_RED, [hazArrowOffset, menu_height + screen_height/2 - hazArrowWidth/2, hazArrowHeight,hazArrowWidth])
            pygame.draw.polygon(screen, colors.SOFT_RED, [[topOfArrowStem,menu_height+screen_height/2 + hazArrowPointerWidth],[topOfArrowStem,menu_height+screen_height/2 - hazArrowPointerWidth],[topOfArrowStem +hazArrowPointerWidth,menu_height+screen_height/2]])
        hazardWarningTime +=1

def leftRightHaz(screen,player):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazardRecedTime
    if hazardCounter > 0:
        if hazardCounter < time_bottomUpHaz:
            depth = ((screen_width/2)/time_bottomUpHaz) * hazardCounter
        elif hazardCounter <= time_bottomUpHaz + hazardWaitTime:
            depth = screen_width/2
        else:
            depth = screen_width/2-(((screen_width/2)/time_bottomUpHaz)*hazardRecedTime)
            hazardRecedTime +=1
        pygame.draw.rect(screen, colors.SOFT_RED, [0,menu_height,depth,screen_height])
        if hazardCounter % 10 == 0 and hazardCounter > 0:
            if player.rect.x < depth:
                player.kill()
                game_over = True
            for sprite in Lists.Enemy_list:
                if sprite.rect.x < depth:
                    sprite.kill()

        if knifeCycle == 40:
            knifeCycle =0
        else:
            knifeCycle += 4
        knifeSpacing = menu_height -20
        while knifeSpacing < menu_height + screen_height:
            pygame.draw.polygon(screen,colors.SOFT_RED,[[depth+10,knifeSpacing+10+knifeCycle],[depth,knifeSpacing+20+knifeCycle],[depth,knifeSpacing+knifeCycle]])
            knifeSpacing += 20
    hazardCounter += 1

def rightLeftHazCountDown(screen):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazArrowOffset, hazArrowHeight, hazArrowWidth, hazArrowPointerWidth, hazardWaitTime

    if hazardWarningTime < hazardWaitTime:
        reducedTime = hazardWarningTime
        while reducedTime > 50:
            reducedTime -= 50
        if reducedTime > 25:
            topOfArrowStem = screen_width - hazArrowOffset -hazArrowHeight
            pygame.draw.rect(screen, colors.SOFT_RED, [topOfArrowStem, menu_height + screen_height/2 - hazArrowWidth/2, hazArrowHeight,hazArrowWidth])
            pygame.draw.polygon(screen, colors.SOFT_RED, [[topOfArrowStem-hazArrowPointerWidth,menu_height+screen_height/2],[topOfArrowStem,menu_height+screen_height/2 - hazArrowPointerWidth],[topOfArrowStem,menu_height+screen_height/2 + hazArrowPointerWidth]])
        hazardWarningTime +=1

def rightLeftHaz(screen,player):
    global hazardCounter, knifeCycle, game_over, hazardWarningTime, hazardRecedTime
    if hazardCounter > 0:
        if hazardCounter < time_bottomUpHaz:
            depth = screen_width- (((screen_width/2)/time_bottomUpHaz) * hazardCounter)
        elif hazardCounter <= time_bottomUpHaz + hazardWaitTime:
            depth = screen_width/2
        else:
            depth = screen_width-(screen_width/2-(((screen_width/2)/time_bottomUpHaz)*hazardRecedTime))
            hazardRecedTime +=1
        pygame.draw.rect(screen, colors.SOFT_RED, [depth,menu_height,screen_width,screen_height])
        if hazardCounter % 10 == 0 and hazardCounter > 0:
            if player.rect.x+10 > depth:
                player.kill()
                game_over = True
            for sprite in Lists.Enemy_list:
                if sprite.rect.x > depth:
                    sprite.kill()
                    Lists.startAnimateTimes_list.append(pygame.time.get_ticks())
                    Lists.pointFade_List.append(sprite.rect.y)
                    Lists.pointFade_List.append(sprite.rect.x)
        if knifeCycle == 40:
            knifeCycle =0
        else:
            knifeCycle += 4
        knifeSpacing = menu_height -20
        while knifeSpacing < menu_height + screen_height:
            pygame.draw.polygon(screen,colors.SOFT_RED,[[depth-10,knifeSpacing+10+knifeCycle],[depth,knifeSpacing+20+knifeCycle],[depth,knifeSpacing+knifeCycle]])
            knifeSpacing += 20
    hazardCounter += 1

def titleFlashText(screen, p):
    global screenFlashTime, titleScreenAnimation, activeMode
    #pygame.draw.ellipse(screen, colors.BLACK, [screen_width/3,screen_height/1.33 + titleMenuSep*activeMode,15,15])

    littleFont = pygame.font.SysFont("Arial", 35)
    easyMode = littleFont.render('Easy Mode',True,colors.BLACK)
    medMode = littleFont.render('Medium Mode',True,colors.BLACK)
    hardMode = littleFont.render('Hard Mode',True,colors.BLACK)
    if(activeMode == 0):
        easyMode = littleFont.render('Easy Mode',True,colors.SOFT_GREEN)
        instructionText = littleFont.render('Press Space bar to play Easy mode',True,colors.SOFT_GREEN)
    if(activeMode == 1):
        medMode = littleFont.render('Medium Mode',True,colors.SOFT_GREEN)
        instructionText = littleFont.render('Press Space bar to play Medium mode',True,colors.SOFT_GREEN)
    if(activeMode == 2):
        hardMode = littleFont.render('Hard Mode',True,colors.SOFT_GREEN)
        instructionText = littleFont.render('Press Space bar to play Hard mode',True,colors.SOFT_GREEN)

    reducedTime = screenFlashTime
    while reducedTime > 75:
        reducedTime -= 75
    if reducedTime < 55:
        if(activeMode == 0):
            screen.blit(instructionText, [screen_width/5.5,screen_height/1.45])
        if(activeMode == 1):
            screen.blit(instructionText, [screen_width/6.5,screen_height/1.45])
        if(activeMode == 2):
            screen.blit(instructionText, [screen_width/5.5,screen_height/1.45])

    screen.blit(easyMode, [screen_width/2.5,screen_height/1.25])
    screen.blit(medMode, [screen_width/2.7,screen_height/1.25 + titleMenuSep])
    screen.blit(hardMode, [screen_width/2.5,screen_height/1.25 + titleMenuSep*2])

    if screenFlashTime == 20:
        Lists.introScreenList.add(p)
    if screenFlashTime > 20:
        if screenFlashTime == 160:
            p.changespeed(-1,0)
            p.update()

        if reducedTime %15 == 0:
            bulletLeft = bullets.bullet(bullets.bulletWidth,bullets.bulletHeight,0,bullets.straightSpeed,colors.BLUE,0,0)
            bulletRight = bullets.bullet(bullets.bulletWidth,bullets.bulletHeight,0,bullets.straightSpeed,colors.BLUE,0,0)
            bulletLeft.rect.x = p.rect.x
            bulletLeft.rect.y = p.rect.y
            bulletRight.rect.x = p.rect.x + 15-bullets.bulletWidth
            bulletRight.rect.y = p.rect.y
            Lists.introScreenListBullets.add(bulletLeft)
            Lists.introScreenListBullets.add(bulletRight)
            bullets.removeTitleBullets()

    Lists.introScreenList.update()
    Lists.introScreenList.draw(screen)
    Lists.introScreenListBullets.update()
    Lists.introScreenListBullets.draw(screen)
    if p.rect.x < 10:
        p.changespeed(1,0)
    if p.rect.x > screen_width - 20:
        p.changespeed(-1,0)


    titleScreenAnimation += 1
    screenFlashTime +=1

def modeSelect(change):
    global activeMode, modePossible
    if change > 0:
        activeMode += 1
    if change < 0:
        activeMode -= 1
    if activeMode > modePossible:
        activeMode = 0
    elif activeMode < 0:
        activeMode = modePossible

def process_events():
    global spaceHold, player, currHold,currHoldU,currHoldR,currHoldD,currHoldL, shotCount, game_over, playerColor
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
                currHold += currHoldL
                if spaceHold == False:
                    shotDir = shotDirL
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
                currHold += currHoldR
                if spaceHold == False:
                    shotDir = shotDirR
            elif event.key == pygame.K_UP:
                player.changespeed(0,-3)
                currHold += currHoldU
                if spaceHold == False:
                    shotDir = shotDirU
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,3)
                currHold += currHoldD
                if spaceHold == False:
                    shotDir = shotDirD
            elif event.key == pygame.K_SPACE:
                spaceHold = True
                if currHold != 0:
                    shotDir = currHold
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                #player = switchPlayerColor(player)
                if playerColor == 0:
                    playerColor = 1
                    newPlayer = player.Player(colors.RED, player.getX(), player.getY())
                    newPlayer.setSpeed(player.getChangeX(), player.getChangeY())
                    for p in Lists.player_list:
                        p.remove()
                        p.kill()
                    player = newPlayer
                    Lists.player_list.add(player)
                    Lists.all_sprites_list.add(player)
                elif playerColor == 1:
                    playerColor = 0
                    newPlayer = player.Player(colors.BLUE, player.getX(), player.getY())
                    newPlayer.setSpeed(player.getChangeX(), player.getChangeY())
                    for p in Lists.player_list:
                        p.remove()
                        p.kill()
                    player = newPlayer
                    Lists.player_list.add(player)
                    Lists.all_sprites_list.add(player)
#                     if game_over:
#                         #this resets to a new instance of the game if game over is true and the space bar is pressed
#                         self.__init__()

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                currHold -= currHoldL
                player.changespeed(3,0)
            elif event.key == pygame.K_RIGHT:
                currHold -= currHoldR
                player.changespeed(-3,0)
            elif event.key == pygame.K_UP:
                currHold -= currHoldU
                player.changespeed(0,3)
            elif event.key == pygame.K_DOWN:
                currHold -= currHoldD
                player.changespeed(0,-3)
            elif event.key == pygame.K_SPACE:
                shotCount = 0
                spaceHold = False

    #method that handles bullet generation. Spawning the bullets based on
    #current held directio  or last preivously held direction. Also has
    #a shot clock to prevent bullets from coming out as a constant stream
    if spaceHold:
        if wavePower:
            if shotCount == 0:
                bullets.fireWave(player)
                shotCount = 1
            elif shotCount == 15:
                shotCount = 0
            else:
                shotCount +=1
        else:
            if shotCount == 0:
                bullets.fireNorm(player)

                shotCount = 1
            elif shotCount == 8:
                shotCount = 0
            else:
                shotCount +=1
    if game_over:
        return True
    else:
        return False


