#!/usr/bin/python
#coding:utf-8

from Tkinter import *
import json
from GetDate import getresult

def Translate():
	global vRes
	global text
	data = text.get(1.0,END)
	print data
	res = getresult(data,'json')
	print res
	res = json.loads(res)
	leb = "-"*18 +"BASIC" + "-"*18
	for item in res['basic']["explains"]:
		leb += "\n  " + item
	leb += "\n"+ "-"* 17 + "WEB" + "-"*17
	for item in res['web']:
		leb += "\n " + item['key'] + " : "
		for subitem in item['value']:
			leb += subitem + ','

	print leb
	vRes.set(leb)

MainFrame = Tk()

vRes = StringVar()
vData = StringVar()

button = Button(MainFrame,
		command = Translate,
		text = 'Translate')
text = Text(MainFrame,
		height = 10,
		width = 60,
		wrap=WORD)
label = Label(MainFrame,
		anchor = NW,
		justify = LEFT,
		height = 10,
		textvariable = vRes,
		width = 60,
		bd = 3,
		text= "the reault of Translation!")
button.pack()
text.pack()
label.pack()
MainFrame.mainloop()

