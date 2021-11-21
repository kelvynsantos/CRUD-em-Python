from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def geraRelatorioCliente(self):
        self.c = canvas.Canvas("cliente.pdf")
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 600, 'Cidade: ')


        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.telefoneRel)
        self.c.drawString(150, 600, self.cidadeRel)


        self.c.rect(20, 720, 550, 200, fill= False, stroke= True)

        self.c.showPage()
        self.c.save()
        self.printCliente()
class Funcoes():
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
    def conecta_db(self):
        self.conne = sqlite3.connect("clientes.db")
        self.cursor = self.conne.cursor();print("Conectando ao DB")
    def desconecta_db(self):
        self.conne.close();print("Desconectando ao DB")
    def montaTabelas(self):
        self.conecta_db()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes( 
                cod INTEGER PRIMARY KEY, 
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            ); 
        """)
        self.conne.commit(); print("DB criado")
        self.desconecta_db()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def add_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)  
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conne.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? 
            WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conne.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()
    def deleta_cliente(self):
         self.variaveis()
         self.conecta_db()
         self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
         self.conne.commit()
         self.desconecta_db()
         self.limpar_tela()
         self.select_lista()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_db()
    def busca_cliente(self):
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END,'%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscaNomeCli = self.cursor.fetchall()
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values=1)
        self.limpar_tela()
        self.desconecta_db()
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


class Application(Funcoes, Relatorios):
    def __init__(self):
        self.root = root
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
        self.canvas_bt = Canvas(self.frame1, bd=0, bg='#1e3743', highlightbackground='gray',highlightthickness=5)
        self.canvas_bt.place(relx=0.19,rely= 0.08, relwidth=0.22, relheight=0.19)

        # limpar
        self.bt_limpar = Button(
            self.frame1, text="Limpar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold')
                    , command= self.limpar_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # buscar
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # novo
        self.bt_novo = Button(self.frame1, text="Novo", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # alterar
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # apagar
        self.bt_apagar = Button(self.frame1, text="Apagar", bd=3, bg='#422fa2', fg='white',font=('verdana',8,'bold'), command= self.deleta_cliente)
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
Application()
