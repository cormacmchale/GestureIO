from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    selected = variable.get()
    print ("value is:" + variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()