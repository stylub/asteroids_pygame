import configuration.settings as s
from configuration.settings import pygame
from configuration.settings import sys
from configuration.settings import ran
import numpy
from actors.Circle import Circle

vec = s.VEC

class Meteor(Circle):
    def __init__(self,c = vec(0,0),v = vec(0,0),r = 1,col = s.GOLD):
        self.Vel = v
        len_v = self.Vel.length()
        max_v = 7.0
        Colors = [(255, 219, 0),(248, 186, 9),(241, 154, 17),
                  (233, 121, 26),(226, 88, 34),(196, 39, 39)]
        col = Colors[int((len_v/max_v)*6)-1]
        super().__init__(c,r,col)

    def Explode(self,vel):
        if(self.Radius > 25):
            u_vel =  vel / numpy.linalg.norm(vel)
            x,y = self.Vel
            mag = numpy.sqrt(x*x + y*y)
            u_vel *= mag
            x, y = u_vel
            n1 = vec(y,-x)
            n2 = vec(-y,x)
            cx,cy = self.Center
            m1 = Meteor(vec(cx,cy),n1,self.Radius/2,s.WHITE)
            m2 = Meteor(vec(cx,cy),n2,self.Radius/2,s.RED)
            return [m1,m2]
        return []
 