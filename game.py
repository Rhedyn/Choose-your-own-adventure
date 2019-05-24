from __init__ import *
from dialogue import Dialogue
class Game():
	def __init__(self, story):
		#self.window = pg.display.set_mode(size)
		#self.window.fill((0, 255, 0))
		self.s = story
		self.i = 0
		
	def Run(self):
		while True:
			if self.s[self.i]:
				entry = Dialogue(self.s[self.i])
				entry.Say()
				self.i = entry.Page()
			else:
				i = 0
