# coding: utf-8
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

        self.init()

        #/ initialise le niveau et toutes ses composante ##
    def init(self):

        #self.NiveauHandler.getNiveau(self.niveauIt)
        #self.current_niveau = NiveauDebug()
        self.current_wave = self.current_niveau.wave
        print("Wave:",self.current_wave)
        self.vie = 5
        self.creeps = []
        self.towers = []
        ##Test##
        #self.testInitEnemy()
        self.testInitTower()
        #self.pathPointsList = []

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
                self.creeps.remove(creep)
                print("Enemy Breach")
                self.vie -= 1

        self.handleEnemySpawn()

        if self.vie <= 0:
            return False

        
        #self.showDebugMap()
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

    def ajoutTourCanon(self, x, y):
        pass

    #gère l'addition d'énemis dans le temps
    def handleEnemySpawn(self):
        ##TODO:: tjrs pas fini
        if self.current_niveau.hasEnemies():
            if self.current_niveau.update():
                nextEnemy = self.current_niveau.getNextEnemy()
                if nextEnemy != None:
                    self.creeps.append(nextEnemy)
        else:
            if (len(self.creeps) <= 0):
                self.current_niveau.nextWave()
                self.init()


    #Trouver l'objet du jeu avec l'id correspondant
    def get_component(self, id):
        for tower in self.towers:
            if tower.id == id:
                return tower

    ##afficher un rendu primitif de la map
    def showDebugMap(self):
        for creep in self.creeps:
            pos = creep.pos
            print("Enemy", creep, ":", pos.x, "-", pos.y)

    def testInitTower(self):
        self.towers.append(Tower(100,70))
        self.towers.append(Tower(10,100))
