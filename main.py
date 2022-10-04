from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    """This class is used to create a player, and all of the player's capabilities."""
    
    def __init__(self, playerX, playerY, playerNum: int):
        self.playerColor = 255, 255, 255
        self.playerX = playerX
        self.playerY = playerY
        self.playerHeight = height * 0.15
        self.playerWidth = width * 0.0075
        self.heldKeys = []
        self.moveSpeed = float(height) * 0.0125
        self.playerOneControls = {
            pygame.K_w: 'w',
            pygame.K_s: 's',
            }
        self.playerTwoControls = {
            pygame.K_i: 'i',
            pygame.K_k: 'k'
        }
        self.playerControls = self.setControls(playerNum)
        pass


    def createLine(self):
        """Draw the player to the screen."""  
        
        player = pygame.draw.rect(screen, self.playerColor, pygame.Rect(float(self.playerX), float(self.playerY), self.playerWidth, self.playerHeight))

        return player

    def setControls(self, num) -> dict:
        """Set the controls of the player, so the events are individualized to their respective player number."""

        if num == 1:
            return self.playerOneControls
        
        if num == 2:
            return self.playerTwoControls



    def getEvents(self, i) -> list:
        """Keeps track of key presses/releases, and append/remove them from the list self.heldKeys[]."""

        try:
            if i.type == pygame.KEYDOWN: #Track key presses here
                self.heldKeys.append(self.playerControls[i.key])

            elif i.type == pygame.KEYUP: #Track key releases here
                self.heldKeys.remove(self.playerControls[i.key])
            
            return self.heldKeys

        except KeyError:
            return self.heldKeys


    def checkHeldKeys(self, events):
        """Check what keys are being pressed and call the movePaddle function."""

        keys = self.getEvents(events)

        if keys:
            for key in keys:
                if key in self.playerControls:
                    if key == self.playerControls[pygame.K_w] or self.playerControls[pygame.K_i]:
                        self.playerY = self.movePaddle('up')
                    
                    elif key == self.playerControls[pygame.K_s] or self.playerControls[pygame.K_k]:
                        self.playerY = self.movePaddle('dn')

        else:
            pass

        # Debugging code vvv
        print(keys)
        print(self.playerY)
    
    def movePaddle(self, direction: str):
        """Moves the paddle a certain direction."""

        if direction == 'up' and self.playerY > 0:
            self.playerY -= self.moveSpeed

        elif direction == 'dn' and self.playerY < (height - self.playerHeight):
            self.playerY += self.moveSpeed

        return self.playerY
        


                

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
playerTwoX = width - width * 0.0075

playerOne = Player(0, 0, playerNum = 1)
playerTwo = Player(playerTwoX, 0, playerNum = 2)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        playerOne.checkHeldKeys(event)
        playerTwo.checkHeldKeys(event)

    playerOne.createLine()
    playerTwo.createLine()
    
    
    pygame.display.flip()

