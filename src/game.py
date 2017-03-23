#Created Par Lee-Stenio

from Niveau import Niveau, NiveauDebug
from Creep import Creep
from Tower import *
from _overlapped import NULL


class Game(object):
    '''le modele'''
    def __init__(self, height, width):
        self.current_niveau = NiveauDebug()
        #self.noCurrentNiveau = 1 # valeur du niveau courrant
        self.current_wave = 1 # valeur de la wave courrante
        self.creeps = []
        self.towers = []
        self.vie = 5
        self.universal_id = -1
        self.gold = 500
        #self.pathPointList = []
        self.largeur = width
        self.hauteur = height
        self.universal_id = -1
        self.init()


    #/ initialise le niveau et toutes ses composante ##
    def init(self):

        #self.NiveauHandler.getNiveau(self.niveauIt)
        #self.current_niveau = NiveauDebug()
        self.current_wave = self.current_niveau.wave
        print("Wave:",self.current_wave)
        self.vie = 35
        self.creeps = []
        self.towers = []
        ##Test##
        #self.testInitEnemy()
        self.testInitTower()
        #self.pathPointsList = []


        #self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)


    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for tower in self.towers:
            tower.find_enemy(self.creeps)
            tower.update()

        for creep in self.creeps:
            creep.move()
            #if creep.vie<= 0:
                #creep.remove(creep)
            if creep.pos == self.current_niveau.map.getEnd():
                print("Enemy Breach")
                self.vie -= 1
              
        #Supprimer le creep qui a fini        
        for i in reversed( range (len(self.creeps))):
            if self.creeps[i].vie <= 0:
                self.creeps.remove(self.creeps[i])
            elif self.creeps[i].pos == self.current_niveau.map.getEnd():
                self.creeps.remove(self.creeps[i])
            elif self.creeps[i].pos.x >= self.current_niveau.map.getEnd().x and self.creeps[i].pos.y >= self.current_niveau.map.getEnd().y: 
                self.creeps.remove(self.creeps[i])
                #si la position du creep est plus loin que la position finale

        
        self.handleEnemySpawn()
        #print ("Vie: ", self.vie)
        if self.vie <= 0:
            print("Game over")
            return False

        
        self.showDebugMap()
        return True

    def create_tower(self, towerType, x, y):
        towerPrice = 0
        newTower = Tower()
        #type de donnée de towerType a définir
        if (towerType == "Canon"):
            towerPrice = Canon.getPrice()
            newTower = Canon(self.getUniqueId(), x, y)

        if self.gold >= towerPrice:
            self.towers.append(newTower)
            return True
        else:
            return False

    def ajoutTourBombe(self, x,y):
		#ajouter une tour a la liste de tour
	    pass
	
    def ajoutTourArcher(self,x,y):
		#ajouter une tour a la liste de tour
		#self.towerList.append(TourArcher(x,y))
        pass
	
    def ajoutTourCanon(self,x,y):
		#ajouter une tour a la liste de tour
        pass

    #gère l'addition d'énemis dans le temps
    def handleEnemySpawn(self):
        ##TODO:: tjrs pas fini
        if self.current_niveau.hasEnemies(self.current_wave):
            if self.current_niveau.update():
                nextEnemy = self.current_niveau.getNextEnemy(self.current_wave)
                if nextEnemy != NULL:
                    self.creeps.append(nextEnemy)
        else:
            if (len(self.creeps) <= 0):
                self.current_niveau.nextWave()
                self.init()

    #Trouver l'objet du jeu avec l'id correspondant
    def get_component(self, id):
        for tower in self.towers:
            if tower.getID() == id:
                return tower


    #Assigner un id à tous les creep et towers créé
    def getUniqueId(self):
        self.universal_id += 1
        return self.universal_id

    ##afficher un rendu primitif de la map
    def showDebugMap(self):
        #print(len(self.creeps))
        for creep in self.creeps:
            pos = creep.pos
            print("Enemy", creep, ":", pos.x, "-", pos.y, "HP:", creep.vie)

    def testInitTower(self):
        self.towers.append(Canon(self.getUniqueId()))
        #self.towers.append(Tower(self.getUniqueId()))
        self.towers.append(Canon(self.getUniqueId()))
        #self.towers.append(Tower(self.getUniqueId()))
        self.towers[0].pos.x = 200
        self.towers[0].pos.y = 400
        #self.towers[1].setPos(50, 100)

    def testInitEnemy(self):
        
        self.creeps.append(Creep(self.current_niveau.map.pathPointList, 100, 10))
        self.creeps.append(Creep(self.current_niveau.map.pathPointList, 70, 20))
        self.creeps.append(Creep(self.current_niveau.map.pathPointList, 50, 30))
        self.creeps.append(Creep(self.current_niveau.map.pathPointList, 25, 40))
        self.creeps.append(Creep(self.current_niveau.map.pathPointList, 1, 50))
        