# coding: utf-8

#Créé Par Lee-Stenio
from lib.map import Map
from niveau import *
from creep import *

class Joueur():
    def __init__(self, nom, score, ress, exp):
        self.nom = nom
        self.score = score
        self.ress = ress #ressources
        
    def setRessource(self, ressource):
        self.ress = ressource

## AKA "Modele" ## 
class Game():
	##Crée par Lee-Stenio
    def __init__(self, w, h):
        self.largeur = w
        self.hauteur = h
        self.currentNiveau=Niveau()
        self.noCurrentNiveau=1 # valsur du niveau courrant
        self.currentWave=1 # valsuer de la wave courrante
        self.nbEnemies=0
        self.enemyList=[]# liste d'enemies vivants dans le jeu
        self.towerList=[]# liste des tours actives
        #self.map=Map()
        self.hp = 1 # vie du joueur?

    
    #/ initialise le niveau et toutes ses composante ##    
    def init(self):
        
        #self.NiveauHandler.getNiveau(self.niveauIt)
        self.currentNiveau = NiveauDebug()
        self.map=self.currentNiveau.getMap()
        self.hp=5

        ##Test##      
        self.enemyList=[]
        path = self.map.get_path()  
        self.enemyList.append(Creep(path))
        #self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)
    
    
    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for i in self.enemyList:
            i.move()

            if i.vie <= 0:
                del i
        
        #if (self.hp <= 0):
            ##Gameover
            
        self.showDebugMap()
    
    ## Montre la map par ligne de commande ##
    def showDebugMap(self):
        for i in self.enemyList:
        	pos= [i.x, i.y]
        	print("Enemy ", i, " : ", pos[0], "-", pos[1] )

        	#print( "Enemy ",i, " : ", str(self.enemyList[i].x), " - ", str(self.enemyList[i].y) )
    
    