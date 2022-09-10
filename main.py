from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    """This class is used to create a player, and all of the player's capabilities."""
    
    def __init__(self, playerX, playerY, playerNumber):
        self.white = 255, 255, 255
        self.playerX = playerX
        self.playerY = playerY
        self.playerHeight = height * 0.15
        self.playerWidth = width * 0.0075
        self.playerNumber = playerNumber
        self.heldKeys = []
        self.moveSpeed = height * 0.0125

        pass


    def createLine(self):
        """Draw the player to the screen."""  
        player = pygame.draw.rect(screen, self.white, pygame.Rect(self.playerX, self.playerY, self.playerWidth, self.playerHeight))

        return player


    def getEvents(self, i) -> list:
        """Keeps track of key presses/releases, and append/remove them from the list self.heldKeys[]."""
        
        if self.playerNumber == 1:
            if i.type == pygame.KEYDOWN: #Track key presses here
                if i.key == pygame.K_w:
                    self.heldKeys.append('w')

                elif i.key == pygame.K_s:
                    self.heldKeys.append('s')

                else:
                    pass
            elif i.type == pygame.KEYUP: #Track key releases here
                if i.key == pygame.K_w:
                    self.heldKeys.remove('w')

                elif i.key == pygame.K_s:
                    self.heldKeys.remove('s')

                else:
                    pass
        else:
            if i.type == pygame.KEYDOWN: #Track key presses here

                if i.key == pygame.K_UP:
                    self.heldKeys.append('UP')

                elif i.key == pygame.K_DOWN:
                    self.heldKeys.append('DOWN')
                else:
                    pass
            elif i.type == pygame.KEYUP: #Track key releases here

                if i.key == pygame.K_UP:
                    self.heldKeys.remove('UP')

                elif i.key == pygame.K_DOWN:
                    self.heldKeys.remove('DOWN')
                else:
                    pass
        return self.heldKeys

    def checkHeldKeys(self, events):
        """Check what keys are being pressed and call the movePaddle function."""

        keys = self.getEvents(events)

        if keys:
            if 0 <= self.playerY < int(size[1] - self.playerHeight):
                #for key in keys:
                if 'w' or 'UP' in keys:
                    self.movePaddle('up')
                elif 's' or 'DOWN' in keys:
                    self.movePaddle('down')

        else:
            pass
        print(keys) # for debugging
    
    def movePaddle(self, direction):
        """Moves the paddle a certain direction."""

        if direction == 'up':
            self.playerY -= self.moveSpeed

        else:
            self.playerY += self.moveSpeed

                

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

playerOne = Player(0, 0, 1)
playerTwo = Player(width - width * 0.0075, 0, 2)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        playerOne.checkHeldKeys(event)
        playerTwo.checkHeldKeys(event)

    playerOne.createLine()
    playerTwo.createLine()
    
    
    pygame.display.flip()

