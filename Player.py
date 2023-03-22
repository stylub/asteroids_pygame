import settings as s
from settings import pygame
from settings import sys
from settings import ran
from Triangle import Triangle
from Bullet import Bullet
import numpy

vec = s.VEC
displaysurface = s.DisplaySurface

class Player(Triangle):
    def __init__(self):
        super().__init__()
        self.Vel = vec(0,0)
        self.MAX_SPEED = 3
        self.wait = 0.0 
    def Shoot(self):
        return Bullet(self.Points[2],self.GetDirVec() * 30,5)
    def Move(self):
        pk = pygame.key.get_pressed()
        if pk[s.K_LEFT]:
            self.RotTriangle(-8)     
        if pk[s.K_RIGHT]:
            self.RotTriangle(8)    
        if pk[s.K_UP]:
            v = self.GetDirVec()
            vx = self.Vel[0] + v[0]
            vy = self.Vel[1] + v[1]
            if abs(vx) < self.MAX_SPEED:
                self.Vel[0] = vx
            if abs(vy) < self.MAX_SPEED:
                self.Vel[1] = vy
        if pk[s.K_DOWN]:
            v = self.GetDirVec()
            vx = self.Vel[0] - v[0]
            vy = self.Vel[1] - v[1]
            if abs(vx) < self.MAX_SPEED:
                self.Vel[0] = vx
            if abs(vy) < self.MAX_SPEED:
                self.Vel[1] = vy
        if pk[s.K_SPACE] and self.wait > 200:
            self.wait = 0
            return self.Shoot()
        else:   self.pressed = False 
    def Update(self,time):
        self.wait += time
        b = self.Move()
        super().Update()
        return b

        
        
        
        