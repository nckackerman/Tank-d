import pygame
import colors
import Lists

class pointGains(pygame.sprite.Sprite):

    def __init__(self,color,x,y,value,startTime,pg):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([25, 20])
        self.image.fill(color)
        self.image.set_colorkey(color)
        self.image.blit(pg, [0,0])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startTime = startTime
        self.image = self.image.convert()



    def update(self):
        if (pygame.time.get_ticks() - self.startTime >= 700):
            self.kill()
def spawnNewPoints(color,x,y,value,startTime,pg):

    newPoints = pointGains(color,x,y,value,startTime,pg)
    Lists.all_sprites_list.add(newPoints)



