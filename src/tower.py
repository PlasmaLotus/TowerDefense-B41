#Cree par Lee-Stenio

#from lib.helper import Helper
from lib.point import Point

class Tower():
    id = 1
    def __init__(self):
        self.pos = Point(0, 0)
        self.size_radius = 8 #pixels
        self.atk_delay = 0
        self.atk_speed = 10 #nb de frames avant de pouvoir retirer
        self.atk_power = 1
        self.range = 100 #pixels
        self.angle = 0 #purement cosmetique pour l'instant
        self.can_shoot = False
        self.price = 100
        self.id = Tower.id
        Tower.id += 1

    #rafraichi le cooldown de ses attaques
    def update(self):
        if not self.can_shoot:
            self.atk_delay -= 1
            if self.atk_delay <= 0:
                self.can_shoot = True
                self.atk_delay = self.atk_speed

    def find_enemy(self, creeps):
        for creep in creeps:
            #de cette facon, le premier enemy sera choisi
            if self.in_range(creep.pos):
                #cet enemy est dans le rayon
                #self.angle = Helper.angle(self.pos, creep.pos)
                self.angle = self.pos.angle(creep.pos)
                self.shoot(creep)
                break


    def in_range(self, pos):
        #dist = Helper.distance(self.pos, pos)
        return True if self.pos.distance(pos) <= self.range else False

    #tente d'attaquer un enemy
    def shoot(self, enemy):
        if self.can_shoot:
            #enemy.hp -= self.atkPower
            print("Tower shot")
            self.can_shoot = False

    def get_refund_price(self):
        return self.price/2

#classe inutile
class Canon(Tower):
    def __init__(self, id):
        #Tower.__init__(self, id)
        #balance numbers here
        self.atk_power = 50
        self.atk_speed = 20
        self.range = 90
        self.price = 150


