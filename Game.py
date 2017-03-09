#Créé Par Lee-Stenio

import Map
from Map import *
#class Tile():
import Niveau
from Niveau import *

import Creep
from Creep import *



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

    
    #/ initialise le niveau et toutes ses composante ##    
    def init(self):
        
        #self.NiveauHandler.getNiveau(self.niveauIt)
        self.currentNiveau=NiveauDebug()
        self.map=self.currentNiveau.getMap()
        self.hp=5

        ##Test##      
        self.enemyList=[]  
        self.enemyList.append(Creep())
        #self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)
    
    
    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for i in range(len(self.enemyList) ):
            self.enemyList[i].move()
        
        #if (self.hp <= 0):
            ##Gameover
            
        self.showDebugMap()
    
    ## Montre la map par ligne de commande ##
    def showDebugMap(self):
        for i in range( len(self.enemyList) ):
        	pos= [self.enemyList[i].x, self.enemyList[i].y]
        	print("Enemy ",i, " : ", pos[0], "-", pos[1] )

        	#print( "Enemy ",i, " : ", str(self.enemyList[i].x), " - ", str(self.enemyList[i].y) )
    
    