import Tile
from Tile import *

#class Point:

##Map contient toutes les informations des tiles, taille du niveau et spawnpoint 
class Map:
    def __init__(self):
        self.height = 0
        self.length = 0
        self.tileList=[]
        self.tileSizeX = 16
        self.tileSizeY = 16
        self.spawnPointX=0
        self.spawnPointY=0
        self.endPointX=0
        seld.endPointY=0
    
        
##Map  prédéfinie, Ligne droite au milieu
class MapPreset1(Map):
    def __init__(self):
        super()
        self.height = 11
        self.length = 20
        self.spawnPointX=0
        self.spawnPointY=5
        self.endPointX=0
        seld.endPointX=11
        self.tileList=[[Tile() for i in range(self.length)] for j in range(self.height)]
        for i in range(self.length):
            self.tileList[5][i].setPath(True)
