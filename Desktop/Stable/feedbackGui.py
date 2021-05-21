import tkinter as tk
import tkinterplus as ttx
from feedbackProcess import sendfeedback

font = "avenir"
fontSize = 16

def startfeedback(master,current,reinsert,icon):

  bg = ttx.rgb(23,27,33)
  fg = "white"
  imgc = icon


  current.destroy()

  def goback(arg):
    FeedbackWindow.destroy()
    reinsert()

  def send(event):
    result = tk.Label(FeedbackWindow,text="Sending...",bg="black",fg="white")
    result.grid(row=7,column=0,columnspan=2,sticky=tk.W+tk.E)
    if str(mail.get()) == "" or str(name.get()) == "" or str(feedback.getAll()) == "":
      result.config(text="Fill all fields!")
    else:
      if str(mail.get()).find("@") == -1 or str(mail.get()).find(".") == -1:
        result.config(text="Invalid Mail")
      else:
        try:
          result.config(text=sendfeedback(name=name,mail=mail,feedback=feedback),bg="black",fg=fg)
          name.delete(0,tk.END)
          mail.delete(0,tk.END)
          feedback.delete('1.0', tk.END)
          name.focus_set()
        except:
          result.config("We ran into an error please try again!")
    FeedbackWindow.after(2500,result.destroy)
    FeedbackWindow.update()
    FeedbackWindow.after(2600,FeedbackWindow.update)



  FeedbackWindow = tk.Frame()
  FeedbackWindow.pack(fill=tk.BOTH,expand=1)
  FeedbackWindow.config(bg=bg)
  FeedbackWindow.bind("<Escape>",goback)
  for i in range(0,8):
    FeedbackWindow.grid_rowconfigure(i,weight=1)
  for i in range(0,2):
    FeedbackWindow.grid_columnconfigure(i,weight=1)


  backBut = tk.Label(FeedbackWindow,image=imgc,bg=bg,fg=fg,font=("avenir",20))
  backBut.grid(row=0,column=0,sticky=tk.W)
  backBut.bind("<Button-1>",goback)

  tk.Label(FeedbackWindow,fg=fg,bg=bg,text="Feedback:",font=(font,30)).grid(row=1,column=0,sticky=tk.W+tk.E)

  tk.Label(FeedbackWindow,text="Name:",font=(font,fontSize),fg=fg,bg=bg).grid(row=2,column=0,pady=20,sticky=tk.W+tk.E)

  name = tk.Entry(FeedbackWindow,font=(font,18),relief="solid",insertbackground=fg,borderwidth=1,bg=bg,fg=fg,highlightcolor=fg,highlightbackground=fg,highlightthickness=1)
  name.grid(row=2,column=1,padx=30,sticky=tk.W+tk.E)
  name.focus_set()
  name.bind("<Escape>",goback)

  tk.Label(FeedbackWindow,text="Mail Id:",font=(font,fontSize),fg=fg,bg=bg).grid(row=3,column=0,pady=20,sticky=tk.W+tk.E)

  mail = tk.Entry(FeedbackWindow,font=(font,18),relief="solid",borderwidth=1,insertbackground=fg,bg=bg,fg=fg,highlightcolor=fg,highlightbackground=fg,highlightthickness=1)
  mail.grid(row=3,column=1,padx=30,sticky=tk.W+tk.E)
  mail.bind("<Escape>",goback)

  tk.Label(FeedbackWindow,text="Feedback:",font=(font,fontSize),fg=fg,bg=bg).grid(row=4,column=0,pady=20,sticky=tk.W+tk.E)

  feedback = ttx.CodeEditor(FeedbackWindow,font=(font,18),height=10,width=30,insertbackground=fg,highlightcolor=fg,highlightbackground=fg,highlightthickness=1,relief="solid",borderwidth=1,bg=bg,fg=fg)
  feedback.grid(row=4,column=1,padx=30,rowspan=2,sticky=tk.W+tk.E)
  feedback.bind("<Escape>",goback)

  button = tk.Label(FeedbackWindow,text="Submit",bg=ttx.rgb(32,140,255),fg=fg,pady=5)
  button.grid(row=6,column=0,columnspan=2,pady=20,padx=30,sticky=tk.W+tk.E)
  button.bind("<Button-1>",send)

  def setfocus(widget=None):
    widget.focus_set()

  name.bind("<Return>",lambda event:setfocus(mail))
  name.bind("<Down>",lambda event:setfocus(mail))

  mail.bind("<Up>",lambda event:setfocus(name))
  mail.bind("<Return>",lambda event:setfocus(feedback))
  mail.bind("<Down>",lambda event:setfocus(feedback))

  feedback.bind("<Up>",lambda event: setfocus(mail))
  feedback.bind("<Return>",send)
  
