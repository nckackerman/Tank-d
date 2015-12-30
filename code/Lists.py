import pygame

Good_block_list = pygame.sprite.Group()
Enemy_list = pygame.sprite.Group()
Bad_block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bullet_hit_list = pygame.sprite.Group()

triangle_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
circle_list = pygame.sprite.Group()

fatty_list = pygame.sprite.Group()
bluefatty_list = pygame.sprite.Group()
redfatty_list = pygame.sprite.Group()

straffer_list = pygame.sprite.Group()
bluestraffer_list = pygame.sprite.Group()
redstraffer_list = pygame.sprite.Group()

fourSquare_list = pygame.sprite.Group()
blue_fourSquare_list = pygame.sprite.Group()
red_fourSquare_list = pygame.sprite.Group()
introScreenList = pygame.sprite.Group()
introScreenListBullets = pygame.sprite.Group()
blue_bullet_list = pygame.sprite.Group()
blue_bullet_hit_list = pygame.sprite.Group()
red_bullet_list = pygame.sprite.Group()
red_bullet_hit_list = pygame.sprite.Group()
Blue_Enemy_list = pygame.sprite.Group()
Red_Enemy_list = pygame.sprite.Group()
deathCircle_list = pygame.sprite.Group()
haz_list = pygame.sprite.Group()
pointFade_List = []
startAnimateTimes_list = []
removePointLists = []

def reset():
    for player in player_list:
        player.kill()
    for thisBullet in bullet_list:
        thisBullet.kill()
    for goodBlock in Good_block_list:
        goodBlock.kill()
    for enemy in Enemy_list:
        enemy.kill()
    for badBlock in Bad_block_list:
        badBlock.kill()
    for sprites in all_sprites_list:
        sprites.kill()
    for bulletHits in bullet_hit_list:
        bulletHits.kill()
    for thisTriangle in triangle_list:
        thisTriangle.kill()
    for thisCircle in circle_list:
        thisCircle.kill()
    for thisFatty in fatty_list:
        thisFatty.kill()
    for thisStraffer in straffer_list:
        thisStraffer.kill()
    for thisfourSquare in fourSquare_list:
        thisfourSquare.kill()
    for thisDC in deathCircle_list:
        thisDC.kill()
    while len(pointFade_List) != 0:
        pointFade_List.pop()
    while len(startAnimateTimes_list) != 0:
        startAnimateTimes_list.pop()
