from tkinter import *
from tkinter import ttk

global numbah
numbah = 0

def goofyaaah():
    global numbah
    numbah += 1
    print(numbah)
    labelU.configure(text=f"{numbah}")
    botaoU.configure(text=f"repete oxente{numbah}")

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# Button that calls the function when clicked
labelU = ttk.Label(frm, text=f"{numbah}")
labelU.grid(column=0, row=0)

botaoU = ttk.Button(frm, text=f"repete oxente{numbah}", command= goofyaaah)
botaoU.grid(column=1, row=0)

root.mainloop()