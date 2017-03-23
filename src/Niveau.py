import Map
from Map import *

from Creep import *

#Créé Par Lee-Stenio

#le Niveau contient une map et les waves du niveau (liste d'enemies par wave)
class Niveau:
    def __init__(self):
        self.map=Map()
        #self.enemyList=[]
        self.wave = 1
        self.baseNbEnemies = 15
        self.nbEnemies = 1
        self.spawnDelay=0#frames
        self.creepHPScaling = 1 ##Ajout de HP a chaque vague
        self.creepSpeedScaling = 1 ##ajout de Speed a chaque vague
        self.spawnScaling = 1##réduction de tenps entre le spawn de creeps
        self.maxSpawnDelay=50##Delai de mise a jour avant d'ajouter un creep
        self.minSpawnDelay = 10##delai minimum
        self.creepHP = 1
        self.creepSpeed = 1
        
        
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
    
    def reset(self):
        self.nbEnemies = self.baseNbEnemies
        self.spawnDelay = 0

    def nextWave(self):
        self.reset()
        self.wave+= 1
        self.creepHP+= self.creepHPScaling
        self.creepSpeed+= self.creepSpeedScaling
        
        ##Augmente la vitesse de spawn a chaque 5 wave
        if self.wave %5 == 0:
            self.maxSpawnDelay -= 2
            if self.maxSpawnDelay < self.minSpawnDelay:
                self.maxSpawnDelay = self.minSpawnDelay
        #print("NextWave")
        
    
class NiveauDebug(Niveau):
    def __init__(self):
        #super()
        Niveau.__init__(self)
        self.map=MapPreset1()
        self.creepHP = 100
        self.creepSpeed = 7
        self.nbEnemies = 5
        self.baseNbEnemies = 15
        self.creepHPScaling = 10
        self.creepSpeedScaling = 1
        #self.waves[0] = ["creep","creep","creep","creep","creep"]
        