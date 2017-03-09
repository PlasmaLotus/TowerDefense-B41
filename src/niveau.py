# coding: utf-8
from lib.map import *

#Créé Par Lee-Stenio

#le Niveau contient une map et les waves du niveau (liste d'enemies par wave)
class Niveau:
    def __init__(self):
        self.map=Map()
        #self.enemyList=[]
        self.waves=[]
        self.nextEnemy=0
        self.spawnDelay=0#frames
        self.maxSpawnDelay=60
        
        
    def spawnEnemy(self):
        self.spawnDelay+=1
        if (self.spawnDelay >= self.maxSpawnDelay):
            self.spawnDelay=0
            return True
        else:
            return False
        
        
    def getEnemy(self):
        enemy=self.nextEnemy
        self.nextEnemy+=1
        return enemyList[enemy]
    
    def getMap(self):
        return self.map
    
    
class NiveauDebug(Niveau):
    def __init__(self):
        super()
        self.map=MapPreset1()
        