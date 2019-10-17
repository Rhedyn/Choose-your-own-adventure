from __init__ import *
from dialogue import Dialogue
class Game():
	def __init__(self, s):
		self.s = s
		self.i = 0
		
	def Run(self):
		while True:
			print (f"<Page {self.i}>")
			if self.s[self.i]:
				entry = Dialogue(self.s[self.i])
				entry.Say()
				self.i = entry.Page()
			else:
				self.i = 0
