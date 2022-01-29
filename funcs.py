from modulos import *

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
        if self.nome_entry.get() == "":
            msg = "Para cadastrar um novo cliente é necessário \n"
            msg += "que seja digitado pelo menos um nome"
            messagebox.showinfo("Cadastro de clientes - Aviso!!!" , msg)
        else:
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
    def calendario(self):
        self.calendario1 = Calendar(self.aba2, fg="gray75", bg= "blue", font=("Times",'9','bold'), locale='pt_br')
        self.calendario1.place(relx=0.5, rely=0.1)
        self.calData = Button(self.aba2, text= "Inserir Data", command= self.print_cal)
        self.calData.place(relx=0.85, rely=0.85, height=25, width=100)

    def print_cal(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calData.destroy()