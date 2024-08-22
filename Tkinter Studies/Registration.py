from tkinter import *
from tkinter import messagebox

def show_popup():
    loginCheck = login.get()
    senhaCheck = senha.get()
    senhaConfirmCheck = senhaConfirm.get()
    if loginCheck == "":
        messagebox.showerror("Erro", "Login está vazio")
        return
        
    if senhaCheck == "":
        messagebox.showerror("Erro", "Senha está vazio")
        return
    
    if senhaConfirmCheck != senhaCheck:
        messagebox.showerror("Erro", "Senha não é igual a confirmação de senha")
        return
    
    if senhaCheck == loginCheck:
        messagebox.showerror("Erro", "Login e senha não podem ser os mesmos")
        return
    
    
    messagebox.showinfo("Parabens", "Cadastro feito com sucesso !")
    



# Create the main application window
root = Tk()
root.geometry("720x480")
root.title("Main Window")
changesToWindow = Frame(root, background= 'grey')
changesToWindow.pack(fill="both",anchor='center',expand=True)

loginText = Label(changesToWindow, text= "Login :",fg= 'white',font=('Comic Sans MS',20),justify= 'left',anchor= 'center',background= "gray")
loginText.pack(pady=5)
login = Entry(changesToWindow)
login.pack(pady=20)

senhaText = Label(changesToWindow, text= "Senha :",fg= 'white',font=('Comic Sans MS',20),justify= 'left',anchor= 'center',background= "gray")
senhaText.pack(pady=5)
senha = Entry(changesToWindow)
senha.pack(pady=20)

senhaConfirmText = Label(changesToWindow, text= "Confirmar Senha :",fg= 'white',font=('Comic Sans MS',20),justify= 'left',anchor= 'center',background= "gray")
senhaConfirmText.pack(pady=5)
senhaConfirm = Entry(changesToWindow)
senhaConfirm.pack(pady=20)
# Create a button that will trigger the popup
button = Button(changesToWindow, text="Click Me!", command=show_popup)
button.pack(pady=20)


root.mainloop()