from lib.point import Point
class Creep(object):
    '''creep qui se deplace'''

    def __init__(self, chemin, vie, speed):
        self.vie = vie
        self.speed = speed #vitesse en pixel/update
        self.chemin = iter(chemin)
        position = next(self.chemin) #depart
        self.pos = Point(position.x, position.y)
        self.target = self.set_next_target() #trouver la cible

    def set_next_target(self):
        '''trouve la prochaine cible'''
        tar = None #cible temporaire
        try:
            tar = next(self.chemin) #prochain point
        except StopIteration:
            tar = None #si reste aucun point
        #self.target = tar
        #La fonction retourne Null...
        return tar

    def move(self):
        '''deplace si il y a une cible'''
        if self.target:
            if self.pos.x < self.target.x:
                self.pos.x += self.speed
            elif self.pos.x > self.target.x:
                self.pos.x -= self.speed

            if self.pos.y < self.target.y:
                self.pos.y += self.speed
            elif self.pos.y > self.target.y:
                self.pos.y -= self.speed
            if self.pos == self.target:
                self.set_next_target()

    def recevoir_dmg(self, dmg):
        '''recoit dommage '''
        if self.vie > 0:
            self.vie -= dmg