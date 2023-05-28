import json

class SistemaBancario:
    def __init__(self):
        self.bancoDados = BancoDeDados()
    
    def menu(self):
        pass

class BancoDeDados:

    def __init__(self):
        with open("Gerentes.json") as GeFile:
            self.gerentes = json.load(GeFile)
        with open("Clientes.json") as CliFile:
            self.clientes = json.load(CliFile)
        with open("Historico.json") as HistFile:
            self.historico = json.load(HistFile)

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
