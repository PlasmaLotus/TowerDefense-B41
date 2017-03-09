#Créé Par Lee-Stenio
import Point
from Point import *

class Path:
    def __init__(self, x, y, x2, y2, length):
        self.startX = x
        self.startY = y
        self.endX = x2
        self.endY = y2
        self.length= length #
        
    def isOnPath(self, x, y):
        if (x == self.startX or x == self.endX or y == self.startY or y == self.endY ):
            return True
        else:
            return False
        
    def getStart(self):
        return Point(self.startX, self.startY)
        #return [self.startX, self.startY] 
    def getEnd(self):
        return Point(self.endX, self.endY)
        #return [self.endX, self.endY]