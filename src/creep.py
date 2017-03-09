from lib.point import Point

class Creep():
	def __init__(self, chemin, hp = 100, speed = 10, attaque = 1):
		self.hp = hp #vie
		self.speed = speed #vitesse en pixel/update
		self.attaque = attaque #force du creep
		self.chemin = iter(chemin) #les positions que le creep doit prendre (liste)
		self.pos = next(self.chemin)
		self.target = self.set_next_target()

	def set_next_target(self):
		tar = None
		try:
			tar = next(self.chemin)
		except StopIteration:
			tar = None
		self.target = tar

	def move(self):
		if self.target:
			if self.pos.x < self.target.x:
				self.pos.x += speed
			elif self.pos.x > self.target.x:
				self.pos.x -= speed

			if self.pos.y < self.target.y:
				self.pos.y += speed
			elif self.pos.y > self.target.y:
				self.pos.y -= speed
		if self.pos.x == self.target.x and self.pos.y == self.target.y:
			self.set_next_target()

	