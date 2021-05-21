import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


def plot(datatoplot,window,data2,data):
	try:
		canvas.destroy()
	except:
		pass
	if datatoplot == "atomicmass":
		datatoplot = "Atomic Mass"
	elif datatoplot == "density":
		datatoplot = "Density"
	elif datatoplot == "bp":
		datatoplot = "Boiling Point"
	elif datatoplot == "mp":
		datatoplot = "Melting Point"
	else:
		print("Key Error: key must be [atomicmass,density,bp,mp]")
	if datatoplot == "Melting Point" or datatoplot == "Boiling Point" or datatoplot == "Density":
		if datatoplot == "Melting Point":
			y = []
			for i in data:
				for e in data2:
					if e["symbol"] == i["Symbol"]:
						y.append(e["melting_point"])
		if datatoplot == "Boiling Point":
			y = []
			for i in data:
				for e in data2:
					if e["symbol"] == i["Symbol"]:
						y.append(e["boiling_point"])
		if datatoplot == "Density":
			y = []
			for i in data:
				for e in data2:
					if e["symbol"] == i["Symbol"]:
						y.append(e["density"])
	else:
		y = [ i[datatoplot] for i in data ]

	fig = Figure(figsize=(5,5),dpi=100)

	plot1 = fig.add_subplot(111)
	plot1.set_title(datatoplot)
	plot1.set_ylabel(datatoplot+" Value")
	plot1.set_xlabel("Atomic Number")
	plot1.plot(y)
	


	canvas = FigureCanvasTkAgg(fig,master=window)

	canvas.draw()

	canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)

	toolbar = NavigationToolbar2Tk(canvas,window)

	toolbar.update()

	canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)
	return canvas
