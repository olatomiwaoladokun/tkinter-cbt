
class TestArea(object):
	"""docstring for CSCTest"""
	def __init__(self):
		self.questNo = 0
		self.optSelected = IntVar()
		self.opts = self.radioBtns()
		self.quests = self.question(self.questNo)
		self.showOptions(self.questNo)


	def question(self, questNo):
		text = Label(win, text="CSC101 TEST", font=('times', 20, 'bold'))
		text.place(x=0, y=2)
		questNo = Label(win, text=questions[questNo], font=('times', 16, 'bold'), anchor='w')
		questNo.place(x=70, y=100)
		return questNo


	def radioBtns(self):
		val = 0
		bt = []
		yp = 150
		while val < 4:
			btn = Radiobutton(win, variable=self.optSelected, value=val+1, font=('times', 14))
			bt.apppend(btn)
			btn.place(x=100, y=yp)
			val += 1
			yp += 40
		return bt


	def showOptions(self, questNo):
		val = 0
		self.optSelected.set(0)
		self.quests['text'] = questions[questNo]
		for option in options:
			pass



