from tkinter import *
from sys import platform
import tkinter as tk
from tkinter import messagebox


#rgb
def rgb(r,g,b):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return f'#{r:02x}{g:02x}{b:02x}'

def div(name="None"):
	pass

class CodeEditor(Text):
	def __init__(self,master,draggable=False,sublimetheme=False,theme=None,**args):
		super().__init__(master=master,**args)
		self.theme = theme
		if self.theme != None:
			if self.theme == 'python':
				self.scheme_python()
				self.bind("<Key>",self.scheme_python)
		self.draggable = draggable
		if self.draggable == True:
			self.make_draggable()
		if sublimetheme == True:
			self.sublimetheme()

	def sublimetheme(self,arg=None):
		self.config(bg="#272923",fg="#f7f8f2",insertbackground="#f7f8f2")
		return "#272923","#f7f8f2"
	def clear(self):
		self.delete('1.0','end')
	def find(self,word='',background='red',foreground='white'): 
		s = word
		self.tag_remove('found', '1.0', END) 
		if s: 
			idx = '1.0'
			while True: 
				idx = self.search(s, idx, nocase=1,stopindex=END) 
				if not idx: break
				lastidx = '%s+%dc' % (idx, len(s)) 
				self.tag_add('found', idx, lastidx) 
				idx = lastidx  
			self.tag_config('found', background=background,foreground=foreground)
	def paste(self):
		self.insert(self.index(INSERT),self.clipboard_get())
	def colorscheme(self,colour,word):
		for s in word:
			if s: 
				idx = '1.0'
				while True: 
					idx = self.search(s, idx, nocase=1,stopindex=END) 
					if not idx: break
					lastidx = '%s+%dc' % (idx, len(s)) 
					self.tag_add(colour, idx, lastidx) 
					idx = lastidx 
				self.tag_config(colour, foreground=colour)

	def curly(self,arg=None):
		position = self.index(INSERT)
		self.insert(position,"()")
		self.cursor_set_back()
		return 'break'

	def insert_tabs(self,arg=None):
		code_given = str(self.get(SEL_FIRST,SEL_LAST))
		code_given = code_given.splitlines()
		code_formatted = []
		for lines in code_given:
			code_formatted.append((" "*4)+lines)
		x,y = SEL_FIRST,SEL_LAST
		self.delete(x,y)
		code_formatted = '\n'.join(code_formatted)
		position = self.index(INSERT)
		self.insert(position,code_formatted)

	def remove_tabs(self,arg=None):
		code_given = str(self.get(SEL_FIRST,SEL_LAST))
		code_given = code_given.splitlines()
		code_formatted = []
		for lines in code_given:
			code_formatted.append(lines[4:])
		x,y = SEL_FIRST,SEL_LAST
		self.delete(x,y)
		code_formatted = '\n'.join(code_formatted)
		position = self.index(INSERT)
		self.insert(position,code_formatted)
		return 'break'

	def tab(self,arg=None):
		try: self.insert_tabs()
		except: pass
		self.insert(self.index(INSERT)," "*4)
		return 'break'

	def quotation1(self,arg=None):
		self.insert(self.index(INSERT),"''")
		self.cursor_set_back()
		return 'break'

	def cursor_set_back(self,arg=None):
		position = self.index(INSERT)
		position = position.split(".")
		position = [position[0],str(int(position[1])-1)]
		position = '.'.join(position)
		self.mark_set("insert", f"{position}")

	def quotation2(self,arg=None):
		self.insert(self.index(INSERT),'""')
		self.cursor_set_back()
		return 'break'

	def brackets(self,arg=None):
		self.insert(self.index(INSERT),'[]')
		self.cursor_set_back()
		return 'break'

	def curlybraces(self,arg=None):
		self.insert(self.index(INSERT),'{}')
		self.cursor_set_back()
		return 'break'

	def remove_line(self,arg=None):
		position = self.index(INSERT)
		position2 = position.split(".")
		position1 = float(position2[0]+".0")
		self.delete(str(position1),str(position))


	def scheme_python(self,arg=None):
		yellow =  ['"',"'",'""',"''"]

		purple =  ['True','False','1','2','3','4','5','6','7','8','9','0']

		cyan =  ['len','def ',' int',' str',
				' float',' bool',' sum','append',
				'print','zip','class']

		red =  ['if ','else ','while ','elif ','for ',' in ',
			  ' = ',' + ',' / ',' * ','import ','from ',' as ',
			  'global ',' not ','break',' % ','=!','+=','-']

		green = []

		keys = [[yellow,"#e8db61"],[purple,"#b57aff"],
				[cyan,"#23daf2"],[red,"#ff0070"],[green,"#92e500"]]

		for key in keys:
			self.colorscheme(word=key[0],colour=key[1])

	def keyboard(self,arg=None,linebar=None):
		self.bind("(",self.curly)
		self.bind("<Tab>",self.tab)
		self.bind("<Shift-Tab>",self.remove_tabs)
		if platform == "darwin":
			self.bind("<Command-BackSpace>",self.remove_line)
			self.bind("<Command-c>",self.copy)
		if linebar != None:
			self.bind("<Return>",linebar.run)
		self.bind("'",self.quotation1)
		self.bind('"',self.quotation2)
		self.bind("[",self.brackets)
		self.bind("{",self.curlybraces)

	def fit(self,master,onmotion=False):
		def on_drag_motion(self,master,event=None):
			width = master.winfo_width()
			height = master.winfo_height()
			self.config(width=width,height=height)
		on_drag_motion(self,master)
		if onmotion == True:
			master.bind("<Button-1>", lambda x: on_drag_motion(self=self,master=master))

	def getAll(self):
		return self.get('1.0','end-1c')

	def copy(self,args=None):
		self.clipboard_clear()
		try:
			text = str(self.get(SEL_FIRST,SEL_LAST))
		except:
			text = str(self.get('1.0','end'))
		self.clipboard_append(text)
		try:
			self.clipboard_update()
		except:
			pass


	def make_draggable(self):
		def drag_start(event):
			widget = self
			widget = event.widget
			self._drag_start_x = event.x
			self._drag_start_y = event.y

		def drag_motion(event):
			widget = self
			widget = event.widget
			x = self.winfo_x() - self._drag_start_x + event.x
			y = self.winfo_y() - self._drag_start_y + event.y
			self.place(x=x, y=y)
		self.bind("<Button-1>", drag_start)
		self.bind("<B1-Motion>", drag_motion)
	def lineview(self):
		return int(self.index('end-1c').split('.')[0])
	def defaultmenu(self):
		menu = Menu(self,tearoff=False)
		menu.add_command(label="Copy",command=self.copy)
		menu.add_command(label="Paste",command=self.paste)
		menu.add_command(label="Redo",command=self.edit_redo)
		menu.add_command(label="Undo",command=self.edit_undo)
		menu.add_command(label="Clear",command=self.clear)
		def popup(e):
			menu.tk_popup(e.x_root,e.y_root)
		self.bind("<Button-2>",popup)
		self.bind("<Button-3>",popup)

class Linebar(Text):
	def __init__(self,master,lineview,sublimetheme=False,**args):
		super().__init__(master=master,**args,width=3)
		self.lineview = lineview
		self.config(state=DISABLED)
		if sublimetheme == True:
			self.sublimetheme()
	def line(self,linenumber):
		self.linenumber = self.lineview.lineview
		def insert_():
			self.delete("1.0","end-1c")
			end = 0
			for i in range(1,int(self.linenumber())):
				self.insert(float(str(i)+".0"),str(i)+"	")
				end = i
			self.insert(float(str(end+1)+".0"),str(end+1)+"	")
		self.config(state='normal')
		insert_()
		self.config(state=DISABLED)

	def scroll(self,*args):
		self.yview(*args)
		self.lineview.yview(*args)		

	def sublimetheme(self,arg=None):
		self.config(bg="#272923",fg="#f7f8f2",insertbackground="#f7f8f2")
		return "#272923","#f7f8f2"

	def run(self,arg):
		s = self.line(linenumber=self.lineview)








def test():
	#demo testing area


	window = Tk()



	scrollbar = Scrollbar(window,orient=VERTICAL)
	scrollbar.grid(row=0,column=2,sticky=N+S)

	s = CodeEditor(window,theme="python",sublimetheme=True,draggable=True,yscrollcommand=scrollbar.set,bg="white")
	s.grid(row=0,column=1)

	y = Linebar(window,bg="white",fg='black',yscrollcommand=scrollbar.set,lineview=s)
	y.grid(row=0,column=0)

	s.keyboard(linebar=y)
	s.sublimetheme()
	s.defaultmenu()

	scrollbar.config(command=y.scroll)
	Button(window,command=s.lineview).grid(row=1,column=1)
	window.mainloop()

if __name__ == "__main__":
	test()

def Tooltip(widget=None,text="",bg="white",fg="black",font=None,width=None,height=None,plusx=0,plusy=0,function=None):
	def show_position(e):
		x, y = widget.winfo_rootx(),widget.winfo_rooty()
		window = tk.Toplevel()
		window.config(bg=bg)
		window.overrideredirect(True)
		label_text = Label(window,text=text,bg=bg,fg=fg)
		label_text.pack()
		if font != None:
			label_text.config(font=font)
		x,y = x+15+plusx,y-25+plusy
		window.geometry(f'+{x}+{y}')
		def leave(arg=None):
			widget.config(bg="white")
			window.destroy()

		widget.bind("<Leave>",leave)
		def dest(arg):
			window.destroy()
			function()
		if function != None:
			widget.bind("<Button-1>",dest)
		if width != None: label_text.config(width=width)
		if height != None: label_text.config(height=height)
		window.mainloop()
	def enter(e):
		widget.config(bg="lightgrey")
		show_position(e)
	widget.bind("<Enter>",enter)

import sys
class Tk(tk.Tk):
	def destroy(arg):
		option = messagebox.askyesno("Quit","Are you sure you want to quit?")
		if option == True:
			super().destroy()
		else:
			pass
	def quit():
		sys.exit()
		super().quit()


class TkPlain(tk.Toplevel):
	def __init__(self):
		super().__init__()
		self.bind('<Button-1>', self.SaveLastClickPos)
		self.bind('<B1-Motion>', self.Dragging)
		self.lastClickX = 0
		self.lastClickY = 0
		self.drag = [True]
	def SaveLastClickPos(self,event):
	    self.lastClickX = event.x
	    self.lastClickY = event.y
	def Dragging(self,event):
		if self.drag[0] == True:
		    x, y = event.x - self.lastClickX + self.winfo_x(), event.y - self.lastClickY + self.winfo_y()
		    self.geometry("+%s+%s" % (x , y))
	def stopdrag(self,arg):
		self.drag[0] = False
	def startdrag(self,arg):
		self.drag[0] = True

class Drag:
    def __init__(self,widget):
        self.widget=widget
        self.widget.bind("<Button-1>", self.drag_start)
        self.widget.bind("<B1-Motion>", self.drag_motion)
        self.grid=(10,10)
        self.margin=(500,500)

    def drag_start(self,event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def drag_motion(self,event):
        x = self.widget.winfo_x() - self._drag_start_x + event.x
        y = self.widget.winfo_y() - self._drag_start_y + event.y
        if (
            x%self.grid[0] in range(self.margin[0]) and 
            y%self.grid[1] in range(self.margin[1])
        ):
            self.widget.place(x=x-x%self.grid[0],y=y-y%self.grid[1])
        else:
            self.widget.place(x=x, y=y)

class Labelv(tk.Label):
	def putvalue(self,value):
		self.value = value
	def getvalue(self):
		try:
			return self.value
		except:
			return None
	def draggable(self):
		def drag_start(event):
			widget = self
			widget = event.widget
			self._drag_start_x = event.x
			self._drag_start_y = event.y

		def drag_motion(event):
			widget = self
			widget = event.widget
			x = self.winfo_x() - self._drag_start_x + event.x
			y = self.winfo_y() - self._drag_start_y + event.y
			self.place(x=x, y=y)
		self.bind("<Button-1>", drag_start)
		self.bind("<B1-Motion>", drag_motion)




class Toplevel2(tk.Toplevel):
	def addexit(self,func):
		self.func = func
	def destroy(self):
		self.func()
		super().destroy()

class hoverLabel(tk.Label):
	def hover(self,bg={"entry":"black","leave":"white"},fg={"entry":"white","leave":"black"},command=None):
		def function(arg=None):
			try:
				command()
			except:
				pass
			self.config(bg=bg["entry"],fg=fg["entry"])

		self.bind("<Enter>",function)
		self.bind("<Leave>",lambda event: self.config(bg=bg["leave"],fg=fg["leave"]))



import tkinter as tk

class Option(tk.Frame):
	def __init__(self,parent,function,option,image,*args,**kwargs):
		tk.Frame.__init__(self,parent,*args,**kwargs)
		self.function = function
		self.parent = parent
		self.config(bg="white")

		self.icon =	tk.Label(self,bg="white")
		self.icon.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
		try: self.icon.config(image=image)
		except: pass

		self.label = tk.Label(self,text=option.capitalize(),bg="white",fg="black",font=("avenir",20))
		self.label.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH,padx=20)
		self.bind("<Button-1>",self.clicked)
		self.label.bind("<Button-1>",self.clicked)

	def clicked(self,arg=None):
		self.config(bg="#2b68d1")
		self.label.config(bg="#2b68d1",fg="white")
		self.icon.config(bg="#2b68d1")
		self.function()

	def unclicked(self):
		self.config(bg="white")
		self.label.config(bg="white",fg="black")
		self.icon.config(bg='white')

class ElementBox(tk.Label):
	def interactive(self,colour):
		bg = self.cget("bg")

		def enter(arg=None):
			self.config(bg=colour)
		def leave(arg=None):
			self.config(bg=bg)

		
		self.bind("<Enter>",enter)
		self.bind("<Leave>",leave)

