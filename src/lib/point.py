class Point():
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
		
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
