import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def get_angled_point(self, angle, longueur, cx, cy):
        x = (math.cos(angle) * longueur) + cx
        y = (math.sin(angle) * longueur) + cy

        return Point(x, y)

    def angle(self, pos):
        dx = pos.x - self.x
        dy = pos.y - self.y

        return math.atan2(dy,dx) #angle

    def distance(self, pos):
        dx = abs(pos.x - self.x) ** 2
        dy = abs(pos.y - self.y) ** 2

        return math.sqrt(dx + dy) #distance

