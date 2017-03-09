#Créé Par Lee-Stenio

import Path
from Path import *

#class Point:

##Map contient toutes les informations des tiles, taille du niveau et spawnpoint 
class Map:
    def __init__(self):
        self.height = 0
        self.length = 0
        self.pathList=[]
        
    def getDtart(self):
        return self.pathList[0].getStart()
    
    def getEnd(self):
        return self.pathList[-1].getEnd()
        
##Map  prédéfinie, Ligne droite au milieu##
class MapPreset1(Map):
    def __init__(self):
        Map.__init__(self)
        self.height = 800
        self.length = 600
        self.pathList=[]
        self.pathList.append(Path(10, 300, 590, 300, 16));
