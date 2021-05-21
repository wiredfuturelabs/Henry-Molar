import tkinter as tk

def rgb(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

class legend(tk.Frame):
	def __init__(self,parent,*args,**kwargs):
		super().__init__(parent,*args,**kwargs)
		for i in range(0,5):
			self.grid_rowconfigure(i,weight=1)
		for i in range(0,7):
			self.grid_columnconfigure(i,weight=1)
		bg = rgb(23,27,33)
		self.config(bg=bg)
		row,column = 0,0
		colours = ["#EBBFD8","#FBC9E5","#5BC2E7","#BFEAEC","#CEDC00","#D1A2CB","#00D600","#A2D34D","#F0B323","#EAB37F","#EADA24"]
		
		for colour in colours:
			if row == 4:
				row = 0
				column+=2
			tk.Label(self,bg=colour,fg=colour,text=" ",padx=5).grid(row=row,column=column,padx=10,pady=5)
			row+=1

		labels = ["Alkali Metals","Alkaline Earth Metals","Transition Metals","Lanthanides","Boron Family","Carbon Family","Pnictogen","Actinides","Chalcogen","Halogen","Noble Gas"]
		row,column =0,1
		self.name_labels = []
		for label in labels:
			if row == 4:
				row = 0
				column+=2
			v = tk.Label(self,bg=bg,fg="white",text=label)
			v.grid(row=row,column=column,padx=(1,10),pady=5,sticky=tk.W)
			self.name_labels.append(v)
			row+=1
	def changecolour(self,bg,fg):
		self.config(bg=bg)
		for labels in self.name_labels:
			labels.config(bg=bg,fg=fg)
