import Tile
from Tile import *

import Map
from Map import *
#class Tile():
import Niveau
from Niveau import *

import Creep
from Creep import *



## AKA "Modele" ## 
class Game():
    def __init__(self):

        #self.height = 11
        #self.length = 20
        #self.creepList[]
        self.currentNiveau=Niveau()
        self.noCurrentNiveau=1 # valsur du niveau courrant
        self.currentWave=1 # valsuer de la wave courrante
        self.nbEnemies=0
        self.enemyList=[]# liste d'enemies vivants dans le jeu
        self.towerList=[]# liste des tours actives
        #self.tileList=[]
        self.map=Map()
        self.HP = 1 # vie du joueur?

    
    #/ initialise le niveau et toutes ses composante ##    
    def init(self):
        
        #self.NiveauHandler.getNiveau(self.niveauIt)
        self.currentNiveau=NiveauDebug()
        self.map=self.currentNiveau.getMap()
        self.HP=5

        ##Test##        
        self.enemyList.append(Creep())
        self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)
    
    
    ## Mise a jour du jeu ##
    def update(self):
        #for i in range(enemyList.size):
            #enemyList[i].move()
        
        #if (self.HP <= 0):
            #
    
    ## Montre la map par ligne de commande ##
    def showDebugMap(self):
        charMatrix = [[' ' for i in range(self.map.length)] for j in range(self.map.height)]
        
        for i in range(self.map.height):
            for j in range(self.map.length):
                if (self.map.tileList[i][j].getPath() == True):
                    charMatrix[i][j] = 'P'
                else:
                    charMatrix[i][j] = '_'
                    
        for i in range(self.map.height):
            print(charMatrix[i])
            
    