import tkinter as tk
from tkinter import *
from tkinter import font

class myDragManager():
    def add_dragable_widget(self, widget):
        self.widget = widget
        self.root = widget.winfo_toplevel()

        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease>", self.on_drop)
        self.widget.configure(cursor ="hand1")

    def on_drag(self, event):
        self.widget.place(x=self.root.winfo_pointerx() - self.root.winfo_rootx() - 75, y=self.root.winfo_pointery() - self.root.winfo_rooty() - 65)

    def on_drop(self, event):
        self.widget.place(x=self.root.winfo_pointerx() - self.root.winfo_rootx() - 75, y=self.root.winfo_pointery() - self.root.winfo_rooty() - 65)
        print("Widget placed", self.root.winfo_pointerx())

# Função de cálculo
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))  # Calcula a expressão
        input_text.set(result)
        expression = result
    except:
        input_text.set("Erro")
        expression = ""

def btn_equaltroll():
    global expression
    try:
        input_text.set("olá mndo !!!@")
    except:
        input_text.set("Erro")
        expression = ""
# Janela principal
window = tk.Tk()

expression = ""
input_text = StringVar()

style = font.Font(size=20)
styler = font.Font(size=20)

wrapper = Frame(window, bg="gray")
wrapper.pack(fill="both", expand=True)

# Campo de exibição do cálculo
trollTitle = Label(wrapper, text="Haha sou uma calculadora de verdade", font=style)
trollTitle.place(x=10, y=10)
lbl = Label(wrapper,text="Hehe sou uma calculadora mal funcional", font = style)
lbl.place(x = 10, y = 10)

input_frame = Frame(wrapper, bg="black")
input_frame.place(x=10, y=60, width=610, height=100)

input_field = Entry(input_frame, font=style, textvariable=input_text, width=50, bg="white", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Botões de cálculo
realBtn = Button(wrapper, text="=", font=style, command=btn_equal, background= "black",foreground="white")
realBtn.place(x=470, y=570, width=150, height=125)

igualBtn = Button(wrapper, text="=", font=style, command=btn_equaltroll)
igualBtn.place(x=470, y=570, width=150, height=125)

vezesBtn = Button(wrapper, text="*", font=style, command=lambda: btn_click('*'))
vezesBtn.place(x=470, y=440, width=150, height=125)

divisaoBtn = Button(wrapper, text="/", font=style, command=lambda: btn_click('/'))
divisaoBtn.place(x=470, y=310, width=150, height=125)

menosBtn = Button(wrapper, text="-", font=style, command=lambda: btn_click('-'))
menosBtn.place(x=470, y=180, width=150, height=125)

plusBtn = Button(wrapper, text="+", font=style, command=lambda: btn_click('+'))
plusBtn.place(x=315, y=180, width=150, height=125)

dottoBtn = Button(wrapper, text=".", font=style, command=lambda: btn_click('.'))
dottoBtn.place(x=160, y=180, width=150, height=125)

# Numéricos
zeroBtn = Button(wrapper, text="0", font=style, command=lambda: btn_click(0))
zeroBtn.place(x=5, y=180, width=150, height=125)

umBtn = Button(wrapper, text="1", font=style, command=lambda: btn_click(1))
umBtn.place(x=5, y=310, width=150, height=125)

doisBtn = Button(wrapper, text="2", font=style, command=lambda: btn_click(2))
doisBtn.place(x=160, y=310, width=150, height=125)

tresBtn = Button(wrapper, text="3", font=style, command=lambda: btn_click(3))
tresBtn.place(x=315, y=310, width=150, height=125)

quatroBtn = Button(wrapper, text="4", font=style, command=lambda: btn_click(4))
quatroBtn.place(x=5, y=440, width=150, height=125)

cincoBtn = Button(wrapper, text="5", font=style, command=lambda: btn_click(5))
cincoBtn.place(x=160, y=440, width=150, height=125)

sixBtn = Button(wrapper, text="6", font=style, command=lambda: btn_click(6))
sixBtn.place(x=315, y=440, width=150, height=125)

seteBtn = Button(wrapper, text="7", font=style, command=lambda: btn_click(7))
seteBtn.place(x=5, y=570, width=150, height=125)

oitoBtn = Button(wrapper, text="8", font=style, command=lambda: btn_click(8))
oitoBtn.place(x=160, y=570, width=150, height=125)

noveBtn = Button(wrapper, text="9", font=style, command=lambda: btn_click(9))
noveBtn.place(x=315, y=570, width=150, height=125)

# Botão de limpar
clearBtn = Button(wrapper, text="C", font=style, command=btn_clear)
clearBtn.place(x=5, y=60, width=150, height=100)

# Drag jokes
myDrag1 = myDragManager()
myDrag1.add_dragable_widget(lbl)

myDrag2 = myDragManager()
myDrag2.add_dragable_widget(igualBtn)

window.geometry("625x700")
window.title("A Calculadora mais calculada de todos os tempos.")
window.mainloop()
