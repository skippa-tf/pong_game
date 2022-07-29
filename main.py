import sys, pygame
pygame.init()

size = width, height = 400, 200
screen = pygame.display.set_mode(size)


class Player():
    
    def __init__(self):
        self.white = 255, 255, 255
        pass

    def createLine(self, left, top):
        player = pygame.draw.rect(screen, white, pygame.Rect(left, top, 3, 30))
        return player

player_one = pygame.draw.rect(screen, white, pygame.Rect(0, 0, 3, 30))
player_two = pygame.draw.rect(screen, white, pygame.Rect(397, 0, 3, 30))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    


    if pygame.KEYDOWN():


    pygame.display.flip()

