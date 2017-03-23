import math

class Helper(object):

    @staticmethod
    def get_angled_point(angle, longueur, cx, cy):
        x = (math.cos(angle) * longueur) + cx
        y = (math.sin(angle) * longueur) + cy

        return (x, y)

    @staticmethod
    def angle(pos1, pos2):
        dx = pos2.x - pos1.x
        dy = pos2.y - pos2.y

        return math.atan2(dy,dx) #angle

    @staticmethod
    def distance(pos1, pos2):
        dx = abs(pos2.x - pos1.x) ** 2
        dy = abs(pos2.y - pos1.y) ** 2

        return math.sqrt(dx + dy) #distance
