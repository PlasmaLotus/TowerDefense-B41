
#Tile est une des nombreuses tuiles d'un niveau
class Tile:
    def __init__(self):
        self.path = False #Le fait ou non si la tuile est un chemin
        
    def setPath(self, b):
        self.path = b
        
    def getPath(self):
        return self.path