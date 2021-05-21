import tkinter as tk
from tkinter import ttk,messagebox
from tkinterplus import rgb
from advtable import panel
import tkinterplus as ttx
import os
from graph import plot
from tkinter import filedialog
from PIL import Image
import time
import threading


bg = "white"
fg = "black"
font = "avenir"
fontSiz = 15



def advancedpanel(base,current,reinsert,data,data2,icon):
	data2 = data2
	window = tk.Canvas(base,bg=bg)
	window.pack(side=tk.RIGHT,fill=tk.BOTH)

	global plotbase
	plotbase = tk.Frame(base,bg=bg)
	plotbase.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

	def close(arg=None):
		plotbase.destroy()
		window.destroy()
		reinsert()

	plotback = tk.Label(plotbase,text="Back",bg="#f44336",fg=fg,font=(font,fontSiz))
	plotback.pack(fill=tk.BOTH)
	plotback.bind("<Button-1>",close)

	sidetop = tk.Frame(window,bg=bg)
	sidetop.pack(expand=True,fil=tk.BOTH,side=tk.TOP)

	sidebottom = tk.Frame(window,bg=bg)
	sidebottom.pack(expand=True,fill=tk.BOTH,side=tk.BOTTOM)


	global buttons,panelwin
	buttons,panelwin = panel(base=plotbase,current=current,reinsert=reinsert,secwindow=window)

	def placeholder(arg=None):
		if str(entry.get()) == "Type an element name...":
			entry.config(fg="black")
			entry.delete(0,tk.END)
		else:
			pass

	def search(event):
		placeholder()
		clearall()
		arg = str(entry.get()).lower()
		notblack = []

		for button in buttons:
			if button.getvalue().lower().find(arg) != -1:
				notblack.append(button)

		u = []
		for button in buttons:
			u.append(button)
		for button in u:
			for notb in notblack:
				if button == notb:
					u.remove(button)
		
		for button in u:
			button.config(bg="lightgrey")

	
	entry = tk.Entry(sidetop,bg=bg,fg="lightgrey",font=(font,"20"),highlightbackground=fg,insertbackground="black")
	entry.grid(row=1,column=0,padx=20,pady=20,columnspan=2,sticky=tk.W+tk.E)
	entry.bind("<Return>",search)
	entry.bind("<Key>",search)
	entry.focus_set()
	entry.insert(0,"Type an element name...")
	entry.bind("<Button-1>",placeholder)
	entry.icursor(0)

	tk.Label(sidetop,bg=rgb(23,27,33),fg="orange",text="Beta",font=(font,'18')).grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)
	
	def focus(arg=None):
		if str(entry.get()) == "":
			entry.insert(0,"Type an element name...")
			entry.icursor(0)
			entry.bind("<FocusIn>",focus)
	entry.bind("<FocusOut>",focus)
		

	def highlight(classification=None,plot_=None,group=None,period=None): 
		for button in buttons:
			for element in data:
				if button.getvalue() == element["Element"]:
					button.config(bg=element["ColourLight"])
		blackbut = []
		if group != None:
			for element in data:
				if element["Group"] != group:
					blackbut.append(element["Element"])

		if period != None:
			for element in data:
				if element["Period"] != period:
					blackbut.append(element["Element"])

		if classification != None:
			for element in data:
				if element["Category"] != classification:
					blackbut.append(element["Element"])

		for button in buttons:
			for bbut in blackbut:
				if button.getvalue() == bbut:
					button.config(bg="lightgrey")

	

	def clearall(arg=None):
		for button in buttons:
			for element in data:
				if button.getvalue() == element["Element"]:
					button.config(bg=element["ColourLight"])
		ievar.set(0)
		secvar.set(0)

	


	pos = []
	def savepos(arg):
		for button in buttons:
			pos.append([button.winfo_x(),button.winfo_y()])
		height,width = base.winfo_height(),base.winfo_width()
		save_pos = [pos,[height,width]]
		with open("henry.save","w") as writefile:
			writefile.write(str(save_pos))
		save.config(text="Saved!")
		def _save_(arg=None):
			time.sleep(2)
			save.config(text="Save")
		threading.Thread(target=_save_).start()
		

	ievar = tk.IntVar()
	secvar = tk.IntVar()


	def iefunc(arg):
		for button in buttons:
			for element in data:
				if button.getvalue() == element["Element"]:
					button.config(bg=element["ColourLight"])
		blackbut = []

		for element in data:
			if int(element["First Ionization Energy"]) > int(ievar.get()):
				blackbut.append(element["Element"])
		for button in buttons:
			for bbut in blackbut:
				if button.getvalue() == bbut:
					button.config(bg="lightgrey")

	def secfunc(arg):
		for button in buttons:
			for element in data:
				if button.getvalue() == element["Element"]:
					button.config(bg=element["ColourLight"])
		blackbut = []

		for element in data:
			if element["Second Ionization energy"] == 'Unknown':
				if 0 > int(secvar.get()):
					blackbut.append(element["Element"])
			else:
				if int(element["Second Ionization energy"]) > int(secvar.get()):
					blackbut.append(element["Element"])
		for button in buttons:
			for bbut in blackbut:
				if button.getvalue() == bbut:
					button.config(bg="lightgrey")


	ielist,seclist = [],[]
	for element in data:
		ielist.append(element["First Ionization Energy"])
		if element["Second Ionization energy"] == 'Unknown':
			seclist.append(0)
		else:
			seclist.append(element["Second Ionization energy"])

	classify = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="Classification",font=(font,fontSiz))
	classify.grid(row=2,column=0,columnspan=2,pady=20,padx=20,sticky=tk.E+tk.W)

	metal_ = ttx.hoverLabel(classify,text="Metal",bg=bg,fg=fg,font=(font,fontSiz))
	metal_.grid(row=0,column=0,padx=10)
	metal_.hover(command=lambda: highlight(classification="Metal"))

	nonmetal_ = ttx.hoverLabel(classify,text="Non-Metal",bg=bg,fg=fg,font=(font,fontSiz))
	nonmetal_.grid(row=0,column=1,padx=10)
	nonmetal_.hover(command=lambda: highlight(classification="Non metal"))

	metalloid_ = ttx.hoverLabel(classify,text="Metalloid",bg=bg,fg=fg,font=(font,fontSiz))
	metalloid_.grid(row=0,column=2,padx=10)
	metalloid_.hover(command=lambda: highlight(classification="Metalloid"))

	group = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="Group",font=(font,fontSiz))
	group.grid(row=3,column=0,pady=20,padx=20,sticky=tk.E+tk.W,columnspan=2)

	row,column = 0,0
	for button in range(1,19):
		gb = ttx.hoverLabel(group,bg=bg,fg=fg,text=button,font=(font,fontSiz))
		gb.grid(row=row,column=column)
		gb.hover(command=lambda group=button: highlight(group=group))
		
		column+=1
		if column == 9:
			row+=1
			column = 0

	period = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="Period",font=(font,fontSiz))
	period.grid(row=4,column=0,pady=20,padx=20,sticky=tk.E+tk.W+tk.N+tk.S,columnspan=2)

	row,column = 0,0
	for button in range(1,8):
		pb = ttx.hoverLabel(period,bg=bg,fg=fg,text=button,font=(font,fontSiz))
		pb.grid(row=row,column=column,padx=2,pady=2)
		pb.hover(command=lambda period=button: highlight(period=period))
		column+=1
		if column == 7:
			row+=1
			column = 0


	def pplot(plotfor,data2):

		global plotbase
		for widget in plotbase.winfo_children():
			widget.destroy()
		plotback = tk.Label(plotbase,text="Back",bg="#f44336",fg=fg,font=(font,fontSiz))
		plotback.pack(fill=tk.BOTH)
		plotback.bind("<Button-1>",goback)
		canva = plot(datatoplot=plotfor,window=plotbase,data2=data2,data=data)
		

	plot_ = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="Plot",font=(font,fontSiz))
	plot_.grid(row=5,column=0,pady=20,padx=20,sticky=tk.E+tk.W,columnspan=2)

	atmass = ttx.hoverLabel(plot_,bg=bg,fg=fg,text="Atomic Mass",font=(font,fontSiz))
	atmass.grid(row=0,column=0,padx=10)
	atmass.hover()
	atmass.bind("<Button-1>",lambda event: pplot(plotfor="atomicmass",data2=data2))

	density = ttx.hoverLabel(plot_,bg=bg,fg=fg,text="Density",font=(font,fontSiz))
	density.grid(row=0,column=1,padx=10)
	density.hover()
	density.bind("<Button-1>",lambda event: pplot(plotfor="density",data2=data2))

	mpoint = ttx.hoverLabel(plot_,bg=bg,fg=fg,text="Melting Point",font=(font,fontSiz))
	mpoint.grid(row=1,column=0,padx=10)
	mpoint.hover()
	mpoint.bind("<Button-1>",lambda event: pplot(plotfor="mp",data2=data2))

	bpoint = ttx.hoverLabel(plot_,bg=bg,fg=fg,text="Boiling Point",font=(font,fontSiz))
	bpoint.grid(row=1,column=1,padx=10)
	bpoint.hover()
	bpoint.bind("<Button-1>",lambda event: pplot(plotfor="bp",data2=data2))

	


	def goback(arg=None):
		global plotbase
		for widget in plotbase.winfo_children():
			widget.destroy()
		global buttons,panelwin
		plotback = tk.Label(plotbase,text="Back",bg="#f44336",fg=fg,font=(font,fontSiz))
		plotback.pack(fill=tk.BOTH)
		plotback.bind("<Button-1>",close)
		buttons,panelwin = panel(base=plotbase,current=current,reinsert=reinsert,secwindow=window)
		

	def restore(arg=None):
		try:
			with open("henry.save","r") as readfile:
				save_pos = eval(readfile.read())
			posprev = save_pos[0]
			resize = messagebox.askyesno("Restore","Do you want to restore window size?")
			if resize == True:
				base.geometry(f"{save_pos[1][1]}x{save_pos[1][0]}")
			t = 0
			for button in buttons:
				button.place(x=posprev[t][0],y=posprev[t][1])
				t+=1
			restorebut.config(text="Restored!")
			def _restore_(arg=None):
				time.sleep(2)
				restorebut.config(text="Restore")
			threading.Thread(target=_restore_).start()
		except:
			restorebut.config(text="Failed")
			def _restore_(arg=None):
				time.sleep(2)
				restorebut.config(text="Restore")
			threading.Thread(target=_restore_).start()


	restorebut = ttx.hoverLabel(sidetop,bg=rgb(65, 151, 242),fg="white",text="Restore",highlightcolor="white",padx=10,pady=10)
	restorebut.grid(row=8,column=1,sticky=tk.W+tk.E+tk.N+tk.S,padx=10,pady=10)
	restorebut.bind("<Button-1>",restore)
	restorebut.hover(bg={"entry":rgb(11, 92, 179),"leave":rgb(65, 151, 242)},fg={"entry":"white","leave":"white"})

	save = ttx.hoverLabel(sidetop,bg=rgb(65, 151, 242),fg="white",padx=10,pady=10,text="Save")
	save.grid(row=8,column=0,sticky=tk.W+tk.E+tk.N+tk.S,padx=10,pady=10)
	save.bind("<Button-1>",savepos)
	save.hover(bg={"entry":rgb(11, 92, 179),"leave":rgb(65, 151, 242)},fg={"entry":"white","leave":"white"})

	clear = ttx.hoverLabel(sidetop,bg=rgb(65, 151, 242),fg="white",text="Clear",highlightcolor="white",padx=10,pady=10)
	clear.grid(row=7,column=1,sticky=tk.W+tk.E+tk.N+tk.S,padx=10,pady=10)
	clear.bind("<Button-1>",clearall)
	clear.hover(bg={"entry":rgb(11, 92, 179),"leave":rgb(65, 151, 242)},fg={"entry":"white","leave":"white"})

	def default(arg=None):
		try:
			goback()
		except:
			pass
		base.geometry("1200x750")
		global buttons,panelwin
		panelwin.destroy()
		buttons,panelwin = panel(base=plotbase,current=current,reinsert=reinsert,secwindow=window)

	default_state = ttx.hoverLabel(sidetop,bg=rgb(65, 151, 242),fg="white",text="Default",highlightcolor="white",padx=10,pady=10)
	default_state.grid(row=7,column=0,sticky=tk.W+tk.E+tk.N+tk.S,padx=10,pady=10)
	default_state.bind("<Button-1>",default)
	default_state.hover(bg={"entry":rgb(11, 92, 179),"leave":rgb(65, 151, 242)},fg={"entry":"white","leave":"white"})

	'''	
	scale = tk.StringVar()
	scaleoption = ttk.Combobox(sidetop,state='readonly',textvariable=scale)
	scaleoption.grid(row=7,column=0,columnspan=2,sticky=tk.W+tk.E,padx=10)
	scaleoption['values'] = ('First Ionization Energy',)
	scaleoption.current(0)'''

	first_ionization_energy = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="First Ionization Energy",font=(font,fontSiz))
	first_ionization_energy.grid(row=6,column=0,pady=20,padx=20,sticky=tk.E+tk.W,columnspan=2)

	scale = tk.Scale(first_ionization_energy,bd=2,bg=bg,troughcolor="white",fg=fg,orient=tk.HORIZONTAL,variable=ievar,from_=0, to_=max(ielist), command=iefunc,highlightbackground="white",highlightcolor="white",activebackground="white",length=300)
	scale.grid(row=0,column=0,columnspan=2,sticky=tk.W+tk.E)

	tip = tk.LabelFrame(sidetop,bg=bg,fg=fg,text="Tip ",font=(font,fontSiz))
	tip.grid(row=9,column=0,pady=20,padx=20,sticky=tk.E+tk.W,columnspan=2)

	tip_detail = tk.Label(tip,text="This is where the tip is displayed",bg=bg,fg=fg,font=(font,fontSiz))
	tip_detail.pack(fill=tk.BOTH)

