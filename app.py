from tkinter import *

root = Tk()


class Applicacao():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='#bc96eb')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)


Applicacao()
