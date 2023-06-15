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
        with open("Pagamento_programado.json") as Pagfile:
            self.programado = json.load(Pagfile)
        with open("Atualizacoes.json") as Atufile:
            self.atualizacoes = json.load(Atufile)


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
    
    def cadastrar_user(self, clientes, historico, programado, tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj, saldo):
        novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha, "CPF/CNPJ" : cpf_cnpj, "Saldo" : saldo, "Credito" : 0.0}
        clientes.update({codigo : novo_cliente})
        historico.update({codigo : {}})
        programado.update({codigo : {}})
        with open("Clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
        with open("Historico.json", "w") as arquivo:
            json.dump(historico, arquivo, indent=4)
        with open("Pagamento_programado.json", "w") as arquivo:
            json.dump(programado, arquivo, indent=4)
    
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

    def sacar(self, valor, clientes, codigo, saldo):
        saldo -= valor
        clientes[codigo]["Saldo"] = saldo
        with open('Clientes.json', 'w') as clientes_file:
            json.dump(clientes, clientes_file, indent=4)
        self.registrar_transacao(valor, codigo, 'Saque', saldo)
    
    def depositar(self, valor, clientes, codigo, saldo):
        clientes[codigo]['Saldo'] += valor
        saldo += valor
        with open('Clientes.json', 'w') as clientes_file:
            json.dump(clientes, clientes_file, indent=4)
        self.registrar_transacao(valor, codigo, 'Deposito', saldo)
        
    # sugestão do professor foi fazer uma implentação disso no json como um pagamento
    # que está agendado e posteriormente confirmar essa data com algum bibloteca 
    # depois relizar o pagamento automaticamente
    def pagamento_programado(self, programado, dic, codigo, num):
        programado[codigo].update({num : dic})
        
        with open('Pagamento_programado.json', 'w') as pagfile:
            json.dump(programado, pagfile, indent=4)
    
    def visualizar_historico(self):
        with open('Historico.json') as historico_file:
            historico_lista = json.load(historico_file)

        for item in historico_lista:
            for key, value in item.items():
                print(f'{key}:\t {value}')
            print('--------------------')

    def registrar_transacao(self, valor, codigo, tipo_transacao, saldo):
        data_hoje = datetime.datetime.now()
        data_hoje_str = data_hoje.strftime("%d/%m/%Y")
        data_agora_str = data_hoje.strftime("%I:%M:%S")

        with open('Historico.json') as historico_file:
            historico_dic = json.load(historico_file)

        transacao = {data_agora_str : {'Tipo' : tipo_transacao,
                                        'Valor' : valor,
                                        'Saldo final' : saldo}}
        
        transacao2 = {'Tipo' : tipo_transacao,
                    'Valor' : valor,
                    'Saldo final' : saldo}
        
        if (data_hoje_str in historico_dic[codigo]) == True:
            historico_dic[codigo][data_hoje_str].update({data_agora_str : transacao2})
  
        else:
            historico_dic[codigo].update({data_hoje_str : transacao})

        with open('Historico.json', 'w') as historico_update:
            json.dump(historico_dic, historico_update, indent=4)
        

    

#---------------------------------------------------------------------------------------
#------------------CLASSE EMPRESA-------------------------------------------------------
#---------------------------------------------------------------------------------------

    
class Empresa(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cnpj, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cnpj = cnpj

# a ideia de slocitar crédito partiria de utilizar o pagamento agendado e acrescentar um juros
# para ser pago em uma certa data
    def solicitar_credito(self, valor, clientes, codigo, credito, saldo):
        credito += valor
        saldo += valor
        clientes[codigo]["Saldo"] = saldo
        clientes[codigo]["Credito"] = credito
        with open('Clientes.json', 'w') as clientes_file:
            json.dump(clientes, clientes_file, indent=4)
        self.registrar_transacao(valor, codigo, 'Credito', saldo)
    

#---------------------------------------------------------------------------------------
#------------------CLASSE PESSOA FÍSICA-------------------------------------------------------
#---------------------------------------------------------------------------------------

class PessoaFisica(Cliente):
    def __init__(self, saldo, nome, endereco, telefone, senha, cpf, tipo, codigo):
        super().__init__(saldo, nome, endereco, telefone, senha, tipo, codigo)
        self.cpf = cpf

    def solicitar_credito(self, valor, clientes, codigo, credito, saldo):
        credito += valor
        saldo += valor
        clientes[codigo]["Saldo"] = saldo
        clientes[codigo]["Credito"] = credito
        with open('Clientes.json', 'w') as clientes_file:
            json.dump(clientes, clientes_file, indent=4)
        self.registrar_transacao(valor, codigo, 'Credito', saldo)
