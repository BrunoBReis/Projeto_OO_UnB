from some_library.atm import *
import json

def workspace():
    # armazenando os caminhos dos dados
    clientes_directory = 'Clientes.json'
    gerentes_directory = 'Gerentes.json'
    historico_directory = 'Historico.json'
    pagamento_programado_directory = 'Pagamento_programado.json'

    # criando um objeto para gerente e pessoa
    gerente = Gerente('Bruno', 'SHIS QL 10 conj 5', '91234-5678', '123', '100012', 'gerente')
    pessoa = PessoaFisica(1000, 'Joao', 'SQS 202 bloco d', '91234-1234', '1234', '123.456.789-00', 'Pessoa', '000012')


    # abrindo o banco de dados
    with open(clientes_directory) as clientes_file:
        lista_clientes = json.load(clientes_file)

    with open(gerentes_directory) as gerentes_file:
        lista_gerentes = json.load(gerentes_file)
    
    with open(historico_directory) as historico_file:
        lista_historico = json.load(historico_file)

    with open(pagamento_programado_directory) as pagamento_programado_file:
        lista_pagamento_programado = json.load(pagamento_programado_file)


    # fazendo as alterações na conta 
    #pessoa.sacar(100, lista_clientes, '000184')
    #pessoa.depositar(1000, lista_clientes, '000184')

    # visualizando o historico

    pessoa.pagamento_programado('15/06/2023', 200, lista_pagamento_programado, '000184')
    
if __name__ == '__main__':
    workspace()