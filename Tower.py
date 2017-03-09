#Créé par Lee-Stenio
#from tkinter.test.support import pixels_conv
import helper
from helper import *


class Tower():
    def __init__(self):
        self.x=0
        self.y=0#centre
        self.sizeRadius = 8#pixels
        self.atkCooldown=10#nb de frames avant de pouvoir retirer
        self.atkSpeed=0
        self.atkPower=1
        self.range=100#pixels
        self.angle = 0
        
    def update(self):
        pass
    
    
    def findEnemy(self, enemyList):
        for i in range(len(enemyList)):
            pos=[enemyList[i].x, enemyList[i].y]
            if (self.inRange( pos[0], pos[1] )):
                self.angle=Helper.calcAngle( self.x, self.y, pos[0], pos[1] )
                #cet enlemy est dans le rayon
                break
            
            
    def inRange(self,x2, y2):
        #helper=Helper()
        ##Trouver le point le plus proche du cercle
        #closestX= clamp(self.x, x2-enemySize/2, x2+enemySize/2)
        #closestY= clamp(self.y, y2-enemySize/2, y2+enemySize/2)
        #distanceX = self.x - closestX;
        #distanceY = self.y - closestY;
        dist=Helper.calcDistance(self.x, self.y, x2, y2)
        if dist <= self.range:
            #print("col detected")
            return True;
        else:
            #print("col not detected")
            return False
    
    def clamp(self, x, min, max):
        if (x < min):
            x = min
        elif (x > max):
            x = max
    
        return x
    
    def setPos(self, x, y):
        self.x=x
        self.y=y

    def getPos(self):
        #pos= tow.getPos()
        #x = pos[0], y = pos[1]
        return [self.x, self.y]
    
    def getSizeRadius(self):
        return self.sizeRadius
    
    def getRange(self):
        return self.range
    
    
    
        
class Canon(Tower):
    def __init__(self, x, y):
        Tower.__init__(self)
        #balance numbers here
        self.atkPower = 50
        self.atkCooldown= 20
        self.range=90;
        self.setPos(x, y)