
from lib.point import Point

class Path(object):
    def __init__(self, x, y, x2, y2, length):
        self.start = Point(x, y)
        self.end = Point(x2, y2)
        self.length = length #

    def is_on_path(self, point):
        #if (x == self.startX or x == self.endX or y == self.startY or y == self.endY ):
        if point >= self.start and point <= self.end:
            return True
        else:
            return False
