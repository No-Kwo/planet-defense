class Player(object):
	'''
	A class that is supposed to represent the player
	'''

	def __init__(self, **kwargs):
		self.name = kwargs.get('name', default='Player')
		self.max_hearts = kwargs.get('max_hearts', default=3)
		self.hearts = kwargs.get('hearts', default=self.max_hearts)
		self.sprite = kwargs.get('sprite', default='default_player_sprite.png')

		self.score = 0
		self.kills = 0

		self.ships = []


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
