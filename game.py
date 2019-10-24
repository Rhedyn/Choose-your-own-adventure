from __init__ import *
from dialogue import Dialogue
from player import Player

class Game():
	def __init__(self, s):
		self.s = s
		self.i = 0
		self.p = Player("")
		
	def Run(self):
		while True:
			if self.s[self.i][2] != "!quit":
				if self.i in self.s:
					
					spacer = "."*(5-len(str(self.i)))
					print(" "*(73-len(str(self.i)))+f"<{spacer}{self.i}>")
					
					
					entry = Dialogue(self.s[self.i], self.p)
					
					if len(self.s[self.i][0]) > 0:
						self.p.add_items(self.s[self.i][0])
						for a in self.s[self.i][0]:
							print(tw.fill(f"<The item \"{a}\" was added to your inventory.>")+"\n")
									
					if len(self.s[self.i][1]) > 0:
						self.p.remove_items(self.s[self.i][1])
						for r in self.s[self.i][1]:
							print(tw.fill(f"<The item \"{r}\" was removed from your inventory.>")+"\n")
							
					wait_duration = entry.Say()
					self.i = entry.Page(wait_duration)
					
				else:
					self.i = 0
			else:
				print(f"\n <!quit command recieved>\n\n Exiting Game...\n\n{window_dstrike}")
				quit()
					
