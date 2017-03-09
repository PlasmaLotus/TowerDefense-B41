from lib.point import Point

class Creep():
	def __init__(self, chemin, vie = 100, speed = 10):
		self.vie = vie
		self.speed = speed #vitesse en pixel/update
		self.chemin = iter(chemin) #iteration sur la liste de points du chemin
		self.pos = next(self.chemin) #depart
		self.target = self.set_next_target() #trouver la cible

	#trouve la prochaine cible
	def set_next_target(self):
		tar = None #cible temporaire
		try:
			tar = next(self.chemin) #prochain point
		except StopIteration:
			tar = None #si reste aucun point
		self.target = tar

	# deplace si il y a une cible
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

	def recevoir_dmg(self, dmg):
		if self.vie > 0:
			self.vie -= dmg