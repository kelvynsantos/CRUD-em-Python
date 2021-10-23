from tkinter import * 
from tkinter import ttk

root = Tk()
#root.iconbitmap('images/registry.png')
my_tree = ttk.Treeview(root)


class Applicacao():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1() 
        self.widgets_frame2() 
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de clientes") 
        self.root.configure(background='#080227')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
#place, Pack and grid

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#c2d1e0',
                            highlightbackground='#759fe6', highlightthickness=4)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#c2d1e0',
                            highlightbackground='#759fe6', highlightthickness=4)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # limpar
        self.bt_limpar = Button(
            self.frame1, text="Limpar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # buscar
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # novo
        self.bt_novo = Button(self.frame1, text="Novo", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # alterar
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # apagar
        self.bt_apagar = Button(self.frame1, text="Apagar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # label input codigo
        self.lb_codigo = Label(self.frame1, text="Código",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.1)

        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.1)

        # label input nome
        self.lb_nome = Label(self.frame1, text="Nome",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45,
                              relwidth=0.5, relheight=0.1)
        # label input telefone
        self.lb_telefone = Label(self.frame1, text="Telefone",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        # label input cidade
        self.lb_cidade = Label(self.frame1, text="Cidade",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
 
    def widgets_frame2(self): 
        self.listaCli = ttk.Treeview(self.frame2,height= 3, column=("col1","col2","col3","col4")) 
        self.listaCli.heading("#0",text="")
        self.listaCli.heading("#1",text="Código") 
        self.listaCli.heading("#2",text="Nome") 
        self.listaCli.heading("#3",text="Telefone") 
        self.listaCli.heading("#4",text="Cidade") 
        
        self.listaCli.column("#0", width=1) 
        self.listaCli.column("#1",width=50) 
        self.listaCli.column("#2",width=200)
        self.listaCli.column("#3",width=125)
        self.listaCli.column("#4",width=125) 
         
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85) 

        self.scroolLista = Scrollbar(self.frame2, orient='vertical') 
        self.listaCli.configure(yscroll=self.scroolLista.set) 
        self.scroolLista.place(relx=0.96,rely=0.1,relwidth=0.04, relheight=0.85)
Applicacao() 
 