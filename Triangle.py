import settings as s
from settings import pygame
from settings import sys
from settings import ran
import numpy


vec = s.VEC

class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Points = []
        self.Center = vec(0,0)
        self.R = 1
        self.Color = s.WHITE
    def GetAreaT(self,P):
        A,B,C = P
        AB = [B[0] - A[0],B[1] - A[1]]
        AC = [C[0] - A[0],C[1] - A[1]]
        cross = AB[0] * AC[1] - AB[1] * AC[0]
        return abs(cross)/2
    def GetCenter(self):
        x = 0
        y = 0
        for i in range(len(self.Points)):
            x += self.Points[i][0]
            y += self.Points[i][1]
        x = int(x/3)
        y = int(y/3)
        self.Center = vec(x,y)
    def GetTriangle(self,x,y,r=100):
        self.Points=[vec(x-r,y),vec(x+r,y),vec(x,y-r*2)]
        self.GetCenter()
    def CheckInside(self,P):
        p1,p2,p3 = self.Points
        A = self.GetAreaT(self.Points)
        APB = self.GetAreaT([p1,p2,P])
        BPC = self.GetAreaT([p2,p3,P])
        CPA = self.GetAreaT([p3,p1,P])
        if abs(A - (APB + BPC + CPA)) < 10:
            return True
        else: 
            return False
    def GetDirVec(self):
        midx = (self.Points[0][0] + self.Points[1][0])/2
        midy= (self.Points[0][1] + self.Points[1][1])/2
        dirx = self.Points[2][0] - midx
        diry = self.Points[2][1] - midy
        dir = vec(dirx,diry)
        u_dir = dir / numpy.linalg.norm(dir)
        return u_dir
    def GetDirection(self):
        dirx,diry = self.GetDirVec()
        angle = 0
        if(dirx == 0):
            if diry < 0: angle = s.pi/2
            else: angle = s.pi + s.pi/2
        else: angle = numpy.arctan(abs(diry)/abs(dirx))
        if dirx > 0 and diry < 0: 
            angle = angle
        elif dirx < 0 and diry <0:
            angle = s.pi - angle
        elif dirx < 0 and diry > 0:
            angle = s.pi + angle
        elif dirx > 0 and diry > 0:
            angle = (2 * s.pi) - angle
        return angle
    def RotPoint(self,x1,y1,x2,y2,alfa):
        x = (x1-x2) * s.cos(alfa) - (y1 - y2) * s.sin(alfa) + x2
        y = (x1-x2) * s.sin(alfa) + (y1 - y2) * s.cos(alfa) + y2
        x = x.real
        y = y.real
        return vec(x,y)
    def RotTriangle(self,angl):
        self.GetCenter()
        a = angl * (s.pi/180)
        for i in range(len(self.Points)):
            x1, y1 = self.Points[i]
            x2, y2 = self.Center
            self.Points[i] = self.RotPoint(x1,y1,x2,y2,a)
    def Foward(self,vel):
        angle = self.GetDirection()
        for i in range(len(self.Points)):
            x, y = self.Points[i]
            x += s.cos(abs(angle)) * vel
            y += s.sin(abs(angle)) * vel
            x = x.real
            y = y.real
            self.Points[i] = (x,y)
    def MoveBy(self,dir):
        dirx,diry = dir
        for i in range(len(self.Points)):
            x, y = self.Points[i]
            x += dirx
            y += diry
            self.Points[i] = (x,y)    
    def Collide(self,pos,r):
        x,y = pos
        dir = vec(self.Center[0] - x,self.Center[1] - y)
        u_dir = dir / numpy.linalg.norm(dir)
        point = pos + u_dir * r
        point[0] = int(point[0])
        point[1] = int(point[1])
        return self.CheckInside(point)
    def Draw(self):
        p = []
        for i in range(len(self.Points)):
            p.append((int(self.Points[i][0]),int(self.Points[i][1])))
        pygame.draw.polygon(s.DisplaySurface,self.Color,p)
    def Update(self):
        self.MoveBy(self.Vel) 
        self.GetCenter()
        cx,cy = self.Center
        r =  self.R * 2
        if cx > s.WIDTH + r:
            self.MoveBy([-(s.WIDTH + r*2),0])
        if cx < -r:
            self.MoveBy([(s.WIDTH + r*2),0])
        if cy > s.HEIGHT + r:
            self.MoveBy([0,-(s.HEIGHT+ r*2)])
        if cy < -r:
            self.MoveBy([0,s.HEIGHT+ r*2])
        self.Draw()