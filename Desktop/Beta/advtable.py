import tkinter as tk
import tkinterplus as ttx
from tkinter import messagebox



def showinfo(arg):
	messagebox.showinfo("Element",arg)



font = "avenir"

def panel(base,current,reinsert,secwindow):
	current.destroy()
	
	advwindow = tk.Canvas(base,borderwidth=0)
	bg = ttx.rgb(23,27,33)


	advwindow.config(bg=bg)
	base.config(bg=bg)
	advwindow.pack(fill=tk.BOTH,expand=True)

	#border spaces
	tk.Label(advwindow,bg=bg).grid(row=0,column=0,padx=5,pady=5)

	global hiding
	hiding = False

	def hide_show(arg=None):
		global hiding
		if hiding == False:
			eye.config(text="􀋮")
			secwindow.pack_forget()
			base.update()
			hiding = True

		elif hiding == True:
			eye.config(text="􀋰")
			secwindow.pack(side=tk.RIGHT,fill=tk.BOTH)
			base.update()
			hiding = False


	eye = tk.Label(advwindow,text="􀋰",bg=bg,fg="white")
	eye.grid(row=0,column=19,padx=5,pady=5)
	eye.bind("<Button-1>",hide_show)
	
	tk.Label(advwindow,bg=bg).grid(row=8,column=12,padx=5,pady=5)
	tk.Label(advwindow,bg=bg).grid(row=11,column=12,padx=5,pady=5)

	for i in range(0,12):
		advwindow.grid_rowconfigure(i,weight=1)
	for i in range(0,20):
		advwindow.grid_columnconfigure(i,weight=1)


	hydrogen = ttx.Labelv(advwindow,text="H",bg="#EBBFD8",height=3,width=5)
	hydrogen.grid(row=1,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	hydrogen.bind("<Button-2>",lambda event: showinfo("Hydrogen"))
	hydrogen.putvalue("Hydrogen")
	ttx.Drag(hydrogen)


	helium = ttx.Labelv(advwindow,text="He",bg="#EADA24",height=3,width=5)
	helium.grid(row=1,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	helium.bind("<Button-2>",lambda event: showinfo("Helium"))
	helium.putvalue("Helium")
	ttx.Drag(helium)


	lithium = ttx.Labelv(advwindow,text="Li",bg="#EBBFD8",height=3,width=5)
	lithium.grid(row=2,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	lithium.bind("<Button-2>",lambda event: showinfo("Lithium"))
	lithium.putvalue("Lithium")
	ttx.Drag(lithium)


	beryllium = ttx.Labelv(advwindow,text="Be",bg="#FBC9E5",height=3,width=5)
	beryllium.grid(row=2,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	beryllium.bind("<Button-2>",lambda event: showinfo("Beryllium"))
	beryllium.putvalue("Beryllium")
	ttx.Drag(beryllium)


	boron = ttx.Labelv(advwindow,text="B",bg="#CEDC00",height=3,width=5)
	boron.grid(row=2,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	boron.bind("<Button-2>",lambda event: showinfo("Boron"))
	boron.putvalue("Boron")
	ttx.Drag(boron)


	carbon = ttx.Labelv(advwindow,text="C",bg="#D1A2CB",height=3,width=5)
	carbon.grid(row=2,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	carbon.bind("<Button-2>",lambda event: showinfo("Carbon"))
	carbon.putvalue("Carbon")
	ttx.Drag(carbon)


	nitrogen = ttx.Labelv(advwindow,text="N",bg="#00D600",height=3,width=5)
	nitrogen.grid(row=2,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	nitrogen.bind("<Button-2>",lambda event: showinfo("Nitrogen"))
	nitrogen.putvalue("Nitrogen")
	ttx.Drag(nitrogen)


	oxygen = ttx.Labelv(advwindow,text="O",bg="#F0B323",height=3,width=5)
	oxygen.grid(row=2,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	oxygen.bind("<Button-2>",lambda event: showinfo("Oxygen"))
	oxygen.putvalue("Oxygen")
	ttx.Drag(oxygen)


	fluorine = ttx.Labelv(advwindow,text="F",bg="#EAB37F",height=3,width=5)
	fluorine.grid(row=2,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	fluorine.bind("<Button-2>",lambda event: showinfo("Fluorine"))
	fluorine.putvalue("Fluorine")
	ttx.Drag(fluorine)


	neon = ttx.Labelv(advwindow,text="Ne",bg="#EADA24",height=3,width=5)
	neon.grid(row=2,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	neon.bind("<Button-2>",lambda event: showinfo("Neon"))
	neon.putvalue("Neon")
	ttx.Drag(neon)


	sodium = ttx.Labelv(advwindow,text="Na",bg="#EBBFD8",height=3,width=5)
	sodium.grid(row=3,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	sodium.bind("<Button-2>",lambda event: showinfo("Sodium"))
	sodium.putvalue("Sodium")
	ttx.Drag(sodium)


	magnesium = ttx.Labelv(advwindow,text="Mg",bg="#FBC9E5",height=3,width=5)
	magnesium.grid(row=3,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	magnesium.bind("<Button-2>",lambda event: showinfo("Magnesium"))
	magnesium.putvalue("Magnesium")
	ttx.Drag(magnesium)


	aluminium = ttx.Labelv(advwindow,text="Al",bg="#CEDC00",height=3,width=5)
	aluminium.grid(row=3,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	aluminium.bind("<Button-2>",lambda event: showinfo("Aluminium"))
	aluminium.putvalue("Aluminium")
	ttx.Drag(aluminium)


	silicon = ttx.Labelv(advwindow,text="Si",bg="#D1A2CB",height=3,width=5)
	silicon.grid(row=3,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	silicon.bind("<Button-2>",lambda event: showinfo("Silicon"))
	silicon.putvalue("Silicon")
	ttx.Drag(silicon)


	phosphorus = ttx.Labelv(advwindow,text="P",bg="#00D600",height=3,width=5)
	phosphorus.grid(row=3,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	phosphorus.bind("<Button-2>",lambda event: showinfo("Phosphorus"))
	phosphorus.putvalue("Phosphorus")
	ttx.Drag(phosphorus)


	sulfur = ttx.Labelv(advwindow,text="S",bg="#F0B323",height=3,width=5)
	sulfur.grid(row=3,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	sulfur.bind("<Button-2>",lambda event: showinfo("Sulfur"))
	sulfur.putvalue("Sulfur")
	ttx.Drag(sulfur)


	chlorine = ttx.Labelv(advwindow,text="Cl",bg="#EAB37F",height=3,width=5)
	chlorine.grid(row=3,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	chlorine.bind("<Button-2>",lambda event: showinfo("Chlorine"))
	chlorine.putvalue("Chlorine")
	ttx.Drag(chlorine)


	argon = ttx.Labelv(advwindow,text="Ar",bg="#EADA24",height=3,width=5)
	argon.grid(row=3,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	argon.bind("<Button-2>",lambda event: showinfo("Argon"))
	argon.putvalue("Argon")
	ttx.Drag(argon)


	potassium = ttx.Labelv(advwindow,text="K",bg="#EBBFD8",height=3,width=5)
	potassium.grid(row=4,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	potassium.bind("<Button-2>",lambda event: showinfo("Potassium"))
	potassium.putvalue("Potassium")
	ttx.Drag(potassium)


	calcium = ttx.Labelv(advwindow,text="Ca",bg="#FBC9E5",height=3,width=5)
	calcium.grid(row=4,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	calcium.bind("<Button-2>",lambda event: showinfo("Calcium"))
	calcium.putvalue("Calcium")
	ttx.Drag(calcium)


	scandium = ttx.Labelv(advwindow,text="Sc",bg="#5BC2E7",height=3,width=5)
	scandium.grid(row=4,column=3,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	scandium.bind("<Button-2>",lambda event: showinfo("Scandium"))
	scandium.putvalue("Scandium")
	ttx.Drag(scandium)


	titanium = ttx.Labelv(advwindow,text="Ti",bg="#5BC2E7",height=3,width=5)
	titanium.grid(row=4,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	titanium.bind("<Button-2>",lambda event: showinfo("Titanium"))
	titanium.putvalue("Titanium")
	ttx.Drag(titanium)


	vanadium = ttx.Labelv(advwindow,text="V",bg="#5BC2E7",height=3,width=5)
	vanadium.grid(row=4,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	vanadium.bind("<Button-2>",lambda event: showinfo("Vanadium"))
	vanadium.putvalue("Vanadium")
	ttx.Drag(vanadium)


	chromium = ttx.Labelv(advwindow,text="Cr",bg="#5BC2E7",height=3,width=5)
	chromium.grid(row=4,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	chromium.bind("<Button-2>",lambda event: showinfo("Chromium"))
	chromium.putvalue("Chromium")
	ttx.Drag(chromium)


	manganese = ttx.Labelv(advwindow,text="Mn",bg="#5BC2E7",height=3,width=5)
	manganese.grid(row=4,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	manganese.bind("<Button-2>",lambda event: showinfo("Manganese"))
	manganese.putvalue("Manganese")
	ttx.Drag(manganese)


	iron = ttx.Labelv(advwindow,text="Fe",bg="#5BC2E7",height=3,width=5)
	iron.grid(row=4,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	iron.bind("<Button-2>",lambda event: showinfo("Iron"))
	iron.putvalue("Iron")
	ttx.Drag(iron)


	cobalt = ttx.Labelv(advwindow,text="Co",bg="#5BC2E7",height=3,width=5)
	cobalt.grid(row=4,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	cobalt.bind("<Button-2>",lambda event: showinfo("Cobalt"))
	cobalt.putvalue("Cobalt")
	ttx.Drag(cobalt)


	nickel = ttx.Labelv(advwindow,text="Ni",bg="#5BC2E7",height=3,width=5)
	nickel.grid(row=4,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	nickel.bind("<Button-2>",lambda event: showinfo("Nickel"))
	nickel.putvalue("Nickel")
	ttx.Drag(nickel)


	copper = ttx.Labelv(advwindow,text="Cu",bg="#5BC2E7",height=3,width=5)
	copper.grid(row=4,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	copper.bind("<Button-2>",lambda event: showinfo("Copper"))
	copper.putvalue("Copper")
	ttx.Drag(copper)


	zinc = ttx.Labelv(advwindow,text="Zn",bg="#5BC2E7",height=3,width=5)
	zinc.grid(row=4,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	zinc.bind("<Button-2>",lambda event: showinfo("Zinc"))
	zinc.putvalue("Zinc")
	ttx.Drag(zinc)


	gallium = ttx.Labelv(advwindow,text="Ga",bg="#CEDC00",height=3,width=5)
	gallium.grid(row=4,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	gallium.bind("<Button-2>",lambda event: showinfo("Gallium"))
	gallium.putvalue("Gallium")
	ttx.Drag(gallium)


	germanium = ttx.Labelv(advwindow,text="Ge",bg="#D1A2CB",height=3,width=5)
	germanium.grid(row=4,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	germanium.bind("<Button-2>",lambda event: showinfo("Germanium"))
	germanium.putvalue("Germanium")
	ttx.Drag(germanium)


	arsenic = ttx.Labelv(advwindow,text="As",bg="#00D600",height=3,width=5)
	arsenic.grid(row=4,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	arsenic.bind("<Button-2>",lambda event: showinfo("Arsenic"))
	arsenic.putvalue("Arsenic")
	ttx.Drag(arsenic)


	selenium = ttx.Labelv(advwindow,text="Se",bg="#F0B323",height=3,width=5)
	selenium.grid(row=4,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	selenium.bind("<Button-2>",lambda event: showinfo("Selenium"))
	selenium.putvalue("Selenium")
	ttx.Drag(selenium)


	bromine = ttx.Labelv(advwindow,text="Br",bg="#EAB37F",height=3,width=5)
	bromine.grid(row=4,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	bromine.bind("<Button-2>",lambda event: showinfo("Bromine"))
	bromine.putvalue("Bromine")
	ttx.Drag(bromine)


	krypton = ttx.Labelv(advwindow,text="Kr",bg="#EADA24",height=3,width=5)
	krypton.grid(row=4,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	krypton.bind("<Button-2>",lambda event: showinfo("Krypton"))
	krypton.putvalue("Krypton")
	ttx.Drag(krypton)


	rubidium = ttx.Labelv(advwindow,text="Rb",bg="#EBBFD8",height=3,width=5)
	rubidium.grid(row=5,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	rubidium.bind("<Button-2>",lambda event: showinfo("Rubidium"))
	rubidium.putvalue("Rubidium")
	ttx.Drag(rubidium)


	strontium = ttx.Labelv(advwindow,text="Sr",bg="#FBC9E5",height=3,width=5)
	strontium.grid(row=5,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	strontium.bind("<Button-2>",lambda event: showinfo("Strontium"))
	strontium.putvalue("Strontium")
	ttx.Drag(strontium)


	yttrium = ttx.Labelv(advwindow,text="Y",bg="#5BC2E7",height=3,width=5)
	yttrium.grid(row=5,column=3,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	yttrium.bind("<Button-2>",lambda event: showinfo("Yttrium"))
	yttrium.putvalue("Yttrium")
	ttx.Drag(yttrium)


	zirconium = ttx.Labelv(advwindow,text="Zr",bg="#5BC2E7",height=3,width=5)
	zirconium.grid(row=5,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	zirconium.bind("<Button-2>",lambda event: showinfo("Zirconium"))
	zirconium.putvalue("Zirconium")
	ttx.Drag(zirconium)


	niobium = ttx.Labelv(advwindow,text="Nb",bg="#5BC2E7",height=3,width=5)
	niobium.grid(row=5,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	niobium.bind("<Button-2>",lambda event: showinfo("Niobium"))
	niobium.putvalue("Niobium")
	ttx.Drag(niobium)


	molybdenum = ttx.Labelv(advwindow,text="Mo",bg="#5BC2E7",height=3,width=5)
	molybdenum.grid(row=5,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	molybdenum.bind("<Button-2>",lambda event: showinfo("Molybdenum"))
	molybdenum.putvalue("Molybdenum")
	ttx.Drag(molybdenum)


	technetium = ttx.Labelv(advwindow,text="Tc",bg="#5BC2E7",height=3,width=5)
	technetium.grid(row=5,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	technetium.bind("<Button-2>",lambda event: showinfo("Technetium"))
	technetium.putvalue("Technetium")
	ttx.Drag(technetium)


	ruthenium = ttx.Labelv(advwindow,text="Ru",bg="#5BC2E7",height=3,width=5)
	ruthenium.grid(row=5,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	ruthenium.bind("<Button-2>",lambda event: showinfo("Ruthenium"))
	ruthenium.putvalue("Ruthenium")
	ttx.Drag(ruthenium)


	rhodium = ttx.Labelv(advwindow,text="Rh",bg="#5BC2E7",height=3,width=5)
	rhodium.grid(row=5,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	rhodium.bind("<Button-2>",lambda event: showinfo("Rhodium"))
	rhodium.putvalue("Rhodium")
	ttx.Drag(rhodium)


	palladium = ttx.Labelv(advwindow,text="Pd",bg="#5BC2E7",height=3,width=5)
	palladium.grid(row=5,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	palladium.bind("<Button-2>",lambda event: showinfo("Palladium"))
	palladium.putvalue("Palladium")
	ttx.Drag(palladium)


	silver = ttx.Labelv(advwindow,text="Ag",bg="#5BC2E7",height=3,width=5)
	silver.grid(row=5,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	silver.bind("<Button-2>",lambda event: showinfo("Silver"))
	silver.putvalue("Silver")
	ttx.Drag(silver)


	cadmium = ttx.Labelv(advwindow,text="Cd",bg="#5BC2E7",height=3,width=5)
	cadmium.grid(row=5,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	cadmium.bind("<Button-2>",lambda event: showinfo("Cadmium"))
	cadmium.putvalue("Cadmium")
	ttx.Drag(cadmium)


	indium = ttx.Labelv(advwindow,text="In",bg="#CEDC00",height=3,width=5)
	indium.grid(row=5,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	indium.bind("<Button-2>",lambda event: showinfo("Indium"))
	indium.putvalue("Indium")
	ttx.Drag(indium)


	tin = ttx.Labelv(advwindow,text="Sn",bg="#D1A2CB",height=3,width=5)
	tin.grid(row=5,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	tin.bind("<Button-2>",lambda event: showinfo("Tin"))
	tin.putvalue("Tin")
	ttx.Drag(tin)


	antimony = ttx.Labelv(advwindow,text="Sb",bg="#00D600",height=3,width=5)
	antimony.grid(row=5,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	antimony.bind("<Button-2>",lambda event: showinfo("Antimony"))
	antimony.putvalue("Antimony")
	ttx.Drag(antimony)


	tellurium = ttx.Labelv(advwindow,text="Te",bg="#F0B323",height=3,width=5)
	tellurium.grid(row=5,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	tellurium.bind("<Button-2>",lambda event: showinfo("Tellurium"))
	tellurium.putvalue("Tellurium")
	ttx.Drag(tellurium)


	iodine = ttx.Labelv(advwindow,text="I",bg="#EAB37F",height=3,width=5)
	iodine.grid(row=5,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	iodine.bind("<Button-2>",lambda event: showinfo("Iodine"))
	iodine.putvalue("Iodine")
	ttx.Drag(iodine)


	xenon = ttx.Labelv(advwindow,text="Xe",bg="#EADA24",height=3,width=5)
	xenon.grid(row=5,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	xenon.bind("<Button-2>",lambda event: showinfo("Xenon"))
	xenon.putvalue("Xenon")
	ttx.Drag(xenon)


	cesium = ttx.Labelv(advwindow,text="Cs",bg="#EBBFD8",height=3,width=5)
	cesium.grid(row=6,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	cesium.bind("<Button-2>",lambda event: showinfo("Cesium"))
	cesium.putvalue("Cesium")
	ttx.Drag(cesium)


	barium = ttx.Labelv(advwindow,text="Ba",bg="#FBC9E5",height=3,width=5)
	barium.grid(row=6,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	barium.bind("<Button-2>",lambda event: showinfo("Barium"))
	barium.putvalue("Barium")
	ttx.Drag(barium)


	lanthanum = ttx.Labelv(advwindow,text="La",bg="#BFEAEC",height=3,width=5)
	lanthanum.grid(row=9,column=3,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	lanthanum.bind("<Button-2>",lambda event: showinfo("Lanthanum"))
	lanthanum.putvalue("Lanthanum")
	ttx.Drag(lanthanum)
		

	cerium = ttx.Labelv(advwindow,text="Ce",bg="#BFEAEC",height=3,width=5)
	cerium.grid(row=9,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	cerium.bind("<Button-2>",lambda event: showinfo("Cerium"))
	cerium.putvalue("Cerium")
	ttx.Drag(cerium)
		

	praseodymium = ttx.Labelv(advwindow,text="Pr",bg="#BFEAEC",height=3,width=5)
	praseodymium.grid(row=9,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	praseodymium.bind("<Button-2>",lambda event: showinfo("Praseodymium"))
	praseodymium.putvalue("Praseodymium")
	ttx.Drag(praseodymium)
		

	neodymium = ttx.Labelv(advwindow,text="Nd",bg="#BFEAEC",height=3,width=5)
	neodymium.grid(row=9,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	neodymium.bind("<Button-2>",lambda event: showinfo("Neodymium"))
	neodymium.putvalue("Neodymium")
	ttx.Drag(neodymium)
		

	promethium = ttx.Labelv(advwindow,text="Pm",bg="#BFEAEC",height=3,width=5)
	promethium.grid(row=9,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	promethium.bind("<Button-2>",lambda event: showinfo("Promethium"))
	promethium.putvalue("Promethium")
	ttx.Drag(promethium)
		

	samarium = ttx.Labelv(advwindow,text="Sm",bg="#BFEAEC",height=3,width=5)
	samarium.grid(row=9,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	samarium.bind("<Button-2>",lambda event: showinfo("Samarium"))
	samarium.putvalue("Samarium")
	ttx.Drag(samarium)
		

	europium = ttx.Labelv(advwindow,text="Eu",bg="#BFEAEC",height=3,width=5)
	europium.grid(row=9,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	europium.bind("<Button-2>",lambda event: showinfo("Europium"))
	europium.putvalue("Europium")
	ttx.Drag(europium)
		

	gadolinium = ttx.Labelv(advwindow,text="Gd",bg="#BFEAEC",height=3,width=5)
	gadolinium.grid(row=9,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	gadolinium.bind("<Button-2>",lambda event: showinfo("Gadolinium"))
	gadolinium.putvalue("Gadolinium")
	ttx.Drag(gadolinium)
		

	terbium = ttx.Labelv(advwindow,text="Tb",bg="#BFEAEC",height=3,width=5)
	terbium.grid(row=9,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	terbium.bind("<Button-2>",lambda event: showinfo("Terbium"))
	terbium.putvalue("Terbium")
	ttx.Drag(terbium)
		

	dysprosium = ttx.Labelv(advwindow,text="Dy",bg="#BFEAEC",height=3,width=5)
	dysprosium.grid(row=9,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	dysprosium.bind("<Button-2>",lambda event: showinfo("Dysprosium"))
	dysprosium.putvalue("Dysprosium")
	ttx.Drag(dysprosium)
		

	holmium = ttx.Labelv(advwindow,text="Ho",bg="#BFEAEC",height=3,width=5)
	holmium.grid(row=9,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	holmium.bind("<Button-2>",lambda event: showinfo("Holmium"))
	holmium.putvalue("Holmium")
	ttx.Drag(holmium)
		

	erbium = ttx.Labelv(advwindow,text="Er",bg="#BFEAEC",height=3,width=5)
	erbium.grid(row=9,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	erbium.bind("<Button-2>",lambda event: showinfo("Erbium"))
	erbium.putvalue("Erbium")
	ttx.Drag(erbium)
		

	thulium = ttx.Labelv(advwindow,text="Tm",bg="#BFEAEC",height=3,width=5)
	thulium.grid(row=9,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	thulium.bind("<Button-2>",lambda event: showinfo("Thulium"))
	thulium.putvalue("Thulium")
	ttx.Drag(thulium)
		

	ytterbium = ttx.Labelv(advwindow,text="Yb",bg="#BFEAEC",height=3,width=5)
	ytterbium.grid(row=9,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	ytterbium.bind("<Button-2>",lambda event: showinfo("Ytterbium"))
	ytterbium.putvalue("Ytterbium")
	ttx.Drag(ytterbium)
		

	lutetium = ttx.Labelv(advwindow,text="Lu",bg="#BFEAEC",height=3,width=5)
	lutetium.grid(row=9,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	lutetium.bind("<Button-2>",lambda event: showinfo("Lutetium"))
	lutetium.putvalue("Lutetium")
	ttx.Drag(lutetium)
		

	hafnium = ttx.Labelv(advwindow,text="Hf",bg="#5BC2E7",height=3,width=5)
	hafnium.grid(row=6,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	hafnium.bind("<Button-2>",lambda event: showinfo("Hafnium"))
	hafnium.putvalue("Hafnium")
	ttx.Drag(hafnium)


	tantalum = ttx.Labelv(advwindow,text="Ta",bg="#5BC2E7",height=3,width=5)
	tantalum.grid(row=6,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	tantalum.bind("<Button-2>",lambda event: showinfo("Tantalum"))
	tantalum.putvalue("Tantalum")
	ttx.Drag(tantalum)


	tungsten = ttx.Labelv(advwindow,text="W",bg="#5BC2E7",height=3,width=5)
	tungsten.grid(row=6,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	tungsten.bind("<Button-2>",lambda event: showinfo("Tungsten"))
	tungsten.putvalue("Tungsten")
	ttx.Drag(tungsten)


	rhenium = ttx.Labelv(advwindow,text="Re",bg="#5BC2E7",height=3,width=5)
	rhenium.grid(row=6,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	rhenium.bind("<Button-2>",lambda event: showinfo("Rhenium"))
	rhenium.putvalue("Rhenium")
	ttx.Drag(rhenium)


	osmium = ttx.Labelv(advwindow,text="Os",bg="#5BC2E7",height=3,width=5)
	osmium.grid(row=6,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	osmium.bind("<Button-2>",lambda event: showinfo("Osmium"))
	osmium.putvalue("Osmium")
	ttx.Drag(osmium)


	iridium = ttx.Labelv(advwindow,text="Ir",bg="#5BC2E7",height=3,width=5)
	iridium.grid(row=6,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	iridium.bind("<Button-2>",lambda event: showinfo("Iridium"))
	iridium.putvalue("Iridium")
	ttx.Drag(iridium)


	platinum = ttx.Labelv(advwindow,text="Pt",bg="#5BC2E7",height=3,width=5)
	platinum.grid(row=6,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	platinum.bind("<Button-2>",lambda event: showinfo("Platinum"))
	platinum.putvalue("Platinum")
	ttx.Drag(platinum)


	gold = ttx.Labelv(advwindow,text="Au",bg="#5BC2E7",height=3,width=5)
	gold.grid(row=6,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	gold.bind("<Button-2>",lambda event: showinfo("Gold"))
	gold.putvalue("Gold")
	ttx.Drag(gold)


	mercury = ttx.Labelv(advwindow,text="Ag",bg="#5BC2E7",height=3,width=5)
	mercury.grid(row=6,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	mercury.bind("<Button-2>",lambda event: showinfo("Mercury"))
	mercury.putvalue("Mercury")
	ttx.Drag(mercury)


	thallium = ttx.Labelv(advwindow,text="Tl",bg="#CEDC00",height=3,width=5)
	thallium.grid(row=6,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	thallium.bind("<Button-2>",lambda event: showinfo("Thallium"))
	thallium.putvalue("Thallium")
	ttx.Drag(thallium)


	lead = ttx.Labelv(advwindow,text="Pb",bg="#D1A2CB",height=3,width=5)
	lead.grid(row=6,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	lead.bind("<Button-2>",lambda event: showinfo("Lead"))
	lead.putvalue("Lead")
	ttx.Drag(lead)


	bismuth = ttx.Labelv(advwindow,text="Bi",bg="#00D600",height=3,width=5)
	bismuth.grid(row=6,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	bismuth.bind("<Button-2>",lambda event: showinfo("Bismuth"))
	bismuth.putvalue("Bismuth")
	ttx.Drag(bismuth)


	polonium = ttx.Labelv(advwindow,text="Po",bg="#F0B323",height=3,width=5)
	polonium.grid(row=6,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	polonium.bind("<Button-2>",lambda event: showinfo("Polonium"))
	polonium.putvalue("Polonium")
	ttx.Drag(polonium)


	astatine = ttx.Labelv(advwindow,text="At",bg="#EAB37F",height=3,width=5)
	astatine.grid(row=6,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	astatine.bind("<Button-2>",lambda event: showinfo("Astatine"))
	astatine.putvalue("Astatine")
	ttx.Drag(astatine)


	radon = ttx.Labelv(advwindow,text="Rn",bg="#EADA24",height=3,width=5)
	radon.grid(row=6,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	radon.bind("<Button-2>",lambda event: showinfo("Radon"))
	radon.putvalue("Radon")
	ttx.Drag(radon)


	francium = ttx.Labelv(advwindow,text="Fr",bg="#EBBFD8",height=3,width=5)
	francium.grid(row=7,column=1,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	francium.bind("<Button-2>",lambda event: showinfo("Francium"))
	francium.putvalue("Francium")
	ttx.Drag(francium)


	radium = ttx.Labelv(advwindow,text="Ra",bg="#FBC9E5",height=3,width=5)
	radium.grid(row=7,column=2,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	radium.bind("<Button-2>",lambda event: showinfo("Radium"))
	radium.putvalue("Radium")
	ttx.Drag(radium)


	actinium = ttx.Labelv(advwindow,text="Ac",bg="#A2D34D",height=3,width=5)
	actinium.grid(row=10,column=3,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	actinium.bind("<Button-2>",lambda event: showinfo("Actinium"))
	actinium.putvalue("Actinium")
	ttx.Drag(actinium)


	thorium = ttx.Labelv(advwindow,text="Th",bg="#A2D34D",height=3,width=5)
	thorium.grid(row=10,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	thorium.bind("<Button-2>",lambda event: showinfo("Thorium"))
	thorium.putvalue("Thorium")
	ttx.Drag(thorium)


	protactinium = ttx.Labelv(advwindow,text="Pa",bg="#A2D34D",height=3,width=5)
	protactinium.grid(row=10,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	protactinium.bind("<Button-2>",lambda event: showinfo("Protactinium"))
	protactinium.putvalue("Protactinium")
	ttx.Drag(protactinium)


	uranium = ttx.Labelv(advwindow,text="U",bg="#A2D34D",height=3,width=5)
	uranium.grid(row=10,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	uranium.bind("<Button-2>",lambda event: showinfo("Uranium"))
	uranium.putvalue("Uranium")
	ttx.Drag(uranium)


	neptunium = ttx.Labelv(advwindow,text="Np",bg="#A2D34D",height=3,width=5)
	neptunium.grid(row=10,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	neptunium.bind("<Button-2>",lambda event: showinfo("Neptunium"))
	neptunium.putvalue("Neptunium")
	ttx.Drag(neptunium)


	plutonium = ttx.Labelv(advwindow,text="Pu",bg="#A2D34D",height=3,width=5)
	plutonium.grid(row=10,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	plutonium.bind("<Button-2>",lambda event: showinfo("Plutonium"))
	plutonium.putvalue("Plutonium")
	ttx.Drag(plutonium)


	americium = ttx.Labelv(advwindow,text="Am",bg="#A2D34D",height=3,width=5)
	americium.grid(row=10,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	americium.bind("<Button-2>",lambda event: showinfo("Americium"))
	americium.putvalue("Americium")
	ttx.Drag(americium)


	curium = ttx.Labelv(advwindow,text="Cm",bg="#A2D34D",height=3,width=5)
	curium.grid(row=10,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	curium.bind("<Button-2>",lambda event: showinfo("Curium"))
	curium.putvalue("Curium")
	ttx.Drag(curium)


	berkelium = ttx.Labelv(advwindow,text="Bk",bg="#A2D34D",height=3,width=5)
	berkelium.grid(row=10,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	berkelium.bind("<Button-2>",lambda event: showinfo("Berkelium"))
	berkelium.putvalue("Berkelium")
	ttx.Drag(berkelium)


	californium = ttx.Labelv(advwindow,text="Cf",bg="#A2D34D",height=3,width=5)
	californium.grid(row=10,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	californium.bind("<Button-2>",lambda event: showinfo("Californium"))
	californium.putvalue("Californium")
	ttx.Drag(californium)


	einsteinium = ttx.Labelv(advwindow,text="Es",bg="#A2D34D",height=3,width=5)
	einsteinium.grid(row=10,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	einsteinium.bind("<Button-2>",lambda event: showinfo("Einsteinium"))
	einsteinium.putvalue("Einsteinium")
	ttx.Drag(einsteinium)


	fermium = ttx.Labelv(advwindow,text="Fm",bg="#A2D34D",height=3,width=5)
	fermium.grid(row=10,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	fermium.bind("<Button-2>",lambda event: showinfo("Fermium"))
	fermium.putvalue("Fermium")
	ttx.Drag(fermium)


	mendelevium = ttx.Labelv(advwindow,text="Md",bg="#A2D34D",height=3,width=5)
	mendelevium.grid(row=10,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	mendelevium.bind("<Button-2>",lambda event: showinfo("Mendelevium"))
	mendelevium.putvalue("Mendelevium")
	ttx.Drag(mendelevium)


	nobelium = ttx.Labelv(advwindow,text="No",bg="#A2D34D",height=3,width=5)
	nobelium.grid(row=10,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	nobelium.bind("<Button-2>",lambda event: showinfo("Nobelium"))
	nobelium.putvalue("Nobelium")
	ttx.Drag(nobelium)


	lawrencium = ttx.Labelv(advwindow,text="Lr",bg="#A2D34D",height=3,width=5)
	lawrencium.grid(row=10,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	lawrencium.bind("<Button-2>",lambda event: showinfo("Lawrencium"))
	lawrencium.putvalue("Lawrencium")
	ttx.Drag(lawrencium)


	rutherfordium = ttx.Labelv(advwindow,text="Rf",bg="#5BC2E7",height=3,width=5)
	rutherfordium.grid(row=7,column=4,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	rutherfordium.bind("<Button-2>",lambda event: showinfo("Rutherfordium"))
	rutherfordium.putvalue("Rutherfordium")
	ttx.Drag(rutherfordium)


	dubnium = ttx.Labelv(advwindow,text="Db",bg="#5BC2E7",height=3,width=5)
	dubnium.grid(row=7,column=5,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	dubnium.bind("<Button-2>",lambda event: showinfo("Dubnium"))
	dubnium.putvalue("Dubnium")
	ttx.Drag(dubnium)


	seaborgium = ttx.Labelv(advwindow,text="Sg",bg="#5BC2E7",height=3,width=5)
	seaborgium.grid(row=7,column=6,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	seaborgium.bind("<Button-2>",lambda event: showinfo("Seaborgium"))
	seaborgium.putvalue("Seaborgium")
	ttx.Drag(seaborgium)


	bohrium = ttx.Labelv(advwindow,text="Bh",bg="#5BC2E7",height=3,width=5)
	bohrium.grid(row=7,column=7,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	bohrium.bind("<Button-2>",lambda event: showinfo("Bohrium"))
	bohrium.putvalue("Bohrium")
	ttx.Drag(bohrium)


	hassium = ttx.Labelv(advwindow,text="Hs",bg="#5BC2E7",height=3,width=5)
	hassium.grid(row=7,column=8,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	hassium.bind("<Button-2>",lambda event: showinfo("Hassium"))
	hassium.putvalue("Hassium")
	ttx.Drag(hassium)


	meitnerium = ttx.Labelv(advwindow,text="Mt",bg="#5BC2E7",height=3,width=5)
	meitnerium.grid(row=7,column=9,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	meitnerium.bind("<Button-2>",lambda event: showinfo("Meitnerium"))
	meitnerium.putvalue("Meitnerium")
	ttx.Drag(meitnerium)


	darmstadtium = ttx.Labelv(advwindow,text="Ds",bg="#5BC2E7",height=3,width=5)
	darmstadtium.grid(row=7,column=10,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	darmstadtium.bind("<Button-2>",lambda event: showinfo("Darmstadtium"))
	darmstadtium.putvalue("Darmstadtium")
	ttx.Drag(darmstadtium)


	roentgenium = ttx.Labelv(advwindow,text="Rg",bg="#5BC2E7",height=3,width=5)
	roentgenium.grid(row=7,column=11,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	roentgenium.bind("<Button-2>",lambda event: showinfo("Roentgenium"))
	roentgenium.putvalue("Roentgenium")
	ttx.Drag(roentgenium)


	copernicium = ttx.Labelv(advwindow,text="Cn",bg="#5BC2E7",height=3,width=5)
	copernicium.grid(row=7,column=12,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	copernicium.bind("<Button-2>",lambda event: showinfo("Copernicium"))
	copernicium.putvalue("Copernicium")
	ttx.Drag(copernicium)


	nihonium = ttx.Labelv(advwindow,text="Nh",bg="#CEDC00",height=3,width=5)
	nihonium.grid(row=7,column=13,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	nihonium.bind("<Button-2>",lambda event: showinfo("Nihonium"))
	nihonium.putvalue("Nihonium")
	ttx.Drag(nihonium)


	flerovium = ttx.Labelv(advwindow,text="Fl",bg="#D1A2CB",height=3,width=5)
	flerovium.grid(row=7,column=14,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	flerovium.bind("<Button-2>",lambda event: showinfo("Flerovium"))
	flerovium.putvalue("Flerovium")
	ttx.Drag(flerovium)


	moscovium = ttx.Labelv(advwindow,text="Mc",bg="#00D600",height=3,width=5)
	moscovium.grid(row=7,column=15,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	moscovium.bind("<Button-2>",lambda event: showinfo("Moscovium"))
	moscovium.putvalue("Moscovium")
	ttx.Drag(moscovium)


	livermorium = ttx.Labelv(advwindow,text="Lv",bg="#F0B323",height=3,width=5)
	livermorium.grid(row=7,column=16,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	livermorium.bind("<Button-2>",lambda event: showinfo("Livermorium"))
	livermorium.putvalue("Livermorium")
	ttx.Drag(livermorium)


	tennessine = ttx.Labelv(advwindow,text="Ts",bg="#EAB37F",height=3,width=5)
	tennessine.grid(row=7,column=17,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	tennessine.bind("<Button-2>",lambda event: showinfo("Tennessine"))
	tennessine.putvalue("Tennessine")
	ttx.Drag(tennessine)


	oganesson = ttx.Labelv(advwindow,text="Og",bg="#EADA24",height=3,width=5)
	oganesson.grid(row=7,column=18,padx=2,pady=2,sticky=tk.N+tk.S+tk.E+tk.W)
	oganesson.bind("<Button-2>",lambda event: showinfo("Oganesson"))
	oganesson.putvalue("Oganesson")
	ttx.Drag(oganesson)

	buttons = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminium, silicon, phosphorus, sulfur, chlorine, argon, potassium, calcium, scandium, titanium, vanadium, chromium, manganese, iron, cobalt, nickel, copper, zinc, gallium, germanium, arsenic, selenium, bromine, krypton, rubidium, strontium, yttrium, zirconium, niobium, molybdenum, technetium, ruthenium, rhodium, palladium, silver, cadmium, indium, tin, antimony, tellurium, iodine, xenon, cesium, barium, lanthanum, cerium, praseodymium, neodymium, promethium, samarium, europium, gadolinium, terbium, dysprosium, holmium, erbium, thulium, ytterbium, lutetium, hafnium, tantalum, tungsten, rhenium, osmium, iridium, platinum, gold, mercury, thallium, lead, bismuth, polonium, astatine, radon, francium, radium, actinium, thorium, protactinium, uranium, neptunium, plutonium, americium, curium, berkelium, californium, einsteinium, fermium, mendelevium, nobelium, lawrencium, rutherfordium, dubnium, seaborgium, bohrium, hassium, meitnerium, darmstadtium, roentgenium, copernicium, nihonium, flerovium, moscovium, livermorium, tennessine, oganesson]
	return buttons,advwindow

