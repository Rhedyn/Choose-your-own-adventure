from __init__ import *

class Player():
	def __init__(self, name):
		self.name = name
		self.inventory = {}
		
	def add_items(self, item_array):
		for item in item_array:
			if item in self.inventory:
					self.inventory[item] += 1
			else:
				self.inventory[item] = 1
	
	def remove_items(self, item_array):
		for item in item_array:
			if item in self.inventory:
				if self.inventory[item] > 1:
					self.inventory[item] -= 1
				else:
					self.inventory.pop(item)
