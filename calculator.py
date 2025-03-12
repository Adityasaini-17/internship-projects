from tkinter import *
import math
root = Tk()
root.title("Calculator")
root.geometry("380x410")
root.resizable(False, False)
global scvalue
def click(event):
  text = event.widget.cget("text")
  
  if text == "=":
        try:
            
            expression = scvalue.get().replace('×', '*').replace('÷', '/')
            value = eval(expression)

            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    
        
                   
  elif text == "C":
    scvalue.set("")
    screen.update()
    
  elif text == "✖️":
    current_text = scvalue.get()
    scvalue.set(current_text [:-1])
    screen.update()

  elif text == "√":
        try:
          value = math.sqrt(float(scvalue.get()))
          scvalue.set(value)
        except ValueError:
          scvalue.set("Error")

  
  else:
    scvalue.set(scvalue.get() + text)
    screen.update()
    

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue, font = "lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


f = Frame(root,bg="grey")
f.pack()
b = Button(f,text="C",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="✖️",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx = 15,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="÷",padx = 35,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

f = Frame(root,bg="grey")
f.pack()
b = Button(f,text="7",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="9",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="×",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

f = Frame(root,bg="grey")
f.pack()
b = Button(f,text="4",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="6",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

f = Frame(root,bg="grey")
f.pack()
b = Button(f,text="1",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="3",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

f = Frame(root,bg="grey")
f.pack()
b = Button(f,text="√",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="0",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text=".",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx = 20,pady =8,font = "lucida 20 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

root.mainloop()


