from tkinter import *
from some_library.atm import *

# Criando um objeto para trazer a classe "Tk()" que traz tudo que a gente vai usar na interface 

root = Tk()

#Classe para funções que interagem diretamente com a interface

class Funcoes():
    
#Função para limpar a tela do nosso caixa eletronico, podendo colocar novos widgets "atualizando" a tela kk

    def limpa_tela(self, tela):
        
        for widgets in tela.winfo_children():
            widgets.destroy()

#Função para fazer a confirmação dos dados e permitir o programa avançar para a próxima tela

    def logar(self):
        self.usuario = {}
        self.cod = self.en_conta.get()
        self.senha = self.en_senha.get()
        if (self.cod in self.bancoDados.gerentes) == True:
            if (self.senha == self.bancoDados.gerentes[self.cod]["Senha"]) == True:
                nome = self.bancoDados.gerentes[self.cod]["Nome"]
                print(f"Login com Sucesso! Seja bem vindo {nome}")
                self.limpa_tela(self.frame1)
                self.usuario =  self.bancoDados.gerentes[self.cod]
                self.tela_usuario("")
            else:
                self.tela_usuario ("Falha no login! Senha incorreta!")
        elif (self.cod in self.bancoDados.clientes) == True:
            if (self.senha == self.bancoDados.clientes[self.cod]["Senha"]) == True:
                nome = self.bancoDados.clientes[self.cod]["Nome"]
                print(f"Login com Sucesso! Seja bem vindo {nome}")
                self.limpa_tela(self.frame1)
                self.usuario = self.bancoDados.clientes[self.cod]
                self.tela_usuario("")
            else:
                self.tela_usuario("Falha no login! Senha incorreta!")
        else: 
            self.tela_usuario("Falha no login! Conta inesxistente!")
        

    def mostra_lista_gerente(self):
        self.l_cliente_lista = Label(self.fr_lista, text = "Clientes", foreground="#50C649", background="#1C1C1C", font= ("Terminal", "12", "bold"))
        self.l_cliente_lista.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.scrollbar_lista = Scrollbar(self.fr_lista, bg="#1C1C1C", troughcolor="#50C649", activebackground="#000000")
        self.scrollbar_lista.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.8)

        self.lista_gerente = Listbox(self.fr_lista, bg="#1C1C1C", foreground="#50C649", highlightbackground="#50C649",
                                     selectbackground="#50C649", selectforeground="#1C1C1C", font=("Terminal", "10"), yscrollcommand= self.scrollbar_lista.set)
        for cod in self.bancoDados.clientes:
            self.lista_gerente.insert(END, cod)
        self.lista_gerente.place(relx=0.0, rely= 0.2, relwidth=0.9, relheight=0.8)
        self.scrollbar_lista.config(command= self.lista_gerente.yview)
        
    
    def mostra_funcoes_gerente(self):
        self.bt_cadastra = Button(self.fr_acoes, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Cadastrar novo cliente", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_cadastra_cli())
        self.bt_cadastra.place(relx=0, rely=0, relwidth=1, relheight=0.25)

        self.bt_remover = Button(self.fr_acoes, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Remover cliente", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.select_del())
        self.bt_remover.place(relx=0, rely=0.25, relwidth=1, relheight=0.25)

        self.bt_editar = Button(self.fr_acoes, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Editar conta", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.select_edit())
        self.bt_editar.place(relx=0, rely=0.5, relwidth=1, relheight=0.25)

        self.bt_visualiza = Button(self.fr_acoes, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Visualizar conta", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.select_view())
        self.bt_visualiza.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

    def select_edit(self):
        selecao = self.lista_gerente.curselection()
        if selecao == ():
            self.mostra_aviso("AVISO: Você tem que selecionar o cliente\n para fazer a ação designada!")
        else:
            res = self.lista_gerente.get(selecao)
            self.tela_edita_cli(res)

    def select_del(self):
        selecao = self.lista_gerente.curselection()
        if selecao == ():
            self.mostra_aviso("AVISO: Você tem que selecionar o cliente\n para fazer a ação designada!")
        else:
            res = self.lista_gerente.get(selecao)
            self.tela_remove_cli(res)
    
    def select_view(self):
        selecao = self.lista_gerente.curselection()
        if selecao == ():
            self.mostra_aviso("AVISO: Você tem que selecionar o cliente\n para fazer a ação designada!")
        else:
            res = self.lista_gerente.get(selecao)
            self.tela_visualiza_cli(res)
        
    def verifica_se_pode_del(self, cod):
        if self.bancoDados.clientes[cod]["Saldo"] == 0:
            self.user.remover_user(self.bancoDados.clientes, cod)
            self.tela_usuario("")
        else:
            self.tela_usuario("")
            self.mostra_aviso(f"ERROR! Usuário não pode deletar a conta {cod}\n enquanto ela não estiver ZERADA")
        
    
    def mostra_aviso(self, aviso):
        self.tela_aviso_select = Frame(self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.tela_aviso_select.place(relx= 0.5, rely= 0.5, relwidth= 0.8, relheight= 0.4, anchor=CENTER)

        self.botao_x = Button(self.tela_aviso_select, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="X", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_usuario(""))
        self.botao_x.place(relx=0.95, rely=0.15, relwidth=0.1, relheight=0.3, anchor=CENTER)

        self.l_aviso = Label(self.tela_aviso_select, text = aviso, foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_aviso.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    def mostra_dados_gerente(self):
        self.l_admin = Label(self.fr_info_conta, text = "ADMINISTRADOR", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.l_admin.place(relx=0.02, rely=0.01)
        
        self.l_nome_gerente = Label(self.fr_info_conta, text = self.usuario["Nome"], foreground="#50C649", background="#1C1C1C", font=("Terminal", "12", "bold"))
        self.l_nome_gerente.place(relx=0.02, rely=0.4)

        self.l_codigo_conta = Label(self.fr_info_conta, text = self.cod, foreground="#50C649", background="#1C1C1C", font=("Terminal", "12", "bold"))
        self.l_codigo_conta.place(relx=0.02, rely=0.7)
    
    def faz_titulo(self, titulo):

        self.fr_titulo_pag = Frame(self.frame1, bg="#50C649", highlightbackground= "#50C649", highlightthickness=1.5)
        self.fr_titulo_pag.place(relx= 0.5, rely= 0.04, relwidth= 0.20, relheight= 0.1, anchor=CENTER)
        self.login = Label(self.fr_titulo_pag, text = titulo, foreground="#1C1C1C", background="#50C649", font=self.tela_fonte)
        self.login.place(relx=0.5, rely=0.5, anchor=CENTER)

    def faz_cabecalho(self):
        self.bt_log_out = Button(self.frame1, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Log Out", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_inicial())
        self.bt_log_out.place(relx=0.90, rely=0.04, relwidth=0.20, relheight=0.1, anchor=CENTER)

        self.bt_log_out = Button(self.frame1, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#50C649")
        self.bt_log_out.place(relx=0.70, rely=0.04, relwidth=0.20, relheight=0.1, anchor=CENTER)

        self.bt_log_out = Button(self.frame1, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#50C649")
        self.bt_log_out.place(relx=0.30, rely=0.04, relwidth=0.20, relheight=0.1, anchor=CENTER)

        self.bt_log_out = Button(self.frame1, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#50C649")
        self.bt_log_out.place(relx=0.10, rely=0.04, relwidth=0.20, relheight=0.1, anchor=CENTER)

        
                
        
# Classe da interface =)
class SistemaBancario(Funcoes):
    def __init__(self, master=None):

# Fazendo as compsições ou criando variáveis que vão ser necessárias
        self.bancoDados = BancoDeDados()
        self.hist = {}
        self.usuario = {}
        self.cod = ""
        self.senha = ""

# Definindo estilo, tamanho e tipo de fonte padrão pra interface (não necessariamente tudo vai ser assim)
        self.tela_fonte = ("Terminal", "16", "bold")
        self.tela_fontinha = ("Terminal", "12", "bold")

# Construindo a interface inicial
        self.root = root
        self.interface_basica()

        self.frame1 = Frame(self.root, bd = 4, bg="#1C1C1C", highlightbackground= "#4D4D4D", highlightthickness=6)
        self.frame1.place(relx= 0.03, rely= 0.03, relwidth= 0.94, relheight= 0.50)

        self.tela_inicial()
        self.criando_botoes()
        root.mainloop()


# Função para construção da página de login
    def tela_login(self, aviso):
        self.limpa_tela(self.frame1)
        self.faz_titulo("LOGIN")

        self.t_aviso = Label(self.frame1, text = aviso, foreground="#50C649", background="#1C1C1C", font=("Terminal", "10", "bold"))
        self.t_aviso.place(relx=0.5, rely=0.30, anchor=CENTER)
        
        self.t_conta = Label(self.frame1, text = "Conta:", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.t_conta.place(relx=0.12, rely=0.42, anchor=CENTER)
        self.en_conta = Entry(self.frame1, background="#50C649", highlightbackground="#1C1C1C", font=self.tela_fonte)
        self.en_conta.place(relx=0.55, rely=0.42, relwidth=0.7, relheight=0.1, anchor=CENTER)

        self.t_senha = Label(self.frame1, text = "Senha:", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.t_senha.place(relx=0.12, rely=0.56, anchor=CENTER)
        self.en_senha = Entry(self.frame1, background="#50C649", highlightbackground="#1C1C1C", show="*", font=self.tela_fonte)
        self.en_senha.place(relx=0.55, rely=0.56, relwidth=0.7, relheight=0.1, anchor=CENTER)

        self.bt_logar = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Logar", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.logar())
        self.bt_logar.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.1, anchor=CENTER)

        self.bt_voltar = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Voltar", 
                                  font= ("Terminal", "12", "bold"), activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_inicial())
        self.bt_voltar.place(relx=0.88, rely=0.90, relwidth=0.11, relheight=0.09)


# Função para construção da tela de usuário
# Tive que fazer uma gambiarra e essa função também faz parte de confirmar se os dados 
# estão coerentes e gerar a pagina correspondente para o devido tipo de usuário ("Gerente" ou "Cliente")

    def tela_usuario(self, aviso):

        self.limpa_tela(self.frame1)
        self.faz_cabecalho()
        self.frames_menu_de_usuário()

        if self.usuario == {}:
            self.tela_login(aviso)
        
        elif ("Saldo" in self.usuario) == True:
            if self.usuario["Tipo"] == "Empresa":
                self.user = Empresa(self.usuario["Saldo"], self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], self.usuario["CPF/CNPJ"], self.usuario["Tipo"], self.cod)
                
            else:
                self.user = PessoaFisica(self.usuario["Saldo"], self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], self.usuario["CPF/CNPJ"], self.usuario["Tipo"], self.cod)
                
            self.faz_titulo("CLIENTE") 

        elif self.usuario["Tipo"] == "Gerente":
                self.user = Gerente(self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], "000100", self.usuario["Tipo"])   
                self.mostra_dados_gerente()
                self.mostra_lista_gerente()
                self.mostra_funcoes_gerente()
                self.faz_titulo("GERENTE")

    def tela_cadastra_cli(self):
        pass

    def tela_remove_cli(self, cod):
        self.tela_deleta = Frame(self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.tela_deleta.place(relx= 0.5, rely= 0.5, relwidth= 0.6, relheight= 0.8, anchor=CENTER)

        self.l_confirma_del = Label(self.tela_deleta, text = "Você tem certeza que quer deletar\n essa conta?", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_confirma_del.place(relx=0.5, rely=0.1, anchor=CENTER)
    
        self.l_nome_cli = Label(self.tela_deleta, text = "Nome :", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_nome_cli.place(relx=0.03, rely=0.25)
        self.l_nomereal_cli = Label(self.tela_deleta, text = self.bancoDados.clientes[cod]["Nome"], foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_nomereal_cli.place(relx=0.25, rely=0.25)

        self.l_cod_cli = Label(self.tela_deleta, text = "Cód. :", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_cod_cli.place(relx=0.03, rely=0.4)
        self.l_codreal_cli = Label(self.tela_deleta, text = cod, foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_codreal_cli.place(relx=0.25, rely=0.40)

        self.l_sal_cli = Label(self.tela_deleta, text = "Saldo:", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_sal_cli.place(relx=0.03, rely=0.55)
        self.l_salreal_cli = Label(self.tela_deleta, text = "R$" + str(self.bancoDados.clientes[cod]["Saldo"]), foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.l_salreal_cli.place(relx=0.25, rely=0.55)
        
        self.botao_x = Button(self.tela_deleta, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Cancelar", 
                                  font=self.tela_fontinha, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_usuario(""))
        self.botao_x.place(relx=0.3, rely=0.85, relwidth=0.3, relheight=0.1, anchor=CENTER)

        self.botao_x = Button(self.tela_deleta, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Confirmar", 
                                  font=self.tela_fontinha, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.verifica_se_pode_del(cod))
        self.botao_x.place(relx=0.7, rely=0.85, relwidth=0.3, relheight=0.1, anchor=CENTER)

        

    def tela_edita_cli(self):
        pass

    def tela_visualiza_cli(self, cod = ""):
        
        self.tela_visualiza = Frame(self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.tela_visualiza.place(relx= 0.5, rely= 0.5, relwidth= 0.5, relheight= 0.8, anchor=CENTER)

        self.botao_x = Button(self.tela_visualiza, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="X", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_usuario(""))
        self.botao_x.place(relx=0.95, rely=0.05, relwidth=0.1, relheight=0.1, anchor=CENTER)

        self.l_nome_cli = Label(self.tela_visualiza, text = "Nome: ", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_nome_cli.place(relx=0.03, rely=0.05)
        self.l_nomereal_cli = Label(self.tela_visualiza, text = self.bancoDados.clientes[cod]["Nome"], foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_nomereal_cli.place(relx=0.23, rely=0.05)

        self.l_end_cli = Label(self.tela_visualiza, text = "End: ", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_end_cli.place(relx=0.03, rely=0.17)
        self.l_endreal_cli = Label(self.tela_visualiza, text = self.bancoDados.clientes[cod]["Endereco"], foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_endreal_cli.place(relx=0.23, rely=0.17)

        self.l_tel_cli = Label(self.tela_visualiza, text = "Tel: ", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_tel_cli.place(relx=0.03, rely=0.29)
        self.l_telreal_cli = Label(self.tela_visualiza, text = self.bancoDados.clientes[cod]["Telefone"], foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_telreal_cli.place(relx=0.23, rely=0.29)

        self.l_cpf_cli = Label(self.tela_visualiza, text = "CPF: ", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_cpf_cli.place(relx=0.03, rely=0.41)
        self.l_cpfreal_cli = Label(self.tela_visualiza, text = self.bancoDados.clientes[cod]["CPF/CNPJ"], foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_cpfreal_cli.place(relx=0.23, rely=0.41)

        self.l_sal_cli = Label(self.tela_visualiza, text = "Saldo: ", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.l_sal_cli.place(relx=0.03, rely=0.53)
        self.l_salreal_cli = Label(self.tela_visualiza, text = "R$ " + str(self.bancoDados.clientes[cod]["Saldo"]), foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.l_salreal_cli.place(relx=0.03, rely=0.70)

            
    def tela_confirma_senha(self, cod):

        self.tela_aviso_select = Frame(self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.tela_aviso_select.place(relx= 0.5, rely= 0.3, relwidth= 0.5, relheight= 0.5, anchor=CENTER)

        self.botao_x = Button(self.tela_aviso_select, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="X", 
                                  font=self.tela_fonte, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.tela_usuario(""))
        self.botao_x.place(relx=0.95, rely=0.15, relwidth=0.1, relheight=0.3, anchor=CENTER)

        self.en_confirma_senha = Entry(self.tela_aviso_select, text = "Senha", foreground="#50C649", background="#1C1C1C", font=self.tela_fontinha)
        self.en_confirma_senha.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.botao_confirma = Button(self.tela_deleta, bg="#50C649", highlightbackground="#50C649", highlightthickness=1.5, foreground="#1C1C1C", text="Confirmar", 
                                  font=self.tela_fontinha, activebackground="#1C1C1C", activeforeground="#50C649", command=lambda : self.verifica_se_pode_del(cod))
        self.botao_confirma.place(relx=0.5, rely=0.85, relwidth=0.5, relheight=0.1, anchor=CENTER)

# Função para construir a interface principal (caixa eletrônico), e que diferentemente da tela, é imutável

    def interface_basica(self):
        self.root.title("Caixa Bancário")
        self.root.configure(background="#5E5D5D") 
        self.root.geometry("700x700")
        self.root.resizable(False, False)

# Função constroi a tela inicial de quando ligamos o prgrama

    def tela_inicial(self):

        self.limpa_tela(self.frame1)

        self.faz_titulo("MENU")


        self.botao_login = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Login", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_login(""))
        self.botao_login.place(relx=0.5, rely=0.42, relwidth=0.4, relheight=0.1, anchor=CENTER)


        self.botao_sair = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Sair", 
                                 font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=self.root.quit)
        self.botao_sair.place(relx=0.5, rely=0.54, relwidth=0.4, relheight=0.1, anchor=CENTER)

# Função para padronizar frames do menu de usuários

    def frames_menu_de_usuário(self):

        self.fr_info_conta = Frame (self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.fr_info_conta.place(relx= 0.01, rely= 0.12, relwidth= 0.71, relheight= 0.36)

        self.fr_acoes = Frame (self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.fr_acoes.place(relx= 0.01, rely= 0.5, relwidth= 0.71, relheight= 0.5)

        self.fr_lista = Frame (self.frame1, bd = 4, bg="#1C1C1C", highlightbackground= "#50C649", highlightthickness=3)
        self.fr_lista.place(relx= 0.73, rely= 0.12, relwidth= 0.27, relheight= 0.88)


# Função para criar todos os botões de nosso Caixa Eletrônico principal
    
    def criando_botoes(self):
        self.botao1 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="1", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao1.place(relx= 0.03, rely= 0.55, relwidth= 0.22, relheight= 0.09)

        self.botao2 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="2", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao2.place(relx= 0.27, rely= 0.55, relwidth= 0.22, relheight= 0.09) 

        self.botao3 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="3", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao3.place(relx= 0.51, rely= 0.55, relwidth= 0.22, relheight= 0.09)

        self.botao4 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="4", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao4.place(relx= 0.03, rely= 0.66, relwidth= 0.22, relheight= 0.09)

        self.botao5 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="5", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao5.place(relx= 0.27, rely= 0.66, relwidth= 0.22, relheight= 0.09) 

        self.botao6 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="6", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao6.place(relx= 0.51, rely= 0.66, relwidth= 0.22, relheight= 0.09) 

        self.botao7 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="7", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao7.place(relx= 0.03, rely= 0.77, relwidth= 0.22, relheight= 0.09)

        self.botao8 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="8", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao8.place(relx= 0.27, rely= 0.77, relwidth= 0.22, relheight= 0.09) 

        self.botao9 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="9", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao9.place(relx= 0.51, rely= 0.77, relwidth= 0.22, relheight= 0.09) 

        self.botao_cancela = Button(self.root, bg="#E9441B", highlightbackground="#C10D01", highlightthickness=3, text="Cancela", 
                                    font=self.tela_fonte,  activebackground="#C10D01")
        self.botao_cancela.place(relx= 0.03, rely= 0.88, relwidth= 0.22, relheight= 0.09)

        self.botao0 = Button(self.root, bg="#9D9B9B", highlightbackground="#4D4D4D", highlightthickness=3, text="0", 
                             font=self.tela_fonte,  activebackground="#4D4D4D")
        self.botao0.place(relx= 0.27, rely= 0.88, relwidth= 0.22, relheight= 0.09) 

        self.botao_confirma = Button(self.root, bg="#28A80F", highlightbackground="#20850D", highlightthickness=3, text="Confirma", 
                                     font=self.tela_fonte,  activebackground="#20850D")
        self.botao_confirma.place(relx= 0.51, rely= 0.88, relwidth= 0.22, relheight= 0.09) 