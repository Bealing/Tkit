#!/usr/bin/python
#coding:utf-8

from Tkinter import *
import json
from GetDate import getResult


class Application(Frame):
	"""
	Create the windows and widgets
	"""
	def __init__(self, master = None):
		Frame.__init__(self,master)
		self.grid()
		self.__vResult = StringVar()
		self.__CreateWidgets()
	
	def __CreateWidgets(self):
		self.__button = Button(self,
				text = 'Translate',
				command = self.__Translate)
		self.__text = Text(self,
				height = 10, width = 60,
				wrap = WORD)
		self.__label = Label(self,
				anchor = NW, justify = LEFT,
				height = 10, width = 60,
				textvariable = self.__vResult,
				text = "the result of Translation")

		self.__button.pack()
		self.__text.pack()
		self.__label.pack()

	def __Translate(self):
		data = self.__text.get(1.0,END)
		#remove the start and end chars of String:' ' '\n'
		data =  data.strip(" \n").encode('UTF-8')
		if data == '':
			return;
		old_res = getResult(data,'json')
		if old_res == None:
			new_res = 'Translation is Failed!'
		else:
			old_res	= json.loads(old_res)
			try:		
				errorCode = old_res['errorCode']
				if errorCode != 0:
					new_res = 'Translation is Failed!'
				else:
					new_res = "-"*25 +"BASIC" + "-"*25
				for item in old_res['basic']["explains"]:
					new_res += "\n  " + item
				new_res += "\n"+ "-"* 27 + "WEB" + "-"*27
				for item in old_res['web']:
					new_res += "\n " + item['key'] + " : "
					for subitem in item['value']:
						new_res += subitem + ','
			except (KeyError,ValueError):
				new_res = 'Translation is Failed!'
		self.__vResult.set(new_res)

	def run(self):
		self.mainloop()
	
		
app = Application()
app.run()
