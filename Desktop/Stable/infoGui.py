from termcolor import colored
import tkinter as tk
from tkinter import ttk
from tkinterplus import div
from PIL import ImageTk,Image
import os
import tkinterplus as ttx
from image import images_icon
import base64
from urllib.request import urlopen
from io import BytesIO

def InfoWindow(event,data,images,data2,icon):

	bg = ttx.rgb(23,27,33)
	fg = "white"
	imgc = icon
	def imagedata(arg):
		base_url = ["https://www.rsc-cdn.org/www.rsc.org/periodic-table/content/Images/Elements/",arg,"-L.jpg?6.2.65"]
		try:
			image_byt = urlopen(''.join(base_url)).read()
			imageproc = base64.encodebytes(image_byt)
			imageproc = Image.open(BytesIO(base64.b64decode(imageproc)))
			imageproc = imageproc.resize((200,200), Image.ANTIALIAS)
		except:
			print(colored("Internet connection not available [MODERATE]","yellow"))
			imageproc = Image.open(BytesIO(base64.b64decode(images_icon["internet"])))
			imageproc = imageproc.resize((350,200), Image.ANTIALIAS)
		return imageproc

	global img
	img = ""
	def imageprocess(arg):
		global img
		img = Image.open(BytesIO(base64.b64decode(arg)))
		img = img.resize((330,200), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		return img


	#initialize requirements

	levelInfo = tk.Toplevel()


	for da in data2:
		if da["symbol"] == data["Symbol"]:
			e = da

	if e["boiling_point"] == None: e["boiling_point"] = "Unknown"
	if e["melting_point"] == None: e["melting_point"] = "Unknown"
	for key,value in data.items():
		if value == "":
			data[key] = "Unknown"
	if e["en_pauling"] == None: e["en_pauling"] = "Unknown"
	if e["electron_affinity"] == None: e["electron_affinity"] = "Unknown"
	if e["density"] == None: e["density"] = "Unknown"
	if e["vdw_radius"] == None: e["vdw_radius"] = "Unknown"
	if e["oxistates"] == None: e["oxistates"] = "Unknown"
	if e["lattice_constant"] == None: e["lattice_constant"] = "Unknown"
	if e["atomic_volume"] == None: e["atomic_volume"] = "Unknown"
	if e["atomic_radius"] == None: e["atomic_radius"] = "Unknown"
	if e["abundance_crust"] == None: e["abundance_crust"] = "Unknown"

	labels = ["Symbol","Element Name","Atomic Number","Atomic Mass",
	"Density (g cm^-3)","Category","Group","Period","Group Name",
	"Block","Electronic Configuration","Melting Point","Boiling Point",
	"Electronegativity (eV)","Electron Affinity(eV)","First Ionization Energy (eV)",
	"Second Ionization Energy (eV)","Third Ionization Energy (eV)","Vanderwaals Radius (pm)",
	"Atomic Radius (pm)","Atomic Volume (cm3/mol)","Oxidation states","Abundance (Crust) (mg/kg)",
	"Lattice Constant (Angstrom)"]


	dataLabel = [e["symbol"],e["name"],e["atomic_number"],e["atomic_weight"],
	e["density"],data["Category"],data["Group"],e["period"],data["Group Name"],
	e["block"],e["econf"],str(e["melting_point"])+'K',
	str(e["boiling_point"])+'K',e["en_pauling"],e["electron_affinity"],data["First Ionization Energy"],
	data["Second Ionization energy"],data["Third Ionization Energy"],e["vdw_radius"],e["atomic_radius"],
	e["atomic_volume"],e["oxistates"],e["abundance_crust"],e["lattice_constant"]]
	

	levelInfo.config(bg=bg)
	levelInfo.title(dataLabel[1])


	for i in range(0,2):
		levelInfo.grid_rowconfigure(i,weight=1)
	for i in range(0,4):
		levelInfo.grid_columnconfigure(i,weight=1)

	image_label = tk.Label(levelInfo,image=imageprocess(images_icon["loading"]))
	image_label.grid(row=1,column=0,columnspan=3,pady=20,padx=20)

	global image
	image = ""
	def renderimage():
		global image
		image = ImageTk.PhotoImage(imagedata(images))
		return image

	style = ttk.Style()
	# this is set background and foreground of the treeview
	style.configure("Treeview",
	                background=bg,
	                foreground=fg,
	                rowheight=25,
	                fieldbackground=bg)

	# set backgound and foreground color when selected
	style.map('Treeview', background=[('selected', fg)], foreground=[('selected', bg)])

	table = ttk.Treeview(levelInfo,selectmode='browse',height=16)
	table.grid(row=2,column=0,columnspan=3,padx=(20,20),pady=(20,20),sticky=tk.W+tk.E)

	vsb = ttk.Scrollbar(levelInfo, orient="vertical", command=table.yview)
	vsb.grid(row=2,column=2,sticky=tk.N+tk.S+tk.E)

	table.configure(yscrollcommand=vsb.set)

	#defining columns
	table['columns'] = ("value")

	#format our columns
	table.column("#0",width=175,minwidth=50)
	table.column("value",anchor=tk.E,width=175,minwidth=50)
	y = 0
	for label in labels:
		table.insert(parent='',index='end',iid=label,text=label,values=(str(dataLabel[y]),))
		y+=1
	levelInfo.resizable(False,False)
	levelInfo.after(5,lambda: image_label.config(image=renderimage()))
	return levelInfo