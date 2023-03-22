import settings as s
from settings import pygame
from settings import sys
from settings import ran
import numpy

vec = s.VEC
displaysurface = s.DisplaySurface

class Circle(pygame.sprite.Sprite):
    def __init__(self,c = vec(0,0),r = 1,col = s.RED):
        super().__init__()
        self.Center = c
        self.Radius = r
        self.Color = col
        vx = s.ran.randint(0,10) - 5
        vy = s.ran.randint(0,10) - 5
        self.Vel = vec(vx,vy)
    def Draw(self):
        pygame.draw.circle(displaysurface,s.GRAY,self.Center,self.Radius)
        pygame.draw.circle(displaysurface,self.Color,self.Center,self.Radius - 3)
    def Move(self):
        self.Center += self.Vel
    def MoveBy(self,dir):
        self.Center +=dir
    def CollideB(self,C):
        dis = [self.Center[0] - C.Center[0],self.Center[1] - C.Center[1]]
        dis = numpy.linalg.norm(dis)
        range = float(self.Radius + C.Radius)
        if dis < range:
            return True
        else:
            return False
    def Update(self):
        self.Move()
        cx,cy = self.Center
        r =  self.Radius
        if cx > s.WIDTH + r:
            self.Center.x = -r
        if cx < -r:
            self.Center.x = s.WIDTH + r
        if cy > s.HEIGHT + r:
            self.Center.y = -r
        if cy < -r:
            self.Center.y = s.HEIGHT + r
        self.Draw()