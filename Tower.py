#Créé par Lee-Stenio
#from tkinter.test.support import pixels_conv
import helper
from helper import *


class Tower():
    def __init__(self):
        self.x=0
        self.y=0#centre
        self.sizeRadius = 8#pixels
        self.atkCooldown=0
        self.atkSpeed=10#nb de frames avant de pouvoir retirer
        self.atkPower=1
        self.range=100#pixels
        self.angle = 0 #purement cosmetique pour l'instant
        self.canShoot=False
        
    def update(self):
        if (self.canShoot == False):
            self.atkCooldown-=1
            if (self.atkCooldown <= 0):
                self.canShoot=True;
                self.atkCooldown = self.atkSpeed
    
    
    def findEnemy(self, enemyList):
        for i in range(len(enemyList)):
            #de cette façon, le premier enemy sera choisi
            pos=[enemyList[i].x, enemyList[i].y]
            if (self.inRange( pos[0], pos[1] )):
                #cet enlemy est dans le rayon
                self.angle=Helper.calcAngle( self.x, self.y, pos[0], pos[1] )
                self.shoot( enemyList[i] )
                break
            
            
    def inRange(self,x2, y2):

        dist=Helper.calcDistance(self.x, self.y, x2, y2)
        if dist <= self.range:
            #print("col detected")
            return True;
        else:
            #print("col not detected")
            return False

    
    def shoot(self, enemy):
        if (self.canShoot == True):
            #enemy.hp -= self.atkPower
            print("Tower shot")
            self.canShoot = False
    
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
        self.atkSpeed= 20
        self.range=90;
        self.setPos(x, y)
        
        
        