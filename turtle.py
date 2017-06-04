import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple


class Turtle:
    def __init__(self,xwidth=400,ywidth=400):
        self.initstate()
        self.initgfx(xwidth,ywidth)

    def initstate(self):
        self.pos = np.array((0,0))
        # heading is a unit vector
        self.heading = np.array((1,0)) 
        self.pen = True
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0
        
    def reset(self):
        self.initstate()
        self.ax.clear()
        
    def forward(self,distance):
        old = self.pos
        self.pos = old + distance*self.heading
        if self.pen:
            self.update_bbox()
            self.drawline(old, self.pos)
        
    def back(self,distance):
        self.forward(-distance)
        
    def left(self,angle):
        self.heading = rotate(self.heading,angle)
        
    def right(self,angle):
        self.left(-angle)
        
    def penup(self):
        self.pen = False
        
    def pendown(self):
        self.pen = True

    def update_bbox(self):
        x,y = self.pos
        self.minx = min(x,self.minx)
        self.maxx = max(x,self.maxx)
        self.miny = min(y,self.miny)
        self.maxy = max(y,self.maxy)

    def clip(self,border=0):
        self.ax.set_xlim(self.minx-border,self.maxx+border)
        self.ax.set_ylim(self.miny-border,self.maxy+border)


    def initgfx(self,xwidth,ywidth):
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.set_xlim(-xwidth,xwidth)
        ax.set_ylim(-ywidth,ywidth)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal')
        self.fig = fig
        self.ax = ax

    def drawline(self,start,end):
        self.ax.plot([start[0],end[0]],
                     [start[1],end[1]],
                     '-b')

        

def rotate(v,degrees):
    theta = degrees * 2*np.pi / 360
    return np.cos(theta)*v + np.sin(theta)*perp(v)

def perp(v):
    return np.array([-v[1], v[0]])
