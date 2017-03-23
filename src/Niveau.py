import Map
from Map import *

from Creep import *

#Créé Par Lee-Stenio

#le Niveau contient une map et les waves du niveau (liste d'enemies par wave)
class Niveau:
    def __init__(self):
        self.map=Map()
        #self.enemyList=[]
        self.waves=[]
        self.nbEnemies = 5
        self.spawnDelay=0#frames
        self.maxSpawnDelay=50
        self.creepHP = 100
        self.creepSpeed = 20
        
        
    def update(self):
        self.spawnDelay+=1
        if (self.spawnDelay >= self.maxSpawnDelay):
            self.spawnDelay=0
            return True
        else:
            return False
        
    def getNextEnemy(self, wave):
        self.nbEnemies-=1
        #return self.waves[wave][enemy]
        return Creep(self.map.pathPointList, self.creepHP, self.creepSpeed)

    def hasEnemies(self, wave):
        ##TODO:
        if (self.nbEnemies > 0):
            return True
        else:
            return False
    
    
class NiveauDebug(Niveau):
    def __init__(self):
        #super()
        Niveau.__init__(self)
        self.map=MapPreset1()
        #self.waves[0] = ["creep","creep","creep","creep","creep"]
        