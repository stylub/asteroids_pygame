import pygame,sys
from turtle import Vec2D, circle
import pygame,sys
from pygame.locals import *
from cmath import cos
from cmath import sin
from math import pi
import random as ran

def Process(t):
    i = 0
    while t[i] != ' ':
        i+=1
    return t[i+1:len(t)]



HEIGHT = 640
WIDTH = 900
ACC = 0.5
FPS = 30

def Update():    
    f = open('settings.txt','r')
    HEIGHT = int(Process(f.readline()))
    WIDTH = int(Process(f.readline()))
    ACC = float(Process(f.readline()))
    FPS = int(Process(f.readline()))
    f.close()

VEC = pygame.math.Vector2  # 2 for two dimensional
pygame.font.init() 
MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
BIG_FONT = pygame.font.SysFont('Comic Sans MS', 100)
DisplaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GOLD = (255, 215, 0)
GRAY = (72, 72, 80)
