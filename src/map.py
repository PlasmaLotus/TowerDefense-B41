#Created Par Lee-Stenio

from lib.path import Path

#class Point:

##Map contient toutes les informations des tiles, taille du niveau et spawnpoint 
class Map(object):
    def __init__(self):
        self.height = 0
        self.length = 0
        self.pathList=[]
        self.pathPointList=[]

        
    def getStart(self):
        #retourne le debut du premier segment
        return self.pathList[0].getStart()
    
    def getEnd(self):
        #retourne la fin du dernier segment
        return self.pathList[-1].getEnd()
        
##Map  pr�d�finie, Ligne droite au milieu##
class MapPreset1(Map):
    def __init__(self):
        #TODO:Remove Path module
        Map.__init__(self)
        self.height = 800
        self.length = 600
        self.pathList=[]
        self.pathList.append(Path(0, 300, 600, 300, 16));
        self.pathPointList=[]
        self.pathPointList.append(self.getStart())
        for i in range (len(self.pathList)):
            self.pathPointList.append( self.pathList[i].getEnd() )