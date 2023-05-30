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

    def cadastrar_user(self, clientes, tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj, saldo):
        novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha, "CPF/CNPJ" : cpf_cnpj, "Saldo" : saldo}
        clientes.update({codigo : novo_cliente})
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
    
    def remover_user(self, clientes, codigo):
        clientes.pop(codigo, "ok")
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
    
    def editar_user(self, clientes, codigo):
        print ("""O que você quer editar?
    1)Nome
    2)Endereco
    3)Telefone
    4)Senha
    5)Sair do modo de edição""")
        res = input("Resposta: ")
        if res == "1":
            clientes[codigo]["Nome"] = input("Novo Nome: ")
        if res == "2":
            clientes[codigo]["Endereco"] = input("Novo Endereco: ")
        if res == "3":
            clientes[codigo]["Telefone"] = input("Nova Telefone: ")
        if res == "4":
            clientes[codigo]["Senha"] = input("Nova Senha: ")
        else:
            pass
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
        
    def visualiza_user(self, clientes):
        for conta in clientes:
            print (f"[{conta}]\n\n")
            for item in clientes[conta]:
                print (f"{item}: {clientes[conta][item]}")
            print ("\n\n")

class Cliente(Usuario):
    def __init__(self, saldo, nome, endereco, telefone, senha, codigo):
        super().__init__(nome, endereco, telefone, senha, codigo)
        self.saldo = saldo

    def sacar(self):
        pass
    
    def depositar(self):
        pass

    def pagamento_programado(self):
        pass
    
    def visualiar_historico(self):
        pass
    
    
class Empresa(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cnpj):
        super().__init__(saldo, nome, endereco, telefone, senha)
        self.cnpj = cnpj

    def solicitar_credito(self):
        pass
    
class PessoaFisica(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cpf):
        super().__init__(saldo, nome, endereco, telefone, senha)
        self.cpf = cpf

    def solicitar_credito(self):
        pass
