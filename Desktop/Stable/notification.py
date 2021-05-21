import tkinter as tk
from bs4 import BeautifulSoup
import urllib.request
from version import __version__
import tkinterplus as ttx
import webbrowser

website = "https://wiredfuturelabs.github.io/Henry-Molar/notification.html"
version_website = "https://wiredfuturelabs.github.io/Henry-Molar/versioncontrol.html"
notification_website = "https://wiredfuturelabs.github.io/Henry-Molar/notifyuser.html"

def update(arg=None):
	webbrowser.open("https://wiredfuturelabs.github.io/Henry-Molar")
def checkversion():
	fp = urllib.request.urlopen(version_website)
	mybytes = fp.read()

	html = mybytes.decode("utf8")
	fp.close()

	soup = BeautifulSoup(html, 'html.parser')

	data = soup.find('p').getText()
	data = eval(data)
	data = data[4]
	data = data["mac"]

	if data == __version__:
		return True
	else:
		return False


def rendernotification():
	try:
		if checkversion() == True:
			pass
		else:
			fp = urllib.request.urlopen(website)
			mybytes = fp.read()

			html = mybytes.decode("utf8")
			fp.close()

			soup = BeautifulSoup(html, 'html.parser')

			data = soup.find('p').getText()
			data = eval(data)

			notifyWindow = tk.Toplevel()
			notifyWindow.geometry("500x500")
			notifyWindow.attributes("-topmost", True)
			notifyWindow.config(bg="white")
			notifyWindow.resizable(False,False)
			tk.Label(notifyWindow,text=data[0],bg="white",fg="black",font=("avenir",23)).grid(row=0,column=0,columnspan=2,pady=(20,20),padx=1)

			row = 1
			for messages in data[1:]:
				point = '\u2022'
				tk.Label(notifyWindow,text=('\n%s'+messages) % point,bg="white",fg="black",font=("avenir",17)).grid(row=row,column=0,columnspan=2,padx=1,sticky=tk.W)
				row += 1

			if checkversion() == False:
				up =tk.Label(notifyWindow,text="Update",bg=ttx.rgb(32,140,255),fg="white",font=("avenir",17))
				up.grid(row=row,column=0,columnspan=2,padx=1,pady=30,sticky=tk.E)
				up.bind("<Button-1>",update)
	except:
		pass

def notification():
	fp = urllib.request.urlopen(notification_website)
	mybytes = fp.read()

	html = mybytes.decode("utf8")
	fp.close()

	soup = BeautifulSoup(html, 'html.parser')

	data = soup.find('p').getText()
	data = eval(data)
	notifyWindow = tk.Toplevel()
	notifyWindow.geometry("500x500")
	notifyWindow.attributes("-topmost", True)
	notifyWindow.config(bg="white")
	tk.Label(notifyWindow,text=data[0],bg="white",fg="black",font=("avenir",23)).grid(row=0,column=0,columnspan=2,pady=(20,20),padx=1)

	row = 1
	for messages in data[1:]:
		point = '\u2022'
		tk.Label(notifyWindow,text=('\n%s'+messages) % point,bg="white",fg="black",font=("avenir",17)).grid(row=row,column=0,columnspan=2,padx=1,sticky=tk.W)
		row += 1


