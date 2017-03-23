#Cree par Lee-Stenio

from lib.point import Point

class Tower():
    id = 1

    def __init__(self, x, y, speed=10, dmg=1, _range=100, price=100):
        self.pos = Point(x, y)
        self.price = price
        self.atk_speed = speed #nb de frames avant de pouvoir retirer
        self.atk_power = dmg

        self.range = _range #pixels
        self.angle = 0 #purement cosmetique pour l'instant
        self.can_shoot = False
        self.atk_delay = 0
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
                self.angle = self.pos.angle(creep.pos)
                self.shoot(creep)
                break


    def in_range(self, pos):
        dist = self.pos.distance(pos)
        return True if dist <= self.range else False

    #tente d'attaquer un enemy
    def shoot(self, creep):
        if self.can_shoot:
            creep.recevoir_dmg(self.atk_power)
            print("Tower shot")
            self.can_shoot = False

    def get_refund_price(self):
        return self.price/2
