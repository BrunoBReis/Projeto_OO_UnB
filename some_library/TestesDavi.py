from atm import *

# Criando e testando as funções recém criadas (Caso esteja 100% aprovada eu coloco no "atm.py")


# Testando as funções
while True:
    print("""START
1) Login
2) Fechar Programa\n\n""")
    res = input("Resposta: ")
    if res == "1":
        start = SistemaBancario()
    else:
        break

    while True:
        if start.user.tipo == "Gerente":
            print("""GERENTE
            
    1) Cadastrar novo cliente
    2) Remover Cliente
    3) Editar conta de um cliente
    4) visualizar clientes
    5) Sair do programa\n""")
            res = input("Resposta: ")
            if res == "1":
                print("""Digite em ordem as seguintes informações: """)
                tipo = input("Tipo: ")
                nome = input("Nome: ")
                endereco = input("Endereco: ")
                telefone = input("Telefone: ")
                senha = input("Senha: ")
                codigo = input("Codigo: ")
                cpf_cnpj = input("CPF/CNPJ: ")
                saldo = input("Saldo: ")
                saldo = float(saldo)
                start.user.cadastrar_user(start.bancoDados.clientes,tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj, saldo)

            elif res =="2":
                print("Quem você gostaria de remover: \n\n")
                start.user.visualiza_user(start.bancoDados.clientes)
                cod = input("Resposta: ")
                start.user.remover_user(start.bancoDados.clientes, cod)

            elif res == "3":
                print("Quem você gostaria de editar: \n\n")
                start.user.visualiza_user(start.bancoDados.clientes)
                cod = input("Resposta: ")
                start.user.editar_user(start.bancoDados.clientes, cod)

            elif res == "4":
                start.user.visualiza_user(start.bancoDados.clientes)

            else:
                break
        else:
            print ("""CLIENTE

    1) Sacar
    2) Depositar
    3) Pagamento Programado
    4) Histórico
    5) solicitar crédito
    6) Sair do programa\n\n""")
            res = input("Resposta: ")
            if res == "1":
                pass
            elif res == "2":
                pass
            elif res == "3":
                pass
            elif res == "4":
                pass
            elif res == "5":
                pass
            else:
                break 