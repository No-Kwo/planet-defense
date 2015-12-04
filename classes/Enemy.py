class Enemy(object):
	'''
	A class that represents an ennemy.
	This class has to be inherited from.
	'''

	max_hp = 10
	speed = 1.0
	damage = 1
	sprite = ''

	def __init__(self, max_hp=max_hp):
		self.hp = max_hp