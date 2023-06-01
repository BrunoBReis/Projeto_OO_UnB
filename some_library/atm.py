import json

class BancoDeDados:

# Função construtora para pegar a base de dados nos arquivos ".json" e tranformar em dict no codigo

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
        
# na classe usuário precisa-se colar um atributo de limite com um valor fixo de 1000
class Usuario:
    
    def __init__(self, nome, endereco, telefone, senha, codigo, tipo):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha
        self.codigo = codigo
        self.tipo = tipo

class Gerente(Usuario):
    
    def __init__(self, nome, endereco, telefone, senha, codigo, tipo):
        super().__init__(nome, endereco, telefone, senha, codigo, tipo)
    
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
    def __init__(self, saldo, nome, endereco, telefone, senha, codigo, tipo):
        super().__init__(nome, endereco, telefone, senha, codigo, tipo)
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Você sacou {valor} reais da sua conta')
        else:
            print(f'{self.nome} saldo insuficiente')
    
    def depositar(self):
        pass

    # sugestão do professor foi fazer uma implentação disso no json como um pagamento
    # que está agendado e posteriormente confirmar essa data com algum bibloteca 
    # depois relizar o pagamento automaticamente
    def pagamento_programado(self):
        pass
    
    def visualiar_historico(self):
        pass
    
    
class Empresa(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cnpj, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cnpj = cnpj

# a ideia de slocitar crédito partiria de utilizar o pagamento agendado e acrescentar um juros
# para ser pago em uma certa data
    def solicitar_credito(self):
        pass
    
class PessoaFisica(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cpf, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cpf = cpf

    def solicitar_credito(self):
        pass
