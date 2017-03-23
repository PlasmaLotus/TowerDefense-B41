#Créé Par Lee-Stenio

#import lib.path
#from lib.path import *

from lib.point import Point

##Map contient toutes les informations des tiles, taille du niveau et spawnpoint 
class Map:
    def __init__(self):
        self.height = 0
        self.length = 0
        self.pathSize = 10
            
        self.pathPointList=[]
        
    def getStart(self):
        #retourne le debut du premier segment
        return self.pathPointList[0]
    
    def getEnd(self):
        #retourne la fin du dernier segment
        return self.pathPointList[-1]
        
##Map  prédéfinie, Ligne droite au milieu##
class MapPreset1(Map):
    def __init__(self):
        #TODO:Remove Path module
        Map.__init__(self)
        self.height = 800
        self.length = 600
        #self.pathList.append(Path(0, 300, 600, 300, 16));
        self.pathPointList=[]
        self.pathPointList.append(Point(0,400))
        self.pathPointList.append(Point(600,400))
        self.pathSize = 16
