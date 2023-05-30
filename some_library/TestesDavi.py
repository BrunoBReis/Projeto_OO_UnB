from atm import *

# Criando e testando as funções recém criadas (Caso esteja 100% aprovada eu coloco no "atm.py")

def cadastrar_user(clientes, tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj, saldo):
    novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha, "CPF/CNPJ" : cpf_cnpj, "Saldo" : saldo}
    clientes.update({codigo : novo_cliente})
    with open("Clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

def remover_user(clientes, codigo):
    clientes.pop(codigo, "ok")
    with open("Clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

def editar_user(clientes, codigo):
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

def visualiza_user(clientes):
    for conta in clientes:
        print (f"[{conta}]\n\n")
        for item in clientes[conta]:
            print (f"{item}: {clientes[conta][item]}")
        print ("\n\n")


# Testando as funções

start = SistemaBancario()

#while True:
print(start.user.nome)