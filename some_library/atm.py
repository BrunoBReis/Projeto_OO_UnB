import json

class SistemaBancario:

# Criando uma composição da classe "BancoDeDados" em "SistemaBancario"

    def __init__(self):
        self.bancoDados = BancoDeDados()
    
# Função para reconhecer código da conta e senha para logar como "Gerente" ou "Cliente"

    def login(self):
        print("""Escolha uma das opções abaixo:
1) Gerente
2) Cliente

Resposta: """)
        esco = input(" ")
        if esco  == "1":
            print("\n\n GERENTE \n\n")
            cod = input("Código da conta: ")
            senha = input("Senha: ")
            if (cod in self.bancoDados.gerentes) == True:
                if (senha in self.bancoDados.gerentes[cod]["Senha"]) == True:
                    self.bancoDados.ger = self.bancoDados.gerentes[cod]
                    nome = self.bancoDados.ger["Nome"]
                    print(f"Login com Sucesso! Seja bem vindo {nome}")
                else:
                    print("Falha no login! Senha incorreta!")
            else: 
                print("Falha no login, conta inexistente!")
        else:
            print("\n\n CLIENTE \n\n")
            cod = input("Código da conta: ")
            senha = input("Senha: ")
            if (cod in self.bancoDados.clientes) == True:
                if (senha in self.bancoDados.clientes[cod]["Senha"]) == True:
                    self.bancoDados.cli = self.bancoDados.clientes[cod]
                    nome = self.bancoDados.cli["Nome"]
                    print(f"Login com Sucesso! Seja bem vindo {nome}")
                else:
                    print("Falha no login! Senha incorreta!")
            else: 
                print("Falha no login, conta inexistente!")
        

    def menu(self):
        pass

class BancoDeDados:

# Função construtora para pegar a base de dados nos arquivos ".json" e tranformar em dict no codigo
# "Self.hist", "self.cli" e "self.ger" são objetos temporários para receber o cliente recém-logado

    def __init__(self):
        with open("Gerentes.json") as GeFile:
            self.gerentes = json.load(GeFile)
        with open("Clientes.json") as CliFile:
            self.clientes = json.load(CliFile)
        with open("Historico.json") as HistFile:
            self.historico = json.load(HistFile)
        self.hist = {}
        self.cli = {}
        self.ger = {}

    def armazena_dados(self):
        pass

    def busca_dados(self):
        pass
        

class Usuario:
    def __init__(self, nome, endereco, telefone, senha, codigo):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha
        self.codigo = codigo

class Gerente(Usuario):
    def __init__(self, nome, endereco, telefone, senha, codigo):
        super().__init__(nome, endereco, telefone, senha)

    def cadastrar_user(self):
        pass
    
    def remover_user(self):
        pass
    
    def editar_user(self):
        pass
    
    def visualiza_user(self):
        pass

class Cliente(Usuario):
    def __init__(self, saldo, nome, endereco, telefone, senha, codigo):
        super().__init__(nome, endereco, telefone, senha, codigo)
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Você sacou {valor} reais da sua conta')
        else:
            print(f'{self.nome}saldo insuficiente')
    
    def depositar(self):
        pass

    def pagamento_programado(self):
        pass
    
    def visualiar_historico(self):
        pass
    
    
class Empresa(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cnpj, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, codigo)
        self.cnpj = cnpj

    def solicitar_credito(self):
        pass
    
class PessoaFisica(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cpf, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, codigo)
        self.cpf = cpf

    def solicitar_credito(self):
        pass
