
#importing all the modules needed for the GUI development
from tkinter import *
import json
from datetime import datetime as dt






#making an instance of class Tk from module tkinter
#and asigning it to variable win(window)
win = Tk() #creat an instance of class Tk and asign it to varible win (window object)
win.title("CSC101 Test")  #giving the window a title
win.geometry('800x550')	  #set the size of the window
win.configure(bg="#00cc00")	#set the background color

t = 0

def firstPage():
	#create an interface for the test by defining a function
	def startTest():
		win.geometry('900x600')
		win.configure(bg="#999999")
		schName.destroy()
		deptName.destroy()
		instr.destroy()
		intList.destroy()
		startBtn.destroy()

		def timer():
			global t
			t += 25
			return t




		def countDown():
			global t
			if t > 0:
				cdLabel.configure(text=t)
				t -= 1
				cdLabel.after(1000, countDown)
			elif t == 0:
				pass

		#create label for countdown object to display
		cdLabel = Label(win, text='', bg='#999999', font=('calibri', 30, 'bold'))
		cdLabel.pack(side=RIGHT, padx=10, pady=10)
		countDown()



		def testInter():
			qns = 0
			qnLabel = Label(win, text='This is the placeholder for the question', bg="#999999", font=('times', 18))
			qnLabel.pack(anchor='nw', padx=20, pady=35)

		testInter()


		#intance of IntVar class to set the rasio to be (0 or 1)
		radVar = IntVar()

		#create radio button for the test option A
		rad1 = Radiobutton(win, text='option 1', bg='#999999', font=('times', 16), variable=radVar, value='A')
		rad1.pack(anchor='w', padx=70, pady=10)

		#create radio button for the test option B
		rad2 = Radiobutton(win, text='option 2', bg='#999999', font=('times', 16), variable=radVar, value='B')
		rad2.pack(anchor='w', padx=70, pady=10)

		#create radio button for the test option C
		rad2 = Radiobutton(win, text='option 3', bg='#999999', font=('times', 16), variable=radVar, value='C')
		rad2.pack(anchor='w', padx=70, pady=10)

		#create radio button for the test option D
		rad2 = Radiobutton(win, text='option 4', bg='#999999', font=('times', 16), variable=radVar, value='D')
		rad2.pack(anchor='w', padx=70, pady=10)



		#define a callback function for submit button
		def submitBtn():
			print(obj)

		subBtn = Button(win, text='Submit', font=('Arial', 20), command=submitBtn)
		subBtn.pack(side=RIGHT, anchor='se', padx=30, pady=120)


		#define a callback function for previous button
		def previousBtn():
			print('Previous')

		prvBtn = Button(win, text='Previous', font=('Arial', 20), command=previousBtn)
		prvBtn.pack(side=LEFT, anchor='se', padx=150, pady=120)


		#define a callback function for submit button
		def nextBtn():
			print('Next')

		nxtBtn = Button(win, text='Next', font=('Arial', 20), command=nextBtn)
		nxtBtn.pack(side=LEFT, anchor='se', padx=100, pady=120, ipadx=200)


	#create label for the discriptions and instructions to use the app and get its position
	schName = Label(win, text="FEDERAL UNIVERSITY OYE-EKITI", bg="#007700", fg='white', font=('times', 26, 'bold'))
	schName.pack(side=TOP, padx=5, pady=5, fill=X)

	#create label for the name of department and get its position 
	deptName = Label(win, text="Department of Computer Science", bg="#00aa00", fg='white', font=('Arial', 18))
	deptName.pack(side=TOP, padx=5, fill=X)

	#create label for instructions and get its position
	instr = Label(win, text="Instructions:", bg='#00cc00', fg='red', font=('Arial', 16, 'bold'))
	instr.pack(padx=0, pady=20)



	#create label for the list of instructions and get its position
	intlist = '\
	The test you are about to take is a course titled "Introduction to Computer" \n\n \
	The course code is CSC101 \n\n \
	Once you click the start button bellow, your test started \n\n \
	You are to answer all the questions provided \n\n \
	You have 25 minites to answer 50 questions \n\n \
	Click Submit button when you are done with the test \n\n \
	Your scores will be display immidiatly after you submit \n\n \
	Wish you Best of Luck.'

	intList = Label(win, text=intlist, bg='#00cc00', font=(28))
	intList.pack(pady=5)


	#create start button to procede to the test
	startBtn = Button(win, text="Start Test", bg='#aaaaaa', font=('Arial', 20), command=startTest)
	startBtn.pack(side=BOTTOM, pady=30, ipadx=30)

firstPage()


win.mainloop() #calling the event loop to keep the window updated