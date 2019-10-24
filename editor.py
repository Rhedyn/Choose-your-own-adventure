class Story():
	def __init__(self):
		self.e = {}
	def Add(self, entry):
		self.e[len(self.e)] = entry
	
	
class Entry():
	def __init__(self, name = "DEFAULT", text = "DEFAULT"):
		self.name = name
		self.text = text
		self.additions = []
		self.removals = []
		self.exits = [("DEFAULT", 0)]
		
	def EditName(self):
		print (f"\n=<EDIT NAME>{'='*68}\n")
		self.name = input("What should the new name be?\n\n> ")
		
	def EditText(self):
		print (f"\n=<EDIT TEXT>{'='*68}\n")
		self.text = input("What should the new text be?\nBe aware of the following formattings:\n-> Player name  = !yn\n-> No Speaker   = !no\n-> Typing Pause = !ps\n\n> ")
	
	def EditExits(self):
		print (f"\n=<EDIT EXITS>{'='*67}\n")
		for i in enumerate (self.exits):
			print(f"{i[0]} - {i[1][0]}: {i[1][1]}")
		choice = input("Which exit would you like to change?\n\n> ")
		for c, i in enumerate (self.exits):
			if choice == str(c):
				tempText = input("Please enter the exit text\n\n> ")
				tempID = input("Please enter the pointer\n\n> ")
				self.exits[c] = (tempText, tempID)
	
	def AddExit(self):
		print (f"\n=<ADD EXIT>{'='*69}\n")
		tempText = input("Please enter the exit text\n\n> ")
		tempID = input("Please enter the pointer\n\n> ")
		print ("<DEBUG> Text: ", tempText," ID: " ,tempID)
		self.exits.append((tempText, tempID))
	
	def RemoveExit(self):
		print (f"\n=<REMOVE EXITS>{'='*65}\n")
		for i in enumerate (self.exits):
			print(f"{i[0]} - {i[1][0]}: {i[1][1]}")
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
			choice = input(f"""
=<EDIT STORY>{'='*67}

CURRENT ENTRY ID - {self.currentID}
NUMBER OF ENTRIES - {len(self.s.e)}

What would you like to do?
			
{'-'*79}
			
1) Choose another Entry
2) Add a new Entry
3) Change a part of the current entry
4) See how the current entry looks
5) See a list of all entries
6) Save the dictionary
7) Load existing story from story.py\n\n> """)
			
			if choice == "1": self.ChangeID()
			
			if choice == "2":
				self.s.Add(Entry())
				print("Added a new blank entry.")
			
			if choice == "3": self.EditEntry()
			
			if choice == "4": self.ViewEntry()
			
			if choice == "5": self.ViewList()
			
			if choice == "6": self.Save()
			
			if choice == "7": self.Load()
	
	def ChangeID(self):
		print(f"\n=<MOVE TO ID>{'='*67}\n\n Which ID would you like to move to?\n{'-'*79}")
		for e in (self.s.e):
			print(f"{e}) <{self.s.e[e].name[0:20]}>: {self.s.e[e].text[0:59]}")
			for _exit in self.s.e[e].exits:
				print(f"\t{_exit[0]}: {_exit[1]}")
		requestedID = input(f"{'-'*79}\nPlease give the entry ID you want to switch to\n\n> ")
		for k in self.s.e:
			if str(k) == requestedID:
				self.currentID = int(requestedID)
	
	def EditEntry(self):
		while True:
			choice = input(f"""
=<EDIT ENTRY>{'='*67}

What Part of the Entry would you like to change?

{'-'*79}

1) Change name of speaker
2) Change dialogue
3) Edit existing exits
4) Add a new exit
5) Remove an exit\n\n> """)
			
			if choice == "1": self.s.e[self.currentID].EditName()
			if choice == "2": self.s.e[self.currentID].EditText()
			if choice == "3": self.s.e[self.currentID].EditExits()
			if choice == "4": self.s.e[self.currentID].AddExit()
			if choice == "5": self.s.e[self.currentID].RemoveExit()
			if choice == "": break
			
	def ViewEntry(self):
		print(f"\n=<VIEW ENTRY>{'='*67}\n\n<Additions: {self.s.e[self.currentID].additions}, Removals: {self.s.e[self.currentID].removals}>\n<{self.s.e[self.currentID].name}>: {self.s.e[self.currentID].text}\n\n{'-'*79}\n")
		for i in enumerate (self.s.e[self.currentID].exits):
			print(f"Enum: {i[0]} - <Text: {i[1][0]}> (Pointer: {i[1][1]})")
		print(f"\n{'-'*79}\n> \n")
		
	def ViewList(self):
		print (f"\n=<VIEW LIST>{'='*68}\n\n")
		for e in (self.s.e):
			print(f"{e}) <{self.s.e[e].name[0:20]}>: {self.s.e[e].text[0:72-len(self.s.e[e].name)]}")
			for _exit in self.s.e[e].exits:
				print(f"\t- {_exit[0]}: {_exit[1]}")
	def Save(self):
		confirm = input("Are you sure you want to overwrite any other data? I reccomend you save a copy of your old stuff. Enter (y)es or (n)o.\n\n> ")
		if confirm.lower() == "y":
			temp_string = ""
			temp_string += "{"
			for c, i in enumerate (self.s.e):
				temp_string += f"{c}:[{self.s.e[i].additions}, {self.s.e[i].removals}, \"{self.s.e[i].name}\", \"{self.s.e[i].text}\", ["
				for c, e in enumerate (self.s.e[i].exits):
					if c+1 == len(self.s.e[i].exits):
						temp_string += f"(\"{e[0]}\", {e[1]})"
					else:
						temp_string += f"(\"{e[0]}\", {e[1]}),"
				temp_string += "]],\n"
			temp_string = temp_string[0:len(temp_string)-2] + "}"
			print (f"\n{'='*79}\n{temp_string}\n")
			try:
				with open("story.py", 'w') as f:  
					f.write(f"story = {temp_string}")
				print("Successfully wrote story to file.")
			except:
				print("Couldn't write to file.")
				
	def Load(self):
		self.s.e = {}
		from story import story as s
		for i in range(0, len(s)):
			self.s.Add(Entry(s[i][2], s[i][3]))
			self.s.e[i].exits = s[i][4]
			self.s.e[i].additions = s[i][0]
			self.s.e[i].removals = s[i][1]
			
e = Editor()

