class Story():
	def __init__(self):
		self.e = {}
	def Add(self, entry):
		self.e[len(self.e)] = entry
	
class Entry():
	def __init__(self, name = "DEFAULT", text = "DEFAULT"):
		self.name = name
		self.text = text
		self.exits = [("DEFAULT", 0)]
		
	def EditName(self):
		print ("\n=<EDIT NAME>{}\n".format('='*68))
		self.name = input("What should the new name be?\n\n> ")
	def EditText(self):
		print ("\n=<EDIT TEXT>{}\n".format('='*68))
		self.text = input("What should the new text be?\nBe aware of the following formattings:\n-> Player name  = !yn\n-> No Speaker   = !no\n-> Typing Pause = !ps\n\n> ")
	def EditExits(self):
		print ("\n=<EDIT EXITS>{}\n".format('='*67))
		for i in enumerate (self.exits):
			print("{} - {}: {}".format(i[0], i[1][0], i[1][1]))
		choice = input("Which exit would you like to change?\n\n> ")
		for c, i in enumerate (self.exits):
			if choice == str(c):
				tempText = input("Please enter the exit text\n\n> ")
				tempID = input("Please enter the pointer\n\n> ")
				self.exits[c] = (tempText, tempID)
	def AddExit(self):
		print ("\n=<ADD EXIT>{}\n".format('='*69))
		tempText = input("Please enter the exit text\n\n> ")
		tempID = input("Please enter the pointer\n\n> ")
		print ("<DEBUG> Text: ", tempText," ID: " ,tempID)
		self.exits.append((tempText, tempID))
	def RemoveExit(self):
		print ("\n=<REMOVE EXITS>{}\n".format('='*65))
		for i in enumerate (self.exits):
			print("{} - {}: {}".format(i[0], i[1][0], i[1][1]))
		choice = input("Which exit would you like to remove?\n\n> ")
		for c, i in enumerate (self.exits):
			if choice == str(c):
				del(self.exits[c])

class Editor():
	def __init__(self):
		self.currentID = 0
		self.s = Story()
		self.s.Add(Entry())
		self.Run()

	def Run(self):
		while True:
			print("\n=<EDIT STORY>{}\n\nCURRENT ENTRY ID - {}\nNUMBER OF ENTRIES - {}".format('='*67, self.currentID, len(self.s.e)))
			choice = input("What would you like to do?\n{}\n".format('-'*80)+
					"1) Choose another Entry\n"+
				        "2) Add a new Entry\n"+
					"3) Change a part of the current entry\n"+
					"4) See how the current entry looks\n"+
					"5) See a list of all entries\n"+
					"6) Save the dictionary\n"+
					"7) Load existing story from story.py\n\n> ")
			if choice == "1":
				self.ChangeID()
			if choice == "2":
				self.s.Add(Entry())
				print("Added a new blank entry.")
			if choice == "3":
				self.EditEntry()
			if choice == "4":
				self.ViewEntry()
			if choice == "5":
				self.ViewList()
			if choice == "6":
				self.Save()
			if choice == "7":
				self.Load()
	def ChangeID(self):
		print("\n=<MOVE TO ID>{}\n\n Which ID would you like to move to?\n{}".format('='*67, '-'*80))
		for e in (self.s.e):
			print("{}) <{}>: {}".format(e, self.s.e[e].name, self.s.e[e].text[0:50]))
			for _exit in self.s.e[e].exits:
				print(f"\t{_exit[0]}: {_exit[1]}")
		requestedID = input("{}\nPlease give the entry ID you want to switch to\n\n> ".format('-'*80))
		for k in self.s.e:
			if str(k) == requestedID:
				self.currentID = int(requestedID)
	def EditEntry(self):
		while True:
			print("current ID:", self.currentID)
			choice = input("\n=<EDIT ENTRY>{}\n\nWhat Part of the Entry would you like to change?\n{}\n1) Change name of speaker\n2) Change dialogue\n3) Edit existing exits\n4) Add a new exit\n5) Remove an exit\n\n> ".format('='*67, '-'*80))
			if choice == "1":
				self.s.e[self.currentID].EditName()
			if choice == "2":
				self.s.e[self.currentID].EditText()
			if choice == "3": 
				self.s.e[self.currentID].EditExits()
			if choice == "4": 
				self.s.e[self.currentID].AddExit()
			if choice == "5": 
				self.s.e[self.currentID].RemoveExit()
			if choice == "":
				break
	def ViewEntry(self):
		print("\n=<VIEW ENTRY>{}\n\n <{}>: {}\n\n{}\n".format('='*67, self.s.e[self.currentID].name, self.s.e[self.currentID].text, '-'*80))
		for i in enumerate (self.s.e[self.currentID].exits):
			print("Enum: {} - <Text: {}> (Pointer: {})".format(i[0], i[1][0], i[1][1]))
		print("\n{}\n> \n".format('-'*80))
		
	def ViewList(self):
		print ("\n=<VIEW LIST>{}\n\n".format('='*68))
		for e in (self.s.e):
			print("{}) <{}>: {}".format(e, self.s.e[e].name, self.s.e[e].text[0:30]))
			for _exit in self.s.e[e].exits:
				print(f"\t{_exit[0]}: {_exit[1]}")
	def Save(self):
		confirm = input("Are you sure you want to overwrite any other data? I reccomend you save a copy of your old stuff. Enter (y)es or (n)o.\n\n> ")
		if confirm.lower() == "y":
			temp_string = ""
			temp_string += "{"
			for c, i in enumerate (self.s.e):
				temp_string += "{}:[\"{}\", \"{}\", [".format(c, self.s.e[i].name, self.s.e[i].text)
				for c, e in enumerate (self.s.e[i].exits):
					if c+1 == len(self.s.e[i].exits):
						temp_string += "(\"{}\", {})".format(e[0], e[1])
					else:
						temp_string += "(\"{}\", {}),".format(e[0], e[1])
				temp_string += "]],\n"
			temp_string = temp_string[0:len(temp_string)-2] + "}"
			print ("\n{0}\n{1}\n".format('='*80, temp_string))
			try:
				with open("story.py", 'w') as f:  
					f.write("story = {}".format(temp_string))
				print("Successfully wrote story to file.")
			except:
				print("Couldn't write to file.")
	def Load(self):
		self.s.e = {}
		from story import story as s
		for i in range(0, len(s)):
			self.s.Add(Entry(s[i][0], s[i][1]))
			print(s[i][2])
			for c, _exit in enumerate(s[i][2]):
				self.s.e[i].exits[c-1] = _exit
			
		
			


e = Editor()

