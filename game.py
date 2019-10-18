from __init__ import *
from dialogue import Dialogue
class Game():
	def __init__(self, s):
		self.s = s
		self.i = 0
		
	def Run(self):
		while True:
			if self.s[self.i][0] != "!quit":
				if self.s[self.i]:
					spacer = "."*(5-len(str(self.i)))
					print(" "*(73-len(str(self.i)))+f"<{spacer}{self.i}>")
					entry = Dialogue(self.s[self.i])
					wait_duration = entry.Say()
					self.i = entry.Page(wait_duration)
				else:
					self.i = 0
			else:
				print(f"\n <!quit command recieved>\n\n Exiting Game...\n\n{window_dstrike}")
				quit()
					
