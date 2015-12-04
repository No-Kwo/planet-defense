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