from modulos import *
from validEntry import Validadores
from reports import Relatorios
from funcs import Funcoes
from placeHolder import EntryPlaceHolder
root = tix.Tk()

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
    background="silver",
    foreground="black",
    fieldbackground="silver",
    font=('verdana',8,'bold')
    )

style.map('listacli',
    background=[('selected','green')])


class Application(Funcoes, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menu()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background='#080227')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        # place, Pack and grid
        self.frame1 = Frame(self.root, bd=4, bg='#c2d1e0',
                            highlightbackground='#759fe6', highlightthickness=4)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#c2d1e0',
                            highlightbackground='#759fe6', highlightthickness=4)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background= "#c2d1e0")
        self.aba2.configure(background="lightgray")

        self.abas.add(self.aba1, text = "Aba 1")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx= 0, rely=0, relwidth=0.98, relheight=0.98)

        self.canvas_bt = Canvas(self.aba1, bd=0, bg='#1e3743', highlightbackground='gray',highlightthickness=5)
        self.canvas_bt.place(relx=0.19,rely= 0.08, relwidth=0.22, relheight=0.19)

        # limpar
        self.bt_limpar = Button(
            self.aba1, text="Limpar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold')
                    , command= self.limpar_tela, activebackground='#108ecb', activeforeground='white')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = "Digite no campo nome o cliente que deseja pesquisar")
        # novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # label input codigo
        self.lb_codigo = Label(self.aba1, text="Código",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.1)

        self.codigo_entry = Entry(self.aba1, validate= "key", validatecommand= self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.1)

        # label input nome
        self.lb_nome = Label(self.aba1, text="Nome",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = EntryPlaceHolder(self.aba1, 'Digite o nome do cliente')
        self.nome_entry.place(relx=0.05, rely=0.45,
                              relwidth=0.5, relheight=0.1)
        # label input telefone
        self.lb_telefone = Label(self.aba1, text="Telefone",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = EntryPlaceHolder(self.aba1, 'Formado : XX-XXXXXXXXX')
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        # label input cidade
        self.lb_cidade = Label(self.aba1, text="Cidade",bg='#c2d1e0',fg='#422fa2',font=('verdana',8,'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = EntryPlaceHolder(self.aba1,'Digite o nome completo sem abreviações')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

        #### drop down button
        self.TipVar = StringVar()
        self.TipV = ("Solteiro(a)", "Casado(a)","Divorciado(a)","Viuvo(a)")
        self.TipVar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.TipVar, *self.TipV)
        self.popupMenu.place(relx= 0.1, rely= 0.1, relwidth=0.2, relheight=0.2)
        self.estadoCivil = self.TipVar.get()
        print(self.estadoCivil)
        ##Calendario
        self.bt_calendario = Button(self.aba2, text="Data", command= self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx= 0.5, rely=0.2)
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
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    def Menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu1 = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()
        menubar.add_cascade(label= "Opções", menu= filemenu1)
        menubar.add_cascade(label= "Relatórios", menu= filemenu2)

        filemenu1.add_command(label="Sair", command=Quit)
        filemenu1.add_command(label="Limpa Cliente", command=self.limpar_tela)

        filemenu2.add_command(label="Ficha  do cliente", command=self.geraRelatorioCliente)
    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(background="lightblue")
        self.root2.geometry("400x200")
        self.root2.resizable(False,False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root.grab_set()
    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")

Application()
