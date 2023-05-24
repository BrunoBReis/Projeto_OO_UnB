class SistemaBancario:
    def __init__(self):
        pass
    
    def menu(self):
        pass

class BancoDeDados:
    def __init__(self, gerentes, clientes):
        self.gerentes = {}
        self.clientes = {}

    def armazena_dados(self):
        pass

    def busca_dados(self):
        pass

class Usuario:
    def __init__(self, nome, endereco, telefone, senha):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha

class Gerente(Usuario):
    def __init__(self, nome, endereco, telefone, senha):
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
    def __init__(self, saldo, nome, endereco, telefone, senha):
        super().__init__(nome, endereco, telefone, senha)
        self.saldo = 0

    def sacar(self):
        pass
    
    def depositar(self):
        pass

    def pagamento_programado(self):
        pass
    
    def visualiar_historico(self):
        pass
    
    def solicitar_credito(self):
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