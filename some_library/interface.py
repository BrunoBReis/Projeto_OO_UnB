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
        self.cod = self.en_conta.get()
        self.senha = self.en_senha.get()
        if (self.cod in self.bancoDados.gerentes) == True:
            if (self.senha == self.bancoDados.gerentes[self.cod]["Senha"]) == True:
                nome = self.bancoDados.gerentes[self.cod]["Nome"]
                print(f"Login com Sucesso! Seja bem vindo {nome}")
                self.limpa_tela(self.frame1)
                self.usuario =  self.bancoDados.gerentes[self.cod]
                return ""
            else:
                return "Falha no login! Senha incorreta!"
        elif (self.cod in self.bancoDados.clientes) == True:
            if (self.senha == self.bancoDados.clientes[self.cod]["Senha"]) == True:
                nome = self.bancoDados.clientes[self.cod]["Nome"]
                print(f"Login com Sucesso! Seja bem vindo {nome}")
                self.limpa_tela(self.frame1)
                self.usuario = self.bancoDados.clientes[self.cod]
                return ""
            else:
                return "Falha no login! Senha incorreta!"
        else: 
            return "Falha no login, conta inexistente!"
        
                
        
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

# Construindo a interface inicial

        self.root = root
        self.interface_basica()
        self.frames_da_tela()
        self.tela_inicial()
        self.criando_botoes()
        root.mainloop()

# Função para construção da página de login

    def tela_login(self, aviso):
        self.limpa_tela(self.frame1)
        self.login = Label(self.frame1, text = "LOGIN", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
        self.login.place(relx=0.5, rely=0.04, anchor=CENTER)

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
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_usuario())
        self.bt_logar.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.1, anchor=CENTER)

        self.bt_voltar = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Voltar", 
                                  font= ("Terminal", "12", "bold"), activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_inicial())
        self.bt_voltar.place(relx=0.88, rely=0.90, relwidth=0.11, relheight=0.09)


# Função para construção da tela de usuário
# Tive que fazer uma gambiarra e essa função também faz parte de confirmar se os dados 
# estão coerentes e gerar a pagina correspondente para o devido tipo de usuário ("Gerente" ou "Cliente")

    def tela_usuario(self):
        aviso = self.logar()

        self.bt_log_out = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Log Out", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_inicial())
        self.bt_log_out.place(relx=0.91, rely=0.04, relwidth=0.19, relheight=0.1, anchor=CENTER)

        if self.usuario == {}:
            self.tela_login(aviso)
        
        elif ("Saldo" in self.usuario) == True:
            if self.usuario["Tipo"] == "Empresa":
                self.user = Empresa(self.usuario["Saldo"], self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], self.usuario["CPF/CNPJ"], self.usuario["Tipo"], self.cod)
                
            else:
                self.user = PessoaFisica(self.usuario["Saldo"], self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], self.usuario["CPF/CNPJ"], self.usuario["Tipo"], self.cod)
                
            self.t_cliente = Label(self.frame1, text = "CLIENTE", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
            self.t_cliente.place(relx=0.5, rely=0.04, anchor=CENTER)  

        elif self.usuario["Tipo"] == "Gerente":
                self.user = Gerente(self.usuario["Nome"], self.usuario["Endereco"], self.usuario["Telefone"], self.usuario["Senha"], "000100", self.usuario["Tipo"])   
                
                self.t_gerente = Label(self.frame1, text = "GERENTE", foreground="#50C649", background="#1C1C1C", font=self.tela_fonte)
                self.t_gerente.place(relx=0.5, rely=0.04, anchor=CENTER)
            
# Função para construir a interface principal (caixa eletrônico), e que diferentemente da tela, é imutável

    def interface_basica(self):
        self.root.title("Caixa Bancário")
        self.root.configure(background="#5E5D5D") 
        self.root.geometry("700x700")
        self.root.resizable(False, False)

# Criação do frame da tela "digital"

    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd = 4, bg="#1C1C1C", highlightbackground= "#4D4D4D", highlightthickness=6)
        self.frame1.place(relx= 0.03, rely= 0.03, relwidth= 0.94, relheight= 0.50)

# Função constroi a tela inicial de quando ligamos o prgrama

    def tela_inicial(self):

        self.limpa_tela(self.frame1)

        self.menu = Label(self.frame1, text = "  MENU  ", foreground="#50C649", background="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, font=self.tela_fonte)
        self.menu.place(relx=0.5, rely=0.04, anchor=CENTER)


        self.botao_login = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Login", 
                                  font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=lambda : self.tela_login(""))
        self.botao_login.place(relx=0.5, rely=0.42, relwidth=0.4, relheight=0.1, anchor=CENTER)


        self.botao_sair = Button(self.frame1, bg="#1C1C1C", highlightbackground="#50C649", highlightthickness=1.5, foreground="#50C649", text="Sair", 
                                 font=self.tela_fonte, activebackground="#50C649", activeforeground="#1C1C1C", command=self.root.quit)
        self.botao_sair.place(relx=0.5, rely=0.54, relwidth=0.4, relheight=0.1, anchor=CENTER)

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