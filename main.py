from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    """This class is used to create a player, and all of the player's capabilities."""
    
    def __init__(self, playerX, playerY):
        self.playerColor = 255, 255, 255
        self.playerX = playerX
        self.playerY = playerY
        self.playerHeight = height * 0.15
        self.playerWidth = width * 0.0075
        self.playerNumber = playerNumber
        self.heldKeys = []
        self.moveSpeed = height * 0.0125
        self.Controls = {
            pygame.K_w: 'w',
            pygame.K_s: 's',
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN'
            }
        pass


    def createLine(self):
        """Draw the player to the screen."""  
        player = pygame.draw.rect(screen, self.playerColor, pygame.Rect(self.playerX, self.playerY, self.playerWidth, self.playerHeight))

        return player


    def getEvents(self, i) -> list:
        """Keeps track of key presses/releases, and append/remove them from the list self.heldKeys[]."""
        
        if i.type == pygame.KEYDOWN: #Track key presses here
            self.heldKeys.append(self.Controls[i.key])
        
        elif i.type ==pygame.KEYUP:
            self.heldKeys.remove(self.Controls[i.key])

        return self.heldKeys

    def checkHeldKeys(self, events):
        """Check what keys are being pressed and call the movePaddle function."""

        keys = self.getEvents(events)

        if keys:
            for key in keys:
                if 'w' or 'UP' in keys:
                    self.movePaddle('up')
                    
                elif 's' or 'DOWN' in keys:
                    self.movePaddle('down')

        else:
            pass

        print(keys)
        print(self.playerY) # for debugging
    
    def movePaddle(self, direction):
        """Moves the paddle a certain direction."""

        if direction == 'up' and self.playerY > 0:
            self.playerY -= self.moveSpeed

        elif direction == 'down' and self.playerY < (height - self.playerHeight):
            self.playerY += self.moveSpeed

                

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
playerTwoX = width - width * 0.0075

playerOne = Player(0, 0)
playerTwo = Player(playerTwoX, 0)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        playerOne.checkHeldKeys(event)
        playerTwo.checkHeldKeys(event)

    playerOne.createLine()
    playerTwo.createLine()
    
    
    pygame.display.flip()

