import settings as s
from settings import pygame
from settings import sys
from settings import ran
import numpy
from Circle import Circle

vec = s.VEC

class Bullet(Circle):
    def __init__(self,c = vec(0,0),v = vec(0,0),r = 1,col = s.GOLD):
        super().__init__(c,r,col)
        self.Vel = v
    def Update(self):
        super().Move()
        cx,cy = self.Center
        r =  self.Radius
        if cx > s.WIDTH + r or cx < -r or cy > s.HEIGHT + r or cy < -r:
            self.kill()
        self.Draw()
