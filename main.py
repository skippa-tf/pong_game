from contextlib import nullcontext
import sys, pygame
pygame.init()

class Player():
    """This class is used to create a player, and all of the player's capabilities."""
    
    def __init__(self, playerX, playerY):
        self.white = 255, 255, 255
        self.playerX = playerX
        self.playerY = playerY
        self.heldKeys = []
        pass


    def createLine(self):
        """Draw the player to the screen."""  
        player = pygame.draw.rect(screen, self.white, pygame.Rect(self.playerX, self.playerY, 3, 30))

        return player


    def getEvents(self):
        """Keeps track of key presses/releases, and append/remove them from the list self.heldKeys[]."""

        for i in pygame.event.get():
            if i.type==pygame.KEYDOWN: #Track key presses here
                
                if i.key==pygame.K_w:
                    self.heldKeys.append('w')
                
                if i.key==pygame.K_s:
                    self.heldKeys.append('s')
                
                if i.key==pygame.K_UP:
                    self.heldKeys.append('UP')
                
                if i.key==pygame.K_DOWN:
                    self.heldKeys.append('DOWN')

                else:
                    pass
            elif i.type==pygame.KEYUP: #Track key releases here

                if i.key==pygame.K_w:
                    self.heldKeys.remove('w')
                
                if i.key==pygame.K_s:
                    self.heldKeys.remove('s')
                
                if i.key==pygame.K_UP:
                    self.heldKeys.remove('UP')
                
                if i.key==pygame.K_DOWN:
                    self.heldKeys.remove('DOWN')

                else:
                    pass
            
            return self.heldKeys

    def checkHeldKeys(self):
        """Check the keys in heldKeys[] and move accordingly."""
        for i in self.heldKeys:
            if 'w' in self.heldKeys:
                self.playerY -= 1
            
            elif 's' in self.heldKeys:
                self.playerY += 1
            
            elif 'UP' in self.heldKeys:
                self.playerY -= 1
            
            elif 'DOWN' in self.heldKeys:
                self.playerX += 1
        print(self.heldKeys)
                

size = width, height = 400, 200
screen = pygame.display.set_mode(size)

player_one = Player(0, 0)
player_two = Player(397, 0)
player_one.createLine()
player_two.createLine()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    player_one.getEvents()
    player_one.checkHeldKeys()


    pygame.display.flip()

