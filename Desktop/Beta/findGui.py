import tkinter as tk
from tkinter import ttk
from molmass import Formula

class info(ttk.Frame):
	def build_for_element(self,element,bg,fg,font):
		for i in range(0,14):
			self.grid_rowconfigure(i,weight=1)
		for i in range(0,5):
			self.grid_columnconfigure(i,weight=1)
		labels = ["Atomic Number:","Element Name:","Symbol:",
				"Group:","Period:","Atomic Mass:","Density:",
				"Category:","Group Name:","Electronic Configuration:",
				"Melting Point:","Boiling Point:","Block:",
				"First Ionization Energy:","Second Ionization Energy:",
				"Third Ionization Energy:","Isotopes:","Electronegativity:",
				"Electropositivity:","Electron Affinity:","Vander waals radius:",
				"Atomic Radius:","Atomic Volume:","Oxistates:","Abundance Crust:",
				"Lattice Constant:"]
		c = 0
		for i,label in enumerate(labels):
			if i >= 13:
				c = 2
				i-=13
			tk.Label(self,text=label,bg=bg,fg=fg,font=font).grid(row=i,column=c,sticky=tk.W)
		values = [element[0]["atomic_number"],element[0]["name"],element[1]["Symbol"],
				  element[1]["Group"],element[1]["Period"],element[0]["atomic_weight"],
				  element[0]["density"],element[1]["Category"],element[1]["Group Name"],
				  element[0]["econf"],element[0]["melting_point"],element[0]["boiling_point"],
				  element[0]["block"],element[1]["First Ionization Energy"],element[1]["Second Ionization energy"],
				  element[1]["Third Ionization Energy"],element[1]["Isotopes"],element[0]["en_pauling"],
				  element[1]["Electronpositivity"],element[0]["electron_affinity"],element[0]["vdw_radius"],
				  element[0]["atomic_radius"],element[0]["atomic_volume"],element[0]["oxistates"],element[0]["abundance_crust"],
				  element[0]["lattice_constant"]]
		c = 1
		for i,value in enumerate(values):
			if i >= 13:
				c = 4
				i-=13
			tk.Label(self,text=value,bg=bg,fg=fg,font=font).grid(row=i,column=c,sticky=tk.W)
	def build_for_compound(self,compound,bg,fg,font):
		for i in range(0,6):
			self.grid_rowconfigure(i,weight=1)
		for i in range(0,2):
			self.grid_columnconfigure(i,weight=1)
		tk.Label(self,text="Formula",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=0,column=0)
		tk.Label(self,text=Formula(compound).formula,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=0,column=1)
		tk.Label(self,text="Empirical Formula",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=1,column=0)
		tk.Label(self,text=Formula(compound).empirical,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=1,column=1)
		tk.Label(self,text="Mass",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=2,column=0)
		tk.Label(self,text=Formula(compound).mass,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=2,column=1)
		tk.Label(self,text="Mass of Isotope",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=3,column=0)
		tk.Label(self,text=Formula(compound).isotope.mass,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=3,column=1)
		tk.Label(self,text="Isotope Mass Number:",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=4,column=0)
		tk.Label(self,text=Formula(compound).isotope.massnumber,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=4,column=1)
		tk.Label(self,text="Atoms:",bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=5,column=0)
		tk.Label(self,text=Formula(compound).atoms,bg=bg,fg=fg,font=font).grid(sticky=tk.W,row=5,column=1)

	def frame_reset(self):
		for widgets in self.winfo_children():
			widgets.destroy()


def test():
	window = tk.Tk()
	window.config(bg="white")
	findFrame = tk.Frame(window)
	findFrame.pack(fill=tk.BOTH,expand=True)
	style = ttk.Style()
	style.theme_create( "notebook", parent="alt", settings={
	        "TNotebook.Tab": {
	            "configure": { "background": "white" },
	            "map":       {"background": [("selected", "blue" ),("","white")],
	            			  "foreground": [("selected", "white"),("","black")]} } } )

	style.theme_use("notebook")
	findNotebook = ttk.Notebook(findFrame)
	x = info(findNotebook)
	x.pack(fill=tk.BOTH,expand=True)
	x.build_for_compound(compound="H2O",bg="white",fg="black",font=("arial",20)) 
	v = info(findNotebook)
	v.pack(fill=tk.BOTH,expand=True)
	v.build_for_compound(compound="H2",bg="white",fg="black",font=("arial",20))
	#findNotebook.add(x, text="Properties")
	#findNotebook.add(v, text="Discovered By")
	#findNotebook.add(v, text="Composition")
	findNotebook.pack(fill=tk.BOTH,expand=True)
	window.mainloop()

#test()