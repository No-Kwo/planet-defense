class Ship(object):
	'''
	A class that represents a ship.
	This class has to be inherited from.
	'''

	max_hp = 10
	damage = 1
	atk = 1
	sprite = ''

	def __init__(self, max_hp=max_hp, atk=atk, orbiting=False):
		self.hp = max_hp
		self.orbiting = orbiting
		self.atk = atk