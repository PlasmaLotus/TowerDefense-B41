from vector import Vector

class Entity(object):
	"""docstring for Entity"""
	def __init__(self):
		self.pos = Vector()
		self.components = []

	def add(self, component):
		self.components.append(component)
		