import json

class DataBank_Gerente():

    def get_data (self, name = "Gerentes.json"):
        with open(name) as arquivo:
            gerentes = json.load(arquivo)
        print (gerentes)

class DataBank_Clientes():

    def get_data (self, name = "Clientes.json"):
        with open(name) as arquivo:
            clientes = json.load(arquivo)
        print (clientes)

class DataBank_Historico():

    def get_data (self, name = "Historico.json"):
        with open(name) as arquivo:
            historico = json.load(arquivo)
        print (historico)


def cadastrar_user(clientes, tipo, nome, endereco, telefone, senha, codigo, cpf_cnpj):
    novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha, "CPF/CNPJ" : cpf_cnpj}
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


with open("Clientes.json") as file:
    clientes = json.load(file)
cadastrar_user(clientes, "Pessoa", "Julia", "abcdef", "99122-3445", "abcd123", "100027", "73809566666")
cadastrar_user(clientes, "Empresa", "Apple", "jbfahsdbjv", "8000-3420", "apple2000", "000184", "20-2394889898.38")
#remover_user(clientes, "100027")
#editar_user(clientes, "100027")
with open("Clientes.json") as file:
    clientes = json.load(file)
visualiza_user(clientes)