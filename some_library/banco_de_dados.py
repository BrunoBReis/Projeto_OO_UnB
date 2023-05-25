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


#with open("Clientes.json") as file:
#    clientes = json.load(file)

def cadastrar_user(clientes, tipo, nome, endereco, telefone, senha, codigo):
    novo_cliente = {"Tipo" : tipo, "Nome" : nome, "Endereco" : endereco, "Telefone" : telefone, "Senha" : senha}
    clientes.update({codigo : novo_cliente})
    with open("Clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

clientes = {}
cadastrar_user(clientes, "Pessoa", "Julia", "abcdef", "99122-3445", "abcd123", "100027")