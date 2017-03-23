#Created Par Lee-Stenio

from niveau import Niveau, NiveauDebug
from creep import Creep
from tower import *


class Game(object):
    '''le modele'''
    def __init__(self, largeur, hauteur):
        self.current_niveau = NiveauDebug()
        self.largeur = largeur
        self.hauteur = hauteur
        #self.noCurrentNiveau = 1 # valeur du niveau courrant
        self.current_wave = 1 # valeur de la wave courrante
        self.creeps = []
        self.towers = []
        self.vie = 5
        self.universal_id = -1
        self.gold = 500
        self.pathPointList = []

        self.testInitEnemy()
        self.testInitTower()

    ## Mise a jour du jeu (une fois par frame, probablement appelée par controlleur)##
    def update(self):
        for tower in self.towers:
            tower.findEnemy(self.creeps)
            tower.update()

        for creep in self.creeps:
            if creep.vie == 0:
                self.creeps.remove(creep)
                continue

            creep.move()
            if creep.pos == self.current_niveau.map.getEnd():
                print("Enemy Breach")
                self.vie -= 1

        #self.handleEnemySpawn()

        if self.vie <= 0:
            return False

        self.showDebugMap()
        return True

    #TODO: ajoutTourArcher -> ajouter_tour(x, y, type)
    def ajoutTourArcher(self, x, y, type=None):
        tower = Tower(x, y)
        if self.gold >= tower.price:
            #TODO: valider position (pas sur chemin/autre tour)
            self.towers.append(tower)
            self.gold -= tower.price
            return True
        else:
            return False

    def ajoutTourBombe(self, x, y):
        pass

    def ajoutTourCannon(self, x, y):
        pass

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
            if tower.id == id:
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
        self.towers.append(Tower(self.getUniqueId()))
        self.towers.append(Tower(self.getUniqueId()))
        self.towers[0].setPos(10, 70)
        self.towers[1].setPos(10, 100)

    def testInitEnemy(self):
        self.creeps.append(Creep(self.currentNiveau.map.pathPointList, 100, 10, 1))
        self.creeps.append(Creep(self.currentNiveau.map.pathPointList, 75, 2, 2))
        self.creeps.append(Creep(self.currentNiveau.map.pathPointList, 50, 10, 3))
        #BUG: Les creeps on