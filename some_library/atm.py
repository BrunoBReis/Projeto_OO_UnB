import json
import datetime

#---------------------------------------------------------------------------------------
#------------------CLASSE BANCO DE DADOS-------------------------------------------------------
#---------------------------------------------------------------------------------------

class BancoDeDados:

# Função construtora para pegar a base de dados nos arquivos ".json" e tranformar em dict no codigo

    def __init__(self):
        with open("Gerentes.json") as GeFile:
            self.gerentes = json.load(GeFile)
        with open("Clientes.json") as CliFile:
            self.clientes = json.load(CliFile)
        with open("Historico.json") as HistFile:
            self.historico = json.load(HistFile)


#---------------------------------------------------------------------------------------
#------------------CLASSE USUÁRIO-------------------------------------------------------
#---------------------------------------------------------------------------------------

# na classe usuário precisa-se colar um atributo de limite com um valor fixo de 1000
class Usuario:
    
    def __init__(self, nome, endereco, telefone, senha, codigo, tipo):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha
        self.codigo = codigo
        self.tipo = tipo

#---------------------------------------------------------------------------------------
#------------------CLASSE GERENTE-------------------------------------------------------
#---------------------------------------------------------------------------------------

class Gerente(Usuario):
    
    def __init__(self, nome, endereco, telefone, senha, codigo, tipo):
        super().__init__(nome, endereco, telefone, senha, codigo, tipo)
    
    def cadastrar_user(self, clientes, tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj, saldo):
        novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha, "CPF/CNPJ" : cpf_cnpj, "Saldo" : saldo}
        clientes.update({codigo : novo_cliente})
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
    
    def remover_user(self, clientes, codigo):
        clientes.pop(codigo, "Cliente não existe")
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
    
    def editar_user(self, clientes, codigo, dado, novo_dado):
        clientes[codigo][dado] = novo_dado
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
        
    def visualiza_user(self, clientes):
        for conta in clientes:
            print (f"[{conta}]\n\n")
            for item in clientes[conta]:
                print (f"{item}: {clientes[conta][item]}")
            print ("\n\n")


#---------------------------------------------------------------------------------------
#------------------CLASSE CLIENTE-------------------------------------------------------
#---------------------------------------------------------------------------------------

class Cliente(Usuario):
    def __init__(self, saldo, nome, endereco, telefone, senha, codigo, tipo):
        super().__init__(nome, endereco, telefone, senha, codigo, tipo)
        self.saldo = saldo

    def sacar(self, valor, clientes, codigo):
        if valor <= clientes[codigo]['Saldo']:
            clientes[codigo]['Saldo'] -= valor
            with open('Clientes.json', 'w') as clientes_file:
                json.dump(clientes, clientes_file, indent=4)
            self.registrar_transacao(valor, codigo, tipo_transacao='Saque')
        else:
            print('Valor maior do que o saldo da conta')
    
    def depositar(self, valor, clientes, codigo):
        clientes[codigo]['Saldo'] += valor
        with open('Clientes.json', 'w') as clientes_file:
            json.dump(clientes, clientes_file, indent=4)
        self.registrar_transacao(valor, codigo, tipo_transacao='Deposito')
        
    # sugestão do professor foi fazer uma implentação disso no json como um pagamento
    # que está agendado e posteriormente confirmar essa data com algum bibloteca 
    # depois relizar o pagamento automaticamente
    def pagamento_programado(self):
        pass
    
    def visualiar_historico(self):
        with open('Historico.json') as historico_file:
            historico_lista = json.load(historico_file)

        for item in historico_lista:
            for key, value in item.items():
                print(f'{key}:\t {value}')
            print('--------------------')

    def registrar_transacao(self, valor, codigo, tipo_transacao):
        transacao = {'Codigo' : codigo,
                     'Tipo' : tipo_transacao,
                     'Valor' : valor}
        
        with open('Historico.json') as historico_file:
            historico_lista = json.load(historico_file)
        
        historico_lista.append(transacao)

        with open('Historico.json', 'w') as historico_update:
            json.dump(historico_lista, historico_update, indent=4)
        

    

#---------------------------------------------------------------------------------------
#------------------CLASSE EMPRESA-------------------------------------------------------
#---------------------------------------------------------------------------------------

    
class Empresa(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cnpj, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cnpj = cnpj

# a ideia de slocitar crédito partiria de utilizar o pagamento agendado e acrescentar um juros
# para ser pago em uma certa data
    def solicitar_credito(self):
        pass
    

#---------------------------------------------------------------------------------------
#------------------CLASSE PESSOA FÍSICA-------------------------------------------------------
#---------------------------------------------------------------------------------------

class PessoaFisica(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cpf, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cpf = cpf

    def solicitar_credito(self):
        pass
