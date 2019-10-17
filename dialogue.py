from __init__ import *

class keyboardDisable():

	def start(self):
		self.on = True

	def stop(self):
		self.on = False

	def __call__(self): 
		while self.on:
			msvcrt.getch()


	def __init__(self):
		self.on = False
		import msvcrt

class Dialogue():
	def __init__(self, d):
		self.name = d[0]
		self.text = d[1]
		self.exits = d[2]
		self.disable = keyboardDisable()
		
		self.Process()

	def Process(self):
		#Name Replacement
		if self.name == "!yn":
			self.name = player_name

		#Name Insertion
		temptext = self.text.split("!yn")
		self.text = player_name.join(temptext)

	def Type(self, text):
		self.disable.start()
		textlist = text.split("!ps")
		for i in textlist:
			for c in i:
				print(c, end='')
				time.sleep(0.04)
			time.sleep(0.6)
		self.disable.stop()
		return ""
	
	def Say(self):
		self.disable.start()
		if self.name == "!no":
			print(self.Type("{}".format(self.text)))
		else:
			print(self.Type(" <{}>: {}".format(self.name, self.text)))
		self.disable.stop()

	def Page(self):
		if len(self.exits) > 1:
			print (window_strike)
			for i in enumerate (self.exits):
				print (self.Type(" {} - {}".format(i[0]+1, i[1][0])))
			while True:
				chosen_exit = input("{}\n\n> ".format(window_strike))
				for i in enumerate(self.exits):
					if chosen_exit == str(i[0]+1):
						print ("\n{}\n".format(window_dstrike))
						return i[1][1]
		else:
			self.disable.start()
			time.sleep(0.8)
			self.disable.stop()
			print ("\n{}\n".format(window_dstrike))
			return self.exits[0][1]
