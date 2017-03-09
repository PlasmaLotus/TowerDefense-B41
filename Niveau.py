import Map
from Map import *

#Créé Par Lee-Stenio

#le Niveau contient une map et les waves du niveau (liste d'enemies par wave)
class Niveau:
    def __init__(self):
        self.map=Map()
        #self.enemyList=[]
        self.waves=[]
        self.nextEnemy=0
        self.spawnDelay=0#frames
        self.maxSpawnDelay=100
        
    def update(self):
        self.spawnDelay+=1
        if (self.spawnDelay >= self.maxSpawnDelay):
            self.spawnDelay=0
            return True
        else:
            return False
        
    def getNextEnemy(self, wave):
        ##TODO::
        enemy=self.nextEnemy
        self.nextEnemy+=1
        #return self.waves[wave][enemy]
        return Creep()

    def hasEnemies(self, wave):
        ##TODO:
        if (len(self.waves) > 0):
            return True
        else:
            return False
    
    
class NiveauDebug(Niveau):
    def __init__(self):
        #super()
        Niveau.__init__(self)
        self.map=MapPreset1()
        