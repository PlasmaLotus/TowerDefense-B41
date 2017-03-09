#Créé Par Lee-Stenio

import Map
from Map import *
#class Tile():
import Niveau
from Niveau import *

import Creep
from Creep import *

import Tower
from Tower import *
from _overlapped import NULL


## AKA "Modele" ## 
class Game():
	##Crée par Lee-Stenio
    def __init__(self):

        self.currentNiveau=Niveau()
        self.noCurrentNiveau=1 # valsur du niveau courrant
        self.currentWave=1 # valsuer de la wave courrante
        self.nbEnemies=0
        self.enemyList=[]# liste d'enemies vivants dans le jeu
        self.towerList=[]# liste des tours actives
        #self.map=Map()
        self.HP = 1 # vie du joueur?
        self.universalId = -1
        self.gold = 500

    
    #/ initialise le niveau et toutes ses composante ##    
    def init(self):
        
        #self.NiveauHandler.getNiveau(self.niveauIt)
        self.currentNiveau=NiveauDebug()
        self.hp=5
        self.enemyList=[]  
        self.towerList=[]
        ##Test##     
        self.testInitEnemy()
        self.testInitTower()

        #self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)
    
    
    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for i in range(len(self.towerList) ):
        	self.towerList[i].findEnemy(self.enemyList)
        	self.towerList[i].update() 
        
        for i in range(len(self.enemyList) ):
            ##self.enemyList[i].update()
            enemyPos = [self.enemyList[i].x, self.enemyList[i].y]
            if (enemyPos == self.currentNiveau.map.getEnd()):
            	print("Enemy Breach")
            	self.hp-=1
          
        #self.handleEnemySpawn()  

        if (self.hp <= 0):
            return False
            
        self.showDebugMap()
        return True

    def createTower(self, towerType, x, y):
    	towerPrice = 0
    	newTower = Tower()
    	#type de donnée de towerType a définir
    	if (towerType == "Canon"):
    		towerPrice = Canon.getPrice()
    		newTower = Canon(self.getUniqueId(), x, y)
    		
    	if (self.gold >= towerPrice):
    		self.towerList.append(newTower)
    		return True
    	else:
    		return False
    		
	#gère l'addition d'énemis dans le temps
    def handleEnemySpawn(self):
    	if (self.currentNiveau.hasEnemies(self.currentWave) == True):
    		if(self.currentNiveau.update() == True):
    			nextEnemy = self.currentNiveau.getNextEnemy(self.currentWave)
    			self.enemyList.append( nextEnemy )
    
    #Trouver l'objet du jeu avec l'id correspondant
    def getConponent(self, id):
    	for i in range( len(self.towerList) ):
    		if (self.towerList[i].getID() == id):
    			return self.towerList[i]
    		
    #Assigner un id à tous les creep et towers créé
    def getUniqueId(self):
    	self.universalId += 1
    	return self.universalId 
    def showDebugMap(self):
    	for i in range( len(self.enemyList)):
    		pos= [self.enemyList[i].x, self.enemyList[i].y]
    		print("Enemy",i, ":", pos[0], "-", pos[1])
    def testInitTower(self):
    	self.towerList.append(Tower(self.getUniqueId()))
    	self.towerList.append(Tower(self.getUniqueId()))
    	self.towerList[0].setPos(10, 70)
    	self.towerList[1].setPos(10, 100)
    def testInitEnemy(self):
    	self.enemyList.append(Creep())