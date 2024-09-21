#pgzero

WIDTH = 600 # Window width
HEIGHT = 300 # Window height

TITLE = "Alien Runner" # Title for the game window
FPS = 30 # Number of frames per second

#create a character here
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))

def draw():
    background.draw()
    alien.draw()
    
def update(dt):
    alien.x = alien.x + 5
