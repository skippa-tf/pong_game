from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    
    def __init__(self, left, top):
        self.white = 255, 255, 255
        self.left = left
        self.top = top
        pass

    def createLine(self):
        player = pygame.draw.rect(screen, self.white, pygame.Rect(self.left, self.top, 3, 30))
        return player


size = width, height = 400, 200
screen = pygame.display.set_mode(size)

player_one = Player(0, 0)
player_two = Player(397, 0)
player_one.createLine()
player_two.createLine()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    pressed = pygame.key.get_pressed()
#https://gamedev.stackexchange.com/questions/198635/how-to-make-objects-move-continuously-while-a-key-is-pressed-in-pygame
    if pressed[pygame.K_w]:
        print("W")

    elif pressed[pygame.K_s]:
        print("S")

    elif pressed[pygame.K_UP]:
        print("UP")
    
    elif pressed[pygame.K_DOWN]:
        print("DOWN")


    pygame.display.flip()

