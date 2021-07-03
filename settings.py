import timeit

import pygame
from pyglet import font

font.add_file('gui/main.ttf')
mainFont = font.load('gui/main.ttf', 15)

pygame.init()

monitor = pygame.display.Info()
WIDTH = 927
HEIGHT = 566
MAX_FPS = 100
PAUSE = True
IN_MENU = True
VERSION = "Alpha 0.1.4 Textures Test"
clock = pygame.time.Clock()

DiscordRP = True

FOV = 100
RENDER_DISTANCE = 100

CHUNKS_RENDER_DISTANCE = 900
CHUNK_SIZE = (4, 60, 4)