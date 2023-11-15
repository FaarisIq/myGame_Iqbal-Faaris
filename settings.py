# This file was created by: Faaris Iqbal
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 40

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREEN = (38, 69, 11)

# add platforms
PLATFORM_LIST = [(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"moving"),
                 (125, HEIGHT - 300, 100, 20, "moving"),
                 (250, 250, 100, 20, "moving"),
                 (175, 100, 50, 20, "moving")]