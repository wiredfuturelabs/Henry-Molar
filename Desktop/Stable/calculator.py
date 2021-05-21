import tkinter as tk
from tkinter import ttk
from tkinterplus import rgb,CodeEditor
from molmass import Formula
import tkinterplus as ttx
from tkinter import messagebox
import webbrowser

def startcalculate(master,current,reinsert,icon,data,data2):

	bg = ttx.rgb(23,27,33)
	fg = "white"


	current.destroy()
	def process(event):
		_exist_ = False

		text = str(formula.get())
		output.clear()

		for element in data:
			if text == element["Symbol"] or text.capitalize() == element["Element"]:
				_exist_ = True
				for _each_ in data2:
					if _each_["symbol"] == element["Symbol"]:
						each = _each_
				element_data = f"""
Atomic Number: {each["atomic_number"]}
Element Name: {each["name"]}
Symbol: {element["Symbol"]}
Group: {element["Group"]}
Period: {element["Period"]}
Atomic Mass: {each["atomic_weight"]}
Density: {each["density"]}
Category: {element["Category"]}
Group Name: {element["Group Name"]}
Electronic Configuration: {each["econf"]}
Melting Point: {each["melting_point"]}
Boiling Point: {each["boiling_point"]}
Block: {each["block"]}
First Ionization Energy: {element["First Ionization Energy"]}
Second Ionization Energy: {element["Second Ionization energy"]}
Third Ionization Energy: {element["Third Ionization Energy"]}
Isotopes: {element["Isotopes"]}
Electrongativity: {each["en_pauling"]}
Electronpositivity: {element["Electronpositivity"]}
Electron Affinity: {each["electron_affinity"]}
Vander waals radius: {each["vdw_radius"]}
Atomic Radius: {each["atomic_radius"]}
Atomic Volume: {each["atomic_volume"]}
Oxistates: {each["oxistates"]}
Abundance Crust: {each["abundance_crust"]}
Lattice Constant: {each["lattice_constant"]}
"""
		try:
			output.insert(1.0,element_data)
		except:
			pass
		if _exist_ == False:

			try:
				output.insert("1.0",f"""
Formula: {Formula(text).formula}
Empirical Formula: {Formula(text).empirical}


Mass:            {Formula(text).mass}
Mass of Isotope: {Formula(text).isotope.mass}
Isotope Mass Number: {Formula(text).isotope.massnumber}

Atoms: {Formula(text).atoms}

{Formula(text).spectrum()}""")
			except:
				messagebox.showerror("Error","Please enter a valid compound formula.")
				formula.focus_set()

		
	window = tk.Frame(master)
	window.pack(fill=tk.BOTH,expand=1)
	window.config(bg=bg)


	for i in range(1,3):
		window.grid_rowconfigure(i,weight=1)
	for i in range(0,3):
		window.grid_columnconfigure(i,weight=1)

	backBut = tk.Label(window,image=icon,bg=bg,fg=fg,font=("avenir",20))
	backBut.grid(row=0,column=0,sticky=tk.W)
	def back(arg):
		window.destroy()
		reinsert()
	backBut.bind("<Button-1>",back)
	window.bind("<Escape>",back)
	def removedefault(arg=None):
		if str(formula.get()) == "Type compound formula...":
			formula.config(fg=fg)
			formula.delete(0,tk.END)
		else:
			pass

	

	formula = tk.Entry(window,relief="solid",bg=bg,fg="grey",insertbackground=fg,borderwidth=1,highlightcolor=fg,highlightbackground=fg,highlightthickness=1,font=("avenir",22))
	formula.grid(row=1,column=0,columnspan=2,padx=30,pady=(20,0),sticky=tk.W+tk.E+tk.N)
	formula.focus_set()
	formula.bind("<Escape>",back)
	formula.bind("<Return>",process)
	formula.insert("0","Type compound formula...")
	formula.bind("<Button-1>",removedefault)
	formula.bind("<Key>",removedefault)
	formula.icursor(0)

	def search(website,query=formula.get):
		arg = query()
		if website == "pubchem":
			if arg == "Type compound formula..." or arg == "":
				website_base = "https://pubchem.ncbi.nlm.nih.gov"
			else:
				website_base = "https://pubchem.ncbi.nlm.nih.gov/#query="+str(arg.replace(" ","%20"))
			webbrowser.open(website_base)
		elif website == "google":
			if arg == "Type compound formula..." or arg == "":
				website_base = "https://www.google.com"
			else:
				website_base = "https://www.google.com/search?q="+str(arg.replace(" ","+"))
			webbrowser.open(website_base)
		elif website == "chemspider":
			if arg == "Type compound formula..." or arg == "":
				website_base = "https://www.chemspider.com"
			else:
				website_base = "https://www.chemspider.com/Search.aspx?q="+str(arg.replace(" ","%20"))
			webbrowser.open(website_base)
			

	def popup(e):
		menu.tk_popup(e.x_root,e.y_root)

	menu = tk.Menu(window,tearoff=False)
	menu.add_command(label="Search with pubchem",command=lambda : search(website="pubchem"))
	menu.add_command(label="Search with google",command=lambda : search(website="google"))
	menu.add_command(label="Search with chemspider",command=lambda : search(website="chemspider"))


	calculate = tk.Label(window,text="Find",bg=rgb(32,140,255),fg=fg,pady=7)
	calculate.grid(row=1,column=2,sticky=tk.W+tk.E+tk.N,pady=(20,0),padx=(30,30))
	calculate.bind("<Button-1>",process)
	calculate.bind("<Enter>",lambda event: calculate.config(bg=rgb(11, 92, 179)))
	calculate.bind("<Leave>",lambda event: calculate.config(bg=rgb(32,140,255)))
	calculate.bind("<Button-2>",popup)
	calculate.bind("<Button-3>",popup)

	output = CodeEditor(window,height=20,width=60,bg=bg,fg=fg,insertbackground=fg,relief="solid",borderwidth=2,wrap='word',highlightcolor=fg,highlightbackground=fg,highlightthickness=1,font=("avenir",14))
	output.grid(row=2,column=0,columnspan=3,pady=(10,40),padx=(30,30),sticky=tk.W+tk.E+tk.N+tk.S)
	output.bind("<Escape>",back)


