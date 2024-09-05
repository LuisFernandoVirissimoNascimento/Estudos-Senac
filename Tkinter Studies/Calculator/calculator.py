import tkinter as tk
from tkinter import *
from tkinter import font
import pyautogui

class myDragManager():
    def add_dragable_widget(self, widget):
        self.widget = widget
        self.root = widget.winfo_toplevel()

        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease>", self.on_drop)
        self.widget.configure(cursor ="hand1")

    def on_drag(self, event):
        #x,y = pyautogui.position()
        self.widget.place(x = self.root.winfo_pointerx()- self.root.winfo_rootx() - 75, y = self.root.winfo_pointery()-self.root.winfo_rooty() - 65)
        
    
    def on_drop(self, event):
        #x,y = pyautogui.position()
        self.widget.place(x = self.root.winfo_pointerx()-self.root.winfo_rootx() - 75, y = self.root.winfo_pointery()-self.root.winfo_rooty() - 65)
        print("Widget placed", self.root.winfo_pointerx())
    


window = tk.Tk()

style = font.Font(size = 20)

wrapper = Frame(window,bg="gray")
wrapper.pack(fill="both",expand= True)

trollTitle = Label(wrapper,text="Haha sou uma calculadora de verdade", font = style)
trollTitle.place(x = 10, y = 10)
lbl = Label(wrapper,text="Hehe sou uma calculadora mal funcional", font = style)
lbl.place(x = 10, y = 10)

# Botões de calculo
igualBtn = Button(wrapper, text="=", font= style, command= lambda : print("Igual"))
igualBtn.place(x = 470, y = 570, width= 150, height= 125)

vezesBtn = Button(wrapper, text="*", font= style, command= lambda : print("Igual"))
vezesBtn.place(x = 470, y = 440, width= 150, height= 125)

divisaoBtn = Button(wrapper, text="/", font= style, command= lambda : print("Igual"))
divisaoBtn.place(x = 470, y = 310, width= 150, height= 125)

menosBtn = Button(wrapper, text="-", font= style, command= lambda : print("Igual"))
menosBtn.place(x = 470, y = 180, width= 150, height= 125)

plusBtn = Button(wrapper, text="+", font= style, command= lambda : print("Igual"))
plusBtn.place(x = 315, y = 180, width= 150, height= 125)

dottoBtn = Button(wrapper, text=".", font= style, command= lambda : print("Igual"))
dottoBtn.place(x = 160, y = 180, width= 150, height= 125)
# Numéricos
zeroBtn = Button(wrapper, text="0", font= style, command= lambda : print("Igual"))
zeroBtn.place(x = 5, y = 180, width= 150, height= 125)

umBtn = Button(wrapper, text="1", font= style, command= lambda : print("Igual"))
umBtn.place(x = 5,  y = 310, width= 150, height= 125)

doisBtn = Button(wrapper, text="2", font= style, command= lambda : print("Igual"))
doisBtn.place(x = 160,  y = 310, width= 150, height= 125)

tresBtn = Button(wrapper, text="3", font= style, command= lambda : print("Igual"))
tresBtn.place(x = 315,  y = 310, width= 150, height= 125)

quatroBtn = Button(wrapper, text="4", font= style, command= lambda : print("Igual"))
quatroBtn.place(x = 5, y = 440, width= 150, height= 125)

cincoBtn = Button(wrapper, text="5", font= style, command= lambda : print("Igual"))
cincoBtn.place(x = 160, y = 440, width= 150, height= 125)

sixBtn = Button(wrapper, text="6", font= style, command= lambda : print("Igual"))
sixBtn.place(x = 315, y = 440, width= 150, height= 125)

seteBtn = Button(wrapper, text="7", font= style, command= lambda : print("Igual"))
seteBtn.place(x = 5, y = 570, width= 150, height= 125)

oitoBtn = Button(wrapper, text="8", font= style, command= lambda : print("Igual"))
oitoBtn.place(x = 160, y = 570, width= 150, height= 125)

noveBtn = Button(wrapper, text="9", font= style, command= lambda : print("Igual"))
noveBtn.place(x = 315, y = 570, width= 150, height= 125)



# Drag jokes
myDrag1 = myDragManager()
myDrag1.add_dragable_widget(lbl)

myDrag2 = myDragManager()
myDrag2.add_dragable_widget(igualBtn)


window.geometry("625x700")
window.title("A Calculadora mais calculada de todos os tempos.")
window.mainloop()