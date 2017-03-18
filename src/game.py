#Created Par Lee-Stenio

from niveau import Niveau, NiveauDebug
from creep import Creep
from tower import Tower


class Game(object):
    '''le modele'''
    def __init__(self):
        self.current_niveau = Niveau()
        #self.noCurrentNiveau = 1 # valeur du niveau courrant
        self.current_wave = 1 # valeur de la wave courrante
        self.creeps = []
        self.towers = []
        self.vie = 5
        self.universal_id = -1
        self.gold = 500
        self.pathPointList = []


    #/ initialise le niveau et toutes ses composante ##
    def init(self):

        #self.NiveauHandler.getNiveau(self.niveauIt)
        self.current_niveau = NiveauDebug()
        self.vie = 5
        self.creeps = []
        self.towers = []
        ##Test##
        self.testInitEnemy()
        self.testInitTower()
        self.pathPointsList = []


        #self.enemyList[0].setPos(self.map.spawnPointX, self.map.spawnPointY)


    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for tower in self.towers:
            tower.findEnemy(self.creeps)
            tower.update()

        for creep in self.creeps:
            creep.move()
            if creep.pos == self.current_niveau.map.getEnd():
                print("Enemy Breach")
                self.vie -= 1

        #self.handleEnemySpawn()

        if self.vie <= 0:
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


    #gère l'addition d'énemis dans le temps
    def handleEnemySpawn(self):
        ##TODO:: tjrs pas fini
        if self.current_niveau.hasEnemies(self.current_wave):
            if self.current_niveau.update():
                nextEnemy = self.current_niveau.getNextEnemy(self.current_wave)
                self.creeps.append(nextEnemy)


    #Trouver l'objet du jeu avec l'id correspondant
    def get_component(self, id):
        for tower in self.towers:
            if tower.getID() == id:
                return tower


    #Assigner un id à tous les creep et towers créé
    def getUniqueId(self):
        self.universalId += 1
        return self.universalId

    ##afficher un rendu primitif de la map
    def showDebugMap(self):
        for creep in self.creeps:
            pos = creep.pos
            print("Enemy", creep, ":", pos.x, "-", pos.y)

    def testInitTower(self):
        self.towerList.append(Tower(self.getUniqueId()))
        self.towerList.append(Tower(self.getUniqueId()))
        self.towerList[0].setPos(10, 70)
        self.towerList[1].setPos(10, 100)

    def testInitEnemy(self):
        self.enemyList.append(Creep(self.currentNiveau.map.pathPointList, 100, 10, 1))
        self.enemyList.append(Creep(self.currentNiveau.map.pathPointList, 75, 2, 2))
        self.enemyList.append(Creep(self.currentNiveau.map.pathPointList, 50, 10, 3))
        #BUG: Les creeps on