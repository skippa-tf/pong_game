from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    """This class is used to create a player, and all of the player's capabilities."""
    
    def __init__(self, playerX, playerY, playerNumber):
        self.white = 255, 255, 255
        self.playerX = playerX
        self.playerY = playerY
        self.playerNumber = playerNumber
        self.heldKeys = []
        self.moveSpeed = 5

        pass


    def createLine(self):
        """Draw the player to the screen."""  
        player = pygame.draw.rect(screen, self.white, pygame.Rect(self.playerX, self.playerY, 3, 30))

        return player


    def getEvents(self, i) -> list:
        """Keeps track of key presses/releases, and append/remove them from the list self.heldKeys[]."""
        
        if self.playerNumber == 1:
            if i.type == pygame.KEYDOWN: #Track key presses here
                if i.key == pygame.K_w:
                    self.heldKeys.append('w')

                if i.key == pygame.K_s:
                    self.heldKeys.append('s')

                else:
                    pass
            elif i.type == pygame.KEYUP: #Track key releases here
                if i.key == pygame.K_w:
                    self.heldKeys.remove('w')

                if i.key == pygame.K_s:
                    self.heldKeys.remove('s')

                else:
                    pass
        else:
            if i.type == pygame.KEYDOWN: #Track key presses here

                if i.key == pygame.K_UP:
                    self.heldKeys.append('UP')

                if i.key == pygame.K_DOWN:
                    self.heldKeys.append('DOWN')
                else:
                    pass
            elif i.type == pygame.KEYUP: #Track key releases here

                if i.key == pygame.K_UP:
                    self.heldKeys.remove('UP')

                if i.key == pygame.K_DOWN:
                    self.heldKeys.remove('DOWN')
                else:
                    pass
        return self.heldKeys

    def checkHeldKeys(self, events):
        """Check the keys in keys and move accordingly."""

        keys = self.getEvents(events)

        if keys:
            if int(self.playerY) <= 196:
                for key in keys:
                    if 'w' in keys:
                        self.playerY -= self.moveSpeed

                    elif 's' in keys:
                        self.playerY += self.moveSpeed

                    elif 'UP' in keys:
                        self.playerY -= self.moveSpeed

                    elif 'DOWN' in keys:
                        self.playerY += self.moveSpeed
            else:
                pass
        print(keys) # for debugging
                

size = width, height = 400, 200
screen = pygame.display.set_mode(size)

playerOne = Player(0, 0, 1)
playerTwo = Player(397, 0, 2)


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        playerOne.checkHeldKeys(event)
        playerTwo.checkHeldKeys(event)

    playerOne.createLine()
    playerTwo.createLine()
    
    
    pygame.display.flip()

