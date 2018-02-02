import pygame
import sys
import time
from UltraColor import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

fps_font = pygame.font.Font("/Users/brianfreeman/Downloads/Albow-2.2.0/demo/Resources/fonts/Vera.ttf", 20)

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Winter"

    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")


create_window()
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            isRunning = False

    #  Render graphics.
    window.fill(Color.Black)
    show_fps()





    pygame.display.update()

pygame.quit()
sys.exit()