
from map import Map, MapPreset1

#Created Par Lee-Stenio

#le Niveau contient une map et les waves du niveau (liste d'enemies par wave)
class Niveau(object):
    def __init__(self):
        self.map = Map()
        self.waves = []
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
        #self.waves[0] = ["creep","creep","creep","creep","creep"]
        