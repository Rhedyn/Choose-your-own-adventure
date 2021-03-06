from __init__ import *

class Dialogue():
	def __init__(self, d, p):
		self.name = d[2]
		self.p = p
		self.text = d[3]
		self.exits = d[4]
		self.Process()

	def Process(self):
		#Name Replacement
		if self.name == "!yn":
			self.name = self.p.name

		#Name Insertion
		temptext = self.text.split("!yn")
		self.text = player_name.join(temptext)
		

	def Type(self, text):
		text = text.split("!ps")
		text = "".join(text)
		print(tw.fill(text))
		return 0.04*len(text)
	
	def Say(self):
		
		if self.name == "!no":
			wait_duration = self.Type(f"{self.text}")
		else:
			wait_duration = self.Type(f"<{self.name}>: {self.text}")
		return wait_duration

	def Page(self, wait_duration):
		if len(self.exits) > 1:
			print (f"\n{window_strike}\n")
			for i in enumerate (self.exits):
				self.Type("> Choice {} - {}\n".format(i[0]+1, i[1][0]))
				print('')
			while True:
				chosen_exit = input("{}\n\n> ".format(window_strike))
				for i in enumerate(self.exits):
					if chosen_exit == str(i[0]+1):
						print ("\n{}".format(window_dstrike))
						return i[1][1]
						
					elif chosen_exit.lower() == "inv":
						print(f"\n{window_pstrike}\n")
						for i in self.p.inventory:
							print(f"- {i} ({self.p.inventory[i]})")
						print('')
						break
		else:
			#print(f" DBUG> Progressing to page <{self.exits[0][1]}>")
			print ("\n{}".format(window_dstrike))
			time.sleep(wait_duration)
			return self.exits[0][1]
		
